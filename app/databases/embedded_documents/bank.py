from mongoengine import EmbeddedDocumentField, EnumField

from databases.embedded_documents.bank_details import BankDetailsEmbeddedModel
from databases.enums import BankTypeEnum


class BankEmbeddedModel(EmbeddedDocumentField):
    bank_type = EnumField(BankTypeEnum, required=True)
    bank = EmbeddedDocumentField(
        BankDetailsEmbeddedModel, required=True
    )
