from mongoengine import EmbeddedDocument, BooleanField


class AtmEmbeddedModel(EmbeddedDocument):
    maintenance_status = BooleanField(required=True, default=False)
