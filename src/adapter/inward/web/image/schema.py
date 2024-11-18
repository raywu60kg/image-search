from pydantic import BaseModel


class ImageSearchRequest(BaseModel):
    query: str


class ImageSearchResponse(BaseModel):
    search_image_record_id: int
    base64_image: str
    image_id: int
