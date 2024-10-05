from mongoengine import EmbeddedDocument, StringField, ListField


class InsuranceEmbeddedModel(EmbeddedDocument):
    phone = StringField(required=True)
    working_days = ListField(StringField(required=True))
