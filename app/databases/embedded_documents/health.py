from mongoengine import EmbeddedDocumentField

from databases.embedded_documents.health_items import HealthItemsEmbeddedModel


class HealthEmbeddedModel(EmbeddedDocumentField):
    health_category = EmbeddedDocumentField(HealthItemsEmbeddedModel, required=True)
