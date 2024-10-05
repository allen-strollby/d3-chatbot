from mongoengine import DynamicEmbeddedDocument, StringField, ListField


class ConferenceEmbeddedModel(DynamicEmbeddedDocument):
    authorized_entities = ListField(StringField())
