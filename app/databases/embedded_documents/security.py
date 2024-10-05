from mongoengine import EmbeddedDocumentField, ListField, StringField

from databases.embedded_documents.security_items import LostItemsEmbeddedModel


class SecurityEmbeddedModel(EmbeddedDocumentField):
    phone = StringField(required=True)
    category = ListField(EmbeddedDocumentField(LostItemsEmbeddedModel), required=True)
