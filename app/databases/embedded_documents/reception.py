from mongoengine import EmbeddedDocument, StringField


class ReceptionEmbeddedModel(EmbeddedDocument):
    phone = StringField(required=True)
