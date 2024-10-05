from mongoengine import EmbeddedDocument, StringField


class MainHallEmbeddedModel(EmbeddedDocument):
    phone = StringField(required=True)
