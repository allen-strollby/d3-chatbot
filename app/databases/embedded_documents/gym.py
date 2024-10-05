from mongoengine import EmbeddedDocumentField, StringField, BooleanField


class GymEmbeddedModel(EmbeddedDocumentField):
    phone = StringField(required=True)
    maintenance_status = BooleanField(required=True)
    fee_details = StringField(required=True)
