from mongoengine import EmbeddedDocumentField, StringField, ListField


class ConferenceEmbeddedModel(EmbeddedDocumentField):
    name = StringField(required=True)
    authorized_entities = ListField(StringField())
