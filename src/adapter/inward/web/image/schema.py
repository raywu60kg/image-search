from pydantic import BaseModel


class ImageSearchRequest(BaseModel):
    query: str


class ImageSearchResponse(BaseModel):
    search_record_id: int
    base64_image: str
