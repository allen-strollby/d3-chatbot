from mongoengine import EmbeddedDocument, FloatField, StringField, BooleanField


class GymEmbeddedModel(EmbeddedDocument):
    phone = StringField(required=True)
    maintenance_status = BooleanField(required=True, default=False)
    fee_details = FloatField(required=True)

