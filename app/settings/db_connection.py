from mongoengine import connect
import os

if os.environ.get("DOCKER_COMPOSE"):
    connect(host="mongodb://mongodb:27017/ChatbotDB")
else:
    connect(db="ChatbotDB")
