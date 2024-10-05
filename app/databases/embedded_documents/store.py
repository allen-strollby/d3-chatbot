from mongoengine import EmbeddedDocumentField, ListField

from databases.embedded_documents.store_items import StoreItemsEmbeddedModel


class StoreEmbeddedModel(EmbeddedDocumentField):
    items = ListField(EmbeddedDocumentField(StoreItemsEmbeddedModel), required=True)
