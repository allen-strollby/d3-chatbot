from mongoengine import EmbeddedDocumentField, StringField


class MainHallEmbeddedModel(EmbeddedDocumentField):
    phone = StringField(required=True)
