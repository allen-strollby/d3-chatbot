from mongoengine import EmbeddedDocument, StringField, EmailField


class BankDetailsEmbeddedModel(EmbeddedDocument):
    email = EmailField(required=True)
    phone = StringField(required=True)
