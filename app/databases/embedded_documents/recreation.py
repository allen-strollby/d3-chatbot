from mongoengine import StringField, ListField, EmbeddedDocument


class RecreationEmbeddedModel(EmbeddedDocument):
    games = ListField(StringField())
