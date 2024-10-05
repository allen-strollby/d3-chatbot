from mongoengine import EmbeddedDocumentField, ListField

from databases.embedded_documents.store_items import (
    StoreItemsEmbeddedModel,
    EmbeddedDocument,
)


class StoreEmbeddedModel(EmbeddedDocument):
    items = ListField(EmbeddedDocumentField(StoreItemsEmbeddedModel), required=True)
