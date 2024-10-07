from fastapi import FastAPI

import settings  # noqa
from routers import health_check_router, chatbot_router

app = FastAPI()

app.include_router(health_check_router, prefix="")
app.include_router(chatbot_router, prefix="/chat")

# todo: Indexing of documents
# todo: Controllers
# todo: Advanced Queries for Chatbot
# todo: Script for populating db
# todo: Connection to cloud Atlas
# todo: Web Server Deployment
