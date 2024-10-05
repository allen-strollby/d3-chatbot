from mongoengine import EmbeddedDocument, StringField


class GamesEmbeddedModel(EmbeddedDocument):
    name = StringField(required=True)
