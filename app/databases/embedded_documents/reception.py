from mongoengine import EmbeddedDocumentField, StringField


class ReceptionEmbeddedModel(EmbeddedDocumentField):
    phone = StringField(required=True)
