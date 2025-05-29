# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
import base64
import io
from PIL import Image
import pytesseract
from model import generate_answer

app = FastAPI()

class Query(BaseModel):
    question: str
    image: str = None

@app.post("/api/")
async def answer_question(data: Query):
    question = data.question

    if data.image:
        image_data = base64.b64decode(data.image)
        image = Image.open(io.BytesIO(image_data))
        extracted_text = pytesseract.image_to_string(image)
        question += " " + extracted_text

    answer, links = generate_answer(question)
    return {"answer": answer, "links": links}
