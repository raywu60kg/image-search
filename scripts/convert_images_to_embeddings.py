import os

import numpy as np
import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor  # type: ignore

image_dir = "image_data/val2014"
output_embedding_dir = "image_data/val2014_embeddings/clip.npy"

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")  # type: ignore
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")  # type: ignore


images = [
    Image.open(os.path.join(image_dir, file_name))
    for file_name in os.listdir(image_dir)
]
# Preprocess inputs
inputs = processor(text="", images=images, return_tensors="pt", padding=True)  # type: ignore

# Generate embeddings
with torch.no_grad():  # type: ignore
    outputs = model(**inputs)  # type: ignore

# Extract and normalize image and text embeddings
image_embeddings = outputs.image_embeds / outputs.image_embeds.norm(  # type: ignore
    dim=-1, keepdim=True
)

with open(output_embedding_dir, "wb") as f:
    np.save(f, image_embeddings.numpy())  # type: ignore
