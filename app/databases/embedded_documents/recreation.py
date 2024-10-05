from mongoengine import EmbeddedDocumentField, ListField

from databases.embedded_documents.game_list import GamesEmbeddedModel


class RecreationEmbeddedModel(EmbeddedDocumentField):
    games = ListField(EmbeddedDocumentField(GamesEmbeddedModel), required=True)
