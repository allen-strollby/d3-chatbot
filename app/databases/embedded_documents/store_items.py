from mongoengine import EmbeddedDocument, StringField, FloatField


class StoreItemsEmbeddedModel(EmbeddedDocument):
    name = StringField(required=True)
    price = FloatField(required=True)
