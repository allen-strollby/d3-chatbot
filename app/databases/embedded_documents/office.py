from mongoengine import EmbeddedDocument, ListField, EmailField, EmbeddedDocumentField

from databases.embedded_documents.job_description import JobDescriptionEmbeddedModel


class OfficeEmbeddedModel(EmbeddedDocument):
    email = EmailField(required=True)
    job_openings = ListField(
        EmbeddedDocumentField(JobDescriptionEmbeddedModel), default=[]
    )
