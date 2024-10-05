from mongoengine import EmbeddedDocument, StringField, EnumField, ListField

from databases.enums import HealthTypeEnum


class HealthItemsEmbeddedModel(EmbeddedDocument):
    phone = StringField(required=True)
    type = EnumField(HealthTypeEnum, required=True)
    available_days = ListField(StringField(required=True))
