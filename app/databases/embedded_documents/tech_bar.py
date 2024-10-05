from mongoengine import EmbeddedDocumentField, ListField

from databases.embedded_documents.tech_tems import TechCategoryEmbeddedModel


class TechBarEmbeddedModel(EmbeddedDocumentField):
    category = ListField(
        EmbeddedDocumentField(TechCategoryEmbeddedModel), required=True
    )
