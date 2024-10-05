from mongoengine import EmbeddedDocument, StringField


class FoundersHallEmbeddedModel(EmbeddedDocument):
    phone = StringField(required=True)
