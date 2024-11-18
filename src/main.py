from typing import Callable

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.adapter.inward.web.common.middleware.redirect_tailing_slash import (
    RedirectTailingSlashMiddleware,
)
from src.adapter.inward.web.feedback.router import router as feedback_router
from src.adapter.inward.web.image.image_exception import SearchImageRecordIdIsNone
from src.adapter.inward.web.image.router import router as image_router
from src.adapter.outward.persistence.feedback.feedback_exception import (
    SearchImageRecordNotFoundInFeedbackMapperException,
)
from src.adapter.outward.persistence.image.image_exception import NoSimilarImage
from src.adapter.outward.persistence.search_image_record.search_image_record_exception import (
    SearchImageRecordNotFoundInDatabaseException,
)
from src.app.domain.service.feedback.give_feedback_exception import (
    SearchImageRecordNotFoundException,
)
from src.common.container import Container
from src.common.exception import ImageSearchApiError

app = FastAPI()
container = Container()
app.state.container = container
app.add_middleware(RedirectTailingSlashMiddleware)

app.include_router(image_router)
app.include_router(feedback_router)


def create_exception_handler(
    status_code: int, initial_detail: str
) -> Callable[[Request, ImageSearchApiError], JSONResponse]:
    detail = {"message": initial_detail}

    def exception_handler(_: Request, exc: ImageSearchApiError) -> JSONResponse:
        if exc.message:
            detail["message"] = exc.message

        return JSONResponse(
            status_code=status_code, content={"detail": detail["message"]}
        )

    return exception_handler


app.add_exception_handler(
    exc_class_or_status_code=SearchImageRecordNotFoundException,
    handler=create_exception_handler(404, "Search image record does not exist."),  # type: ignore
)
app.add_exception_handler(
    exc_class_or_status_code=SearchImageRecordIdIsNone,
    handler=create_exception_handler(500, "search image record data process error."),  # type: ignore
)

app.add_exception_handler(
    exc_class_or_status_code=SearchImageRecordNotFoundInFeedbackMapperException,
    handler=create_exception_handler(500, "Search image not found in feedback mapper!"),  # type: ignore
)

app.add_exception_handler(
    exc_class_or_status_code=NoSimilarImage,
    handler=create_exception_handler(500, "No similar image!"),  # type: ignore
)

app.add_exception_handler(
    exc_class_or_status_code=SearchImageRecordNotFoundInDatabaseException,
    handler=create_exception_handler(404, "Search image not found in database"),  # type: ignore
)
