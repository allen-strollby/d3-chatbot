import ollama
from fastapi import APIRouter
import json_repair

from controllers.map import controller_map
from databases.enums import DivisionTypeEnum

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

    ollama_response = response["message"]["content"]
    print("Start of Ollama Response")
    print(ollama_response)
    print("End of Ollama Response")
    data = json_repair.loads(ollama_response)
    print(data)

    if not isinstance(data, dict):
        return {"status": "The Json is Errored"}

    location_type = data.get("location_type")

    if location_type not in DivisionTypeEnum:
        return {"status": "Invalid Location Type"}

    controller = controller_map.get(DivisionTypeEnum(location_type))

    # Example data from ollama:
    # {'location_type': 'CAFETERIA', 'args': [{'food_type': 'burgers'}]}

    if args := data.get("args"):
        # Convert list of dict into single dict
        args = {k: v for d in args for k, v in d.items()}
        return controller(**args)

    return controller()
