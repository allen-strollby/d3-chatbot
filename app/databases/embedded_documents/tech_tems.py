from mongoengine import EmbeddedDocument, StringField, BooleanField


class TechCategoryEmbeddedModel(EmbeddedDocument):
    name = StringField(required=True, description="Software/Hardware etc")
    available = BooleanField(required=True)
    phone = StringField(required=True)
