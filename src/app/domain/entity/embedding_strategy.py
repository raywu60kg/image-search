from abc import ABC, abstractmethod
from enum import Enum

import numpy as np
import torch
from numpy.typing import NDArray
from PIL import Image
from transformers import CLIPModel, CLIPProcessor  # type: ignore

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")  # type: ignore
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")  # type: ignore
placeholder_image = Image.new("RGB", (1, 2))


class EmbeddingModelEnum(Enum):
    CLIP = "clip"


class EmbeddingStrategy(ABC):
    @abstractmethod
    def calculate_query_embedding(self, query: str) -> NDArray[np.float32]:
        pass


class ClipEmbedding(EmbeddingStrategy):
    def calculate_query_embedding(self, query: str) -> NDArray[np.float32]:
        inputs = processor(text=query, images=[], return_tensors="pt", padding=True)  # type: ignore
        with torch.no_grad():
            outputs = model(**inputs)  # type: ignore
        text_embedding = outputs.text_embeds / outputs.text_embeds.norm(  # type: ignore
            dim=-1, keepdim=True
        )
        return text_embedding.reshape(-1).numpy()  # type: ignore


class DummyEmbedding(EmbeddingStrategy):
    def calculate_query_embedding(self, query: str) -> NDArray[np.float32]:
        return np.zeros(512, dtype=np.float32)
