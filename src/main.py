from fastapi import FastAPI

from src.adapter.inward.web.common.middleware.redirect_tailing_slash import (
    RedirectTailingSlashMiddleware,
)
from src.adapter.inward.web.feedback.router import router as feedback_router
from src.adapter.inward.web.image.router import router as image_router

app = FastAPI()

app.add_middleware(RedirectTailingSlashMiddleware)

app.include_router(image_router)
app.include_router(feedback_router)
