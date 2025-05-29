from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import base64
from model import search_data
from PIL import Image
import io

app = FastAPI()

class Query(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
async def virtual_ta(query: Query):
    # Optional image decoding
    if query.image:
        try:
            image_bytes = base64.b64decode(query.image)
            img = Image.open(io.BytesIO(image_bytes))
            # You can apply OCR or image-to-text here if needed
        except Exception as e:
            pass  # Just skip image processing for now

    answer, links = search_data(query.question)

    return {
        "answer": answer,
        "links": links
    }
