from mongoengine import EmbeddedDocumentField, StringField


class ServerEmbeddedModel(EmbeddedDocumentField):
    server_type = StringField(required=True)
