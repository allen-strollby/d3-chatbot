from fastapi import APIRouter

from controllers.ollama import get_controller_from_question, get_ollama_response
from fastapi import Depends, Request


router = APIRouter(tags=["Chat Router"])


def verify_user(req: Request):
    if user := req.headers.get("Authorization"):
        return user
    # Here your code for verifying the token or whatever you use
    return None


@router.get("")
def chat(question: str, user: str | None = Depends(verify_user)):
    print("Authorization", user)
    controller_or_error = get_controller_from_question(question)
    # Handling Error
    if isinstance(controller_or_error, dict):
        error = controller_or_error
        return error

    controller = controller_or_error

    return controller(user=user)


@router.get("/ollama")
def chat_ollama(question: str):
    return get_ollama_response(question)
