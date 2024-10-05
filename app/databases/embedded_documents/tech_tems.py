from mongoengine import EmbeddedDocument, StringField, BooleanField


class TechCategoryEmbeddedModel(EmbeddedDocument):
    repair_type = StringField(required=True, description="Software/Hardware etc")
    available = BooleanField(required=True, default=True)
    phone = StringField(required=True)
