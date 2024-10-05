from mongoengine import EmbeddedDocument, StringField, ListField, IntField


class JobDescriptionEmbeddedModel(EmbeddedDocument):
    job_id = StringField(required=True)
    role = StringField(required=True)
    requirements = ListField(StringField(required=True), required=True)
    yoe = IntField(required=True)
    count = IntField(required=True)
