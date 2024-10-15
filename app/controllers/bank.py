from databases.documents.divisions import DivisionModel
from databases.documents.people import EntityModel
from databases.enums import BankTypeEnum
from databases.enums.division_type import DivisionTypeEnum


def get_bank(**kwargs) -> dict | None:
    bank_type = kwargs.get("type")
    user = kwargs.get("user")


    def generic_bank():
        model = DivisionModel.objects(
            type=DivisionTypeEnum.BANK,
            name="Bank Area",
        ).get()
        return {"type": "BANK", "room_id": model.room_id}

    if not bank_type:
        queryset = EntityModel.objects(
            employee_id=user
        ).get()
        return {"type": "BANK", "room_id": queryset.bank.room_id}

    if len(bank_type.split()) >= 2 and bank_type.split()[-1].lower() == "bank":
        bank_type = bank_type.split()[0]

    if bank_type.upper() not in BankTypeEnum:
        return generic_bank()
    else:
        queryset = DivisionModel.objects(
            type=DivisionTypeEnum.BANK,
            name=BankTypeEnum(bank_type).value,
        )

    if queryset:
        model = queryset[0]
        return {"type": "BANK", "room_id": model.room_id}

    return None
