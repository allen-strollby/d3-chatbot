from mongoengine import (
    EmbeddedDocument,
    StringField,
    BooleanField,
    FloatField,
    IntField,
)


class FoodMenuEmbeddedModel(EmbeddedDocument):
    name = StringField(required=True)
    available = BooleanField(required=True)
    price = FloatField(required=True)
    available_number = IntField(required=False)
