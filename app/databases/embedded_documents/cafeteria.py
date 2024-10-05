from mongoengine import EmbeddedDocumentField, ListField

from databases.embedded_documents.food_menu import FoodMenuEmbeddedModel


class CafeteriaEmbeddedModel(EmbeddedDocumentField):
    menu = ListField(EmbeddedDocumentField(FoodMenuEmbeddedModel), required=True)
