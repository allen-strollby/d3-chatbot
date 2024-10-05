from mongoengine import Document, ReferenceField, DateTimeField, StringField, URLField

from databases.documents.company import CompanyModel
from databases.documents.divisions import DivisionModel


class EventModel(Document):
    meta = {"collection": "events"}
    company = ReferenceField(CompanyModel, required=True)
    venue = ReferenceField(DivisionModel, required=True)
    date = DateTimeField(required=True)
    name = StringField(required=True)
    description = StringField(required=True)
    event_link = URLField()
