from mongoengine import EmbeddedDocument, StringField, EmailField


class BankDetailsEmbeddedModel(EmbeddedDocument):
    name = StringField(required=True)
    email = EmailField(required=True)
    phone = StringField(required=True)
