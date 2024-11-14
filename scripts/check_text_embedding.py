import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor

# Load pre-trained CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load images
images = [
    Image.open("image_data/val2014/COCO_val2014_000000000042.jpg"),
    Image.open("image_data/val2014/COCO_val2014_000000000073.jpg"),
]


# Preprocess inputs
inputs = processor(
    text=["cat", "cat"], images=images, return_tensors="pt", padding=True
)

# Generate embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Extract and normalize image and text embeddings

text_embeddings_1 = outputs.text_embeds / outputs.text_embeds.norm(dim=-1, keepdim=True)
print(text_embeddings_1.size())
# print(cosine_similarity(text_embeddings_1[0].squeeze(), text_embeddings_1[1].squeeze()))
# print(text_embeddings_1[0] == text_embeddings_2[1])
print(torch.equal(text_embeddings_1[0], text_embeddings_1[1]))
