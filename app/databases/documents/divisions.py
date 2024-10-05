from mongoengine import (
    Document,
    ReferenceField,
    IntField,
    StringField,
    EnumField,
    GenericEmbeddedDocumentField,
    BooleanField,
)
from app.databases.documents.company import CompanyModel
from databases.enums import OccupancyStatusEnum, DivisionTypeEnum


class DivisionModel(Document):
    meta = {
        "collection": "divisions",
        "indexes": [
            {
                "fields": (
                    "type",
                    "occupancy_status",
                ),
                "name": "index_type",
            },
            {
                "fields": (
                    "type",
                    "floor_number",
                    "company",
                ),
                "name": "tfc_index",
            },
        ],
    }
    company = ReferenceField(CompanyModel, required=True)
    floor_number = IntField(required=True)
    name = StringField(required=True)
    occupancy_status = EnumField(OccupancyStatusEnum, required=True)
    capacity = IntField(required=True)
    type = EnumField(DivisionTypeEnum, required=True)
    divisions = GenericEmbeddedDocumentField(required=True)
    is_open = BooleanField(required=True)
