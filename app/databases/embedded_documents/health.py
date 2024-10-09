from mongoengine import EmbeddedDocumentField, EmbeddedDocument

from databases.embedded_documents.health_items import HealthItemsEmbeddedModel


class HealthEmbeddedModel(EmbeddedDocument):
    health_category = EmbeddedDocumentField(HealthItemsEmbeddedModel, required=True)
