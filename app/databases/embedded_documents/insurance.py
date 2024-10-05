from mongoengine import EmbeddedDocumentField, StringField


class InsuranceEmbeddedModel(EmbeddedDocumentField):
    phone = StringField(required=True)
    working_days = StringField(required=True)
