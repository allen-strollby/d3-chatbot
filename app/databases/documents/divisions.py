from mongoengine import (
    Document,
    ReferenceField,
    IntField,
    StringField,
    EnumField,
    GenericEmbeddedDocumentField,
    BooleanField,
)


from databases.documents.company import CompanyModel
from databases.enums import OccupancyStatusEnum, DivisionTypeEnum
from databases.embedded_documents import (
    ConferenceEmbeddedModel,
    AccountEmbeddedModel,
    CafeteriaEmbeddedModel,
    AmenityEmbeddedModel,
    BankDetailsEmbeddedModel,
    AtmEmbeddedModel,
    TechBarEmbeddedModel,
    StoreEmbeddedModel,
    SecurityEmbeddedModel,
    ReceptionEmbeddedModel,
    MainHallEmbeddedModel,
    TrainingEmbeddedModel,
    RecreationEmbeddedModel,
    ServerEmbeddedModel,
    GymEmbeddedModel,
    InsuranceEmbeddedModel,
    HrEmbeddedModel,
    HealthEmbeddedModel,
    FoundersHallEmbeddedModel,
)


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
    capacity = IntField()
    type = EnumField(DivisionTypeEnum, required=True)
    room_id = StringField()
    divisions = GenericEmbeddedDocumentField(
        choices=[
            ConferenceEmbeddedModel,
            AccountEmbeddedModel,
            CafeteriaEmbeddedModel,
            AmenityEmbeddedModel,
            BankDetailsEmbeddedModel,
            AtmEmbeddedModel,
            StoreEmbeddedModel,
            TechBarEmbeddedModel,
            SecurityEmbeddedModel,
            ReceptionEmbeddedModel,
            MainHallEmbeddedModel,
            TrainingEmbeddedModel,
            RecreationEmbeddedModel,
            ServerEmbeddedModel,
            GymEmbeddedModel,
            InsuranceEmbeddedModel,
            HrEmbeddedModel,  # todo: who is my hr
            HealthEmbeddedModel,
            FoundersHallEmbeddedModel,
        ],
        required=True,
    )
    is_open = BooleanField(required=True)
