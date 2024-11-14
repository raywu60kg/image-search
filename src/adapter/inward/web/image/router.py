import base64
from io import BytesIO

from fastapi import APIRouter
from PIL import Image

from src.adapter.inward.web.image.schema import ImageSearchRequest, ImageSearchResponse

router = APIRouter(prefix="/v1/image", tags=["image"])


@router.post("/search", status_code=200)
def search_image(request: ImageSearchRequest) -> ImageSearchResponse:
    with Image.open("image_data/val2014/COCO_val2014_000000000042.jpg") as img:
        # Convert image to byte data
        buffered = BytesIO()
        img.save(buffered, format=img.format)
        img_bytes = buffered.getvalue()

        # Convert byte data to base64 string
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    return ImageSearchResponse(search_record_id=1, base64_image=img_base64)
