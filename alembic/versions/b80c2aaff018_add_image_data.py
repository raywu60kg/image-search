"""add image data

Revision ID: b80c2aaff018
Revises: cdb794c720ae
Create Date: 2024-11-15 16:55:22.903318

"""

import base64
import os
from typing import Sequence, Union

import numpy as np
from sqlalchemy import text

from alembic import op
from src.app.domain.entity.embedding_strategy import EmbeddingModelEnum

# revision identifiers, used by Alembic.
revision: str = "b80c2aaff018"
down_revision: Union[str, None] = "cdb794c720ae"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
image_dir = "image_data/val2014"
image_embedding_dir = "image_data/val2014_embeddings/clip.npy"


def image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode("utf-8")
    return base64_string


def upgrade() -> None:
    conn = op.get_bind()
    base64_image_list = [
        image_to_base64(os.path.join(image_dir, file_name))
        for file_name in os.listdir(image_dir)
    ]
    image_embedding = np.load(image_embedding_dir, allow_pickle=True)

    # Insert each vector with additional metadata
    for i in range(len(base64_image_list)):
        conn.execute(
            text("""
                INSERT INTO image ( 
                    image_base64, 
                    image_embedding,
                    embedding_model
                )
                VALUES (
                    :image_base64, 
                    :image_embedding,
                    :embedding_model
                )
            """),
            {
                "image_base64": base64_image_list[i],
                "image_embedding": image_embedding[i].tolist(),
                "embedding_model": EmbeddingModelEnum.CLIP.value.upper(),
            },
        )


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(text("TRUNCATE TABLE image CASCADE"))
