from mongoengine import Document, StringField, EnumField, IntField
from poli_enum.country import Country


class CompanyModel(Document):
    meta = {"collection": "companies"}
    country = EnumField(Country, required=True)
    state = StringField(required=True)
    district = StringField(required=True)
    floor_count = IntField(required=True)
