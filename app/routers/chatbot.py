import json
from json import JSONDecodeError

import ollama
from fastapi import APIRouter

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

    try:
        data = json.loads(response["message"]["content"])
    except JSONDecodeError:
        return {"status": "Error"}

    location_type = data.get("location_type")

    if location_type not in DivisionTypeEnum:
        return {"status": "error"}

    controller = controller_map.get(DivisionTypeEnum(location_type))

    # Example data from ollama:
    # {'location_type': 'CAFETERIA', 'args': [{'food_type': 'burgers'}]}

    if data.get("args"):
        args = data.get("args")
        # Convert list of dict into single dict
        args = {k: v for d in args for k, v in d.items()}
        return controller(**args)

    return controller()
