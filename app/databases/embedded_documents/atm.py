from mongoengine import EmbeddedDocumentField, BooleanField


class AtmEmbeddedModel(EmbeddedDocumentField):
    maintenance_status = BooleanField(required=True, default=False)
