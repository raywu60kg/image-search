from abc import ABC, abstractmethod
from enum import Enum
from functools import lru_cache

import numpy as np
import torch
from numpy.typing import NDArray
from PIL import Image
from transformers import CLIPModel, CLIPProcessor  # type: ignore

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")  # type: ignore
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")  # type: ignore
dummy_image = Image.new("RGB", (1, 2))


class EmbeddingModelEnum(Enum):
    CLIP = "clip"


class EmbeddingStrategy(ABC):
    @abstractmethod
    def calculate_query_embedding(self, query: str) -> NDArray[np.float32]:
        pass


class ClipEmbedding(EmbeddingStrategy):
    @lru_cache(128)
    def calculate_query_embedding(self, query: str) -> NDArray[np.float32]:  # type: ignore
        inputs = processor(  # type: ignore
            text=query, images=[dummy_image], return_tensors="pt", padding=True
        )
        with torch.no_grad():
            outputs = model(**inputs)  # type: ignore
        text_embedding = outputs.text_embeds / outputs.text_embeds.norm(  # type: ignore
            dim=-1, keepdim=True
        )
        return text_embedding.reshape(-1).numpy()  # type: ignore


class DummyEmbedding(EmbeddingStrategy):
    def calculate_query_embedding(self, query: str) -> NDArray[np.float32]:
        return np.zeros(512, dtype=np.float32)
