from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

import logging

import settings  # noqa
from routers import health_check_router, chatbot_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
    logging.error(f"{request}: {exc_str}")
    content = {"status_code": 10422, "message": exc_str, "data": None}
    return JSONResponse(
        content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health_check_router, prefix="")
app.include_router(chatbot_router, prefix="/chat")

# todo: Indexing of documents
# todo: Controllers
# todo: Advanced Queries for Chatbot
# todo: Script for populating db
# todo: Connection to cloud Atlas
# todo: Web Server Deployment
# todo: Availability and authorization of meeting rooms
# todo: Questions regarding training room
# todo: People's meeting status
