import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor

# Load pre-trained CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

img = Image.new("RGB", (1, 2))
print(img.size)
print(img.mode)
# Preprocess inputs
inputs = processor(text="cat", images=[img], return_tensors="pt", padding=True)

# Generate embeddings
with torch.no_grad():
    outputs = model(**inputs)

text_embeddings = outputs.text_embeds / outputs.text_embeds.norm(dim=-1, keepdim=True)
print(text_embeddings.size(), type(text_embeddings))
text_embeddings = text_embeddings.reshape(-1)
print(text_embeddings.size())
text_numpy = text_embeddings.numpy()
print(type(text_numpy), text_numpy.shape)
print(type(text_numpy[0]))
