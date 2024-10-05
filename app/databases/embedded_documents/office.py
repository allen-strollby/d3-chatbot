from mongoengine import (
    EmbeddedDocument,
    ListField,
    EmailField,
    EmbeddedDocumentField,
    ReferenceField,
)


from databases.embedded_documents.job_description import JobDescriptionEmbeddedModel


class AccountEmbeddedModel(EmbeddedDocument):
    email = EmailField(required=True)
    job_openings = ListField(
        EmbeddedDocumentField(JobDescriptionEmbeddedModel), default=[]
    )
    hsc = ReferenceField("EntityModel")
