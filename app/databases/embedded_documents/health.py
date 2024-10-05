from mongoengine import EmbeddedDocumentField, EmbeddedDocument, ListField

from databases.embedded_documents.health_items import HealthItemsEmbeddedModel


class HealthEmbeddedModel(EmbeddedDocument):
    health_category = ListField(
        EmbeddedDocumentField(HealthItemsEmbeddedModel, required=True)
    )
