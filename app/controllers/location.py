from databases.documents.divisions import DivisionModel
from databases.enums.division_type import DivisionTypeEnum


def get_location_details(**kwargs):
    division_type = DivisionTypeEnum(kwargs.get("name"))
    result = DivisionModel.objects(type=division_type).first()
    if result:
        return {
            "type": division_type.value,
            "room_id": result.room_id,
            # "phone_number": result.divisions.phone,
            "is_authorized": True,
            "is_available": True,
        }
