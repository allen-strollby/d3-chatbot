from mongoengine import (
    EmbeddedDocumentField,
    StringField,
    ListField,
    IntField,
    EmailField,
)

from databases.embedded_documents.job_description import JobDescriptionEmbeddedModel


class OfficeEmbeddedModel(EmbeddedDocumentField):
    account_name = StringField(required=True)
    employee_count = IntField(required=True)
    email = EmailField(required=True)
    job_openings = ListField(EmbeddedDocumentField(JobDescriptionEmbeddedModel), default=[])
