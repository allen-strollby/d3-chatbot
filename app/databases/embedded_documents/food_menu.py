from mongoengine import EmbeddedDocument, StringField, BooleanField, IntField


class FoodMenuEmbeddedModel(EmbeddedDocument):
    name = StringField(required=True)
    available = BooleanField(required=True)
    count = IntField(required=True)
