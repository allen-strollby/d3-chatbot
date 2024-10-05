from mongoengine import EmbeddedDocumentField, StringField


class HrEmbeddedModel(EmbeddedDocumentField):
    phone = StringField(required=True)
