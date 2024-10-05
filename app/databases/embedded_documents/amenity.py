from mongoengine import EmbeddedDocumentField, EnumField, BooleanField

from databases.enums import AmenityTypeEnum


class AmenityEmbeddedModel(EmbeddedDocumentField):
    maintenance_status = BooleanField(required=True, default=False)
    amenity_type = EnumField(AmenityTypeEnum, required=True)
