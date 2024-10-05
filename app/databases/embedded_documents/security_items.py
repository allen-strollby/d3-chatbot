from mongoengine import EmbeddedDocument, StringField, IntField


class LostItemsEmbeddedModel(EmbeddedDocument):
    name = StringField(required=True)
    count = IntField(required=True)
