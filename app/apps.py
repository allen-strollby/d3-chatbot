from fastapi import FastAPI

import settings  # noqa
from routers import health_check_router, chatbot_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
# todo: Connection to cloud Atlas
# todo: Web Server Deployment
# todo: Availability and authorization of meeting rooms
# todo: People's meeting status
# todo: Issue with food court
# todo: fix authorization
