from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.adapter.inward.web.image.image_exception import SearchImageRecordIdIsNone
from src.adapter.inward.web.image.schema import ImageSearchRequest, ImageSearchResponse
from src.app.domain.entity.embedding_strategy import ClipEmbedding
from src.app.domain.entity.text_query import TextQuery
from src.app.port.inward.image.search_image_use_case import SearchImageUseCase
from src.common.container import Container

router = APIRouter(prefix="/v1/image", tags=["image"])


@router.post("/search/clip", status_code=200)
@inject
def get_most_similar_image_by_clip_cosine_score(
    request: ImageSearchRequest,
    search_image_use_case: SearchImageUseCase = Depends(
        Provide[Container.search_image_service]
    ),
) -> ImageSearchResponse:
    search_image_record = search_image_use_case.search_image_by_clip_cosine_score(
        text_query=TextQuery(query=request.query, embedding_strategy=ClipEmbedding())
    )
    if search_image_record.search_image_record_id is None:
        raise SearchImageRecordIdIsNone()

    return ImageSearchResponse(
        search_image_record_id=search_image_record.search_image_record_id.value,
        base64_image=search_image_record.result_image.base64_image,
        image_id=search_image_record.result_image.image_id.value,
    )
