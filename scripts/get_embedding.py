import torch
from PIL import Image
from torch.nn.functional import cosine_similarity
from transformers import CLIPModel, CLIPProcessor

# Load pre-trained CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load images
images = [Image.open("image_data/val2014/COCO_val2014_000000000042.jpg")]


# Preprocess inputs
inputs = processor(text="cat", images=images, return_tensors="pt", padding=True)

# Generate embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Extract and normalize image and text embeddings
image_embeddings_1 = outputs.image_embeds / outputs.image_embeds.norm(
    dim=-1, keepdim=True
)
text_embeddings_1 = outputs.text_embeds / outputs.text_embeds.norm(dim=-1, keepdim=True)

# Preprocess inputs
inputs = processor(text="", images=images, return_tensors="pt", padding=True)

# Generate embeddings
with torch.no_grad():
    outputs = model(**inputs)
# Extract and normalize image and text embeddings
image_embeddings_2 = outputs.image_embeds / outputs.image_embeds.norm(
    dim=-1, keepdim=True
)
text_embeddings_2 = outputs.text_embeds / outputs.text_embeds.norm(dim=-1, keepdim=True)

# Compute cosine similarity
cosine_scores = cosine_similarity(image_embeddings_1, image_embeddings_2)

print(cosine_scores, type(image_embeddings_1), image_embeddings_1.size())
print(image_embeddings_1 == image_embeddings_2)
print(cosine_similarity(text_embeddings_1, text_embeddings_2))
