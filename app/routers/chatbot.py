from fastapi import APIRouter
import ollama
import json

router = APIRouter(tags=["Chat Router"])


@router.get("/")
def chat(question: str):
    response = ollama.chat(
        model="maapu",
        messages=[
            {
                "role": "user",
                "content": question,
            },
        ],
    )
    data = json.loads(response["message"]["content"])
    print(data)
