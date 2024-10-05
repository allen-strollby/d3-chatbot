from mongoengine import Document


class EventModel(Document):
    meta = {"collection": "events"}
