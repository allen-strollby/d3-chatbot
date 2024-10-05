from mongoengine import EmbeddedDocumentField, StringField, IntField, BooleanField


class TrainingEmbeddedModel(EmbeddedDocumentField):
    phone = StringField(required=True)
    training_batch_id = IntField(required=True)
    training_in_progress = BooleanField(required=True)
    training_tech_stack = StringField(required=True)
