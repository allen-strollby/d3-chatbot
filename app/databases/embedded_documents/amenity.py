from mongoengine import EmbeddedDocument, EnumField, BooleanField

from databases.enums import AmenityTypeEnum


class AmenityEmbeddedModel(EmbeddedDocument):
    maintenance_status = BooleanField(required=True, default=False)
    amenity_type = EnumField(AmenityTypeEnum, required=True)
