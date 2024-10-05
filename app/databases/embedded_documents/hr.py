from mongoengine import EmbeddedDocument, StringField


class HrEmbeddedModel(EmbeddedDocument):
    phone = StringField(required=True)
