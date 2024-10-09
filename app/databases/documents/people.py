from mongoengine import Document, ReferenceField, StringField, EnumField

from databases.documents.company import CompanyModel
from databases.documents.divisions import DivisionModel
from databases.enums import EntityTypeEnum, EntityStatusEnum


class EntityModel(Document):
    meta = {"collection": "entities"}
    company = ReferenceField(CompanyModel, required=True)
    office = ReferenceField(DivisionModel, required=True)
    manager = ReferenceField("EntityModel")
    name = StringField(required=True)
    employee_id = StringField()
    entity_type = EnumField(EntityTypeEnum, required=True)
    entity_status = EnumField(EntityStatusEnum, required=True)
    bank = ReferenceField(DivisionModel)
    hr = ReferenceField("EntityModel")
