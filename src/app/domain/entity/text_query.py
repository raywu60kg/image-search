import numpy as np
from numpy.typing import NDArray
from PIL import Image
from transformers import CLIPModel, CLIPProcessor  # type: ignore

from src.app.domain.entity.embedding_strategy import EmbeddingStrategy

# Load pre-trained CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")  # type: ignore
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")  # type: ignore
placeholder_image = Image.new("RGB", (1, 2))


class TextQuery:
    def __init__(self, query: str, embedding_strategy: EmbeddingStrategy):
        self.__query = query
        self.__query_embedding = embedding_strategy.calculate_query_embedding(
            query=query
        )

    @property
    def query(self) -> str:
        return self.__query

    @property
    def query_embedding(self) -> NDArray[np.float32]:
        return self.__query_embedding
