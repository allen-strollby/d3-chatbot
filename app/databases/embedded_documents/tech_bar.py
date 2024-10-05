from mongoengine import EmbeddedDocumentField, ListField, EmbeddedDocument

from databases.embedded_documents.tech_tems import TechCategoryEmbeddedModel


class TechBarEmbeddedModel(EmbeddedDocument):
    category = ListField(
        EmbeddedDocumentField(TechCategoryEmbeddedModel), required=True
    )
