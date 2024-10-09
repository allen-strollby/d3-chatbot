from databases.enums.division_type import DivisionTypeEnum


def get_recreation(**kwargs) -> dict | None:
    return {"type": DivisionTypeEnum.RECREATION, "room_id": "02_rc_01"}
