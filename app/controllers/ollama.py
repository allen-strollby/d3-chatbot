from collections.abc import Callable
from functools import partial
import ollama
import json_repair
from databases.enums import DivisionTypeEnum
from controllers.map import controller_map
import os


def get_ollama_response(question: str):
    if os.environ.get("DOCKER_COMPOSE"):
        client = ollama.Client(host="http://ollama:11434")
    else:
        client = ollama.Client()
    response = client.generate(model="maapu", prompt=question)

    ollama_response = response["response"]

    print("Start of Ollama Response")
    print(ollama_response)
    print("End of Ollama Response")

    data = json_repair.loads(ollama_response)
    print(data)

    if not isinstance(data, dict):
        return None

    if data.get("error"):
        return None

    return data


def get_controller_from_question(question: str) -> dict | Callable:
    data = get_ollama_response(question)

    # Retry if first did not work
    if not data:
        data = get_ollama_response(question)
    if not data:
        return {"status": "Invalid Json Returned from Ollama"}

    location_type = data.get("location_type")

    if not location_type:
        return {"status": "Ollama did not return a location type"}

    location_type = location_type.upper()

    if location_type not in DivisionTypeEnum:
        return {"status": f"{location_type} is an invalid location type"}
    controller = controller_map.get(DivisionTypeEnum(location_type))

    if not controller:
        return {
            "status": f"The controller for location type {location_type} is not implemented"
        }

    if args := data.get("args"):
        return partial(controller, **args)

    return controller
