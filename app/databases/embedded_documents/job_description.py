from mongoengine import EmbeddedDocument, StringField, ListField, IntField, EnumField

from databases.enums import JobDomainEnum


class JobDescriptionEmbeddedModel(EmbeddedDocument):
    job_id = StringField(required=True)
    job_domain = EnumField(JobDomainEnum, required=True)
    role = StringField(required=True)
    requirements = ListField(StringField(required=True), required=True)
    yoe = IntField(required=True)
    count = IntField(required=True)
