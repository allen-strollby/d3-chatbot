from mongoengine import (
    EmbeddedDocument,
    StringField,
    BooleanField,
    FloatField,
)


class FoodMenuEmbeddedModel(EmbeddedDocument):
    name = StringField(required=True)
    available = BooleanField(required=True)
    price = FloatField(required=True)
