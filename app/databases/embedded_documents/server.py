from mongoengine import EmbeddedDocument, StringField


class ServerEmbeddedModel(EmbeddedDocument):
    server_type = StringField(required=True)
