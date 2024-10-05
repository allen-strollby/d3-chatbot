from mongoengine import EmbeddedDocumentField, ListField, StringField, EmbeddedDocument

from databases.embedded_documents.security_items import LostItemsEmbeddedModel


class SecurityEmbeddedModel(EmbeddedDocument):
    phone = StringField(required=True)
    category = ListField(EmbeddedDocumentField(LostItemsEmbeddedModel), required=True)
