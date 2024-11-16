# Image Search
## Usage
### 1. Query
input a text query and return the most relevant image in base64 format from the *image_data/val2014*
```
curl http://localhost:80/v1/image/search/clip \
--header 'Content-Type: application/json' \
--data '{
    "query": "<input-text>"
}'
```

output
```json
{
    "search_image_record_id": 1,
    "base64_image": "<base64_image>",
    "image_id": 243
}
```

### 2. Give feedback
Give feedback on the *search_image_record_id* from 1. 

```bash
curl http://localhost:80/v1/feedback \
--header 'Content-Type: application/json' \
--data '{
    "feedback": "good",
    "search_image_record_id": 1
}'
```
output

```json
{
    "feedback_id": 1
}
```


### 3. (Optional) Swagger-UI
Go to the browser *http://localhost:80/docs*

## Technical Stack
- API Server: FastAPI 
- Code Architecture: Hexagonal Architecture
- Containerization: Docker / Docker Compose
- Vector search: pgvector
- Embedding model: CLIP
- Testing Framework: Pytest
- Database: PostgreSQL (with psycopg2)
- Database Migrations: Alembic
- Dependency Injection: python-dependency-injector
- Static Analysis and Linting: Mypy / Ruff

## Setup
### Requirement
- docker 
- docker-compose

###  1. Get pgvector submodule
```
git submodule init
git submodule update
```

### 2. Run
```
docker compose up
```

### 3. Wait for the alembic Database upgrade
This might take a while

## Farther discussion
- Volume for the CLIP model.
- Server return image_id then get image from CDN.
- Index in vector search.
- use join in SearchImageRecordPersistenceAdapter. 
- async.
- test case.

## Reference 
- https://huggingface.co/docs/transformers/en/model_doc/clip
- https://github.com/thombergs/buckpal 
- https://python-dependency-injector.ets-labs.org/examples/fastapi-sqlalchemy.html
- https://github.com/raywu60kg/python-clean-architecture
- https://youtu.be/7MHDDOrDx-w?si=6r7Hjc2SNHqc1REm
- https://github.com/pgvector/pgvector