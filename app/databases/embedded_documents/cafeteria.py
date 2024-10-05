from mongoengine import EmbeddedDocumentField, ListField, EmbeddedDocument

from databases.embedded_documents.food_menu import FoodMenuEmbeddedModel


class CafeteriaEmbeddedModel(EmbeddedDocument):
    menu = ListField(EmbeddedDocumentField(FoodMenuEmbeddedModel), required=True)
