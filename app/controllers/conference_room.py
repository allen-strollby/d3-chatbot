from databases.documents.divisions import DivisionModel
from databases.enums.division_type import DivisionTypeEnum
from databases.enums.occupancy_status import OccupancyStatusEnum


def get_available_conference_room(**kwargs) -> dict | None:
    """

    Args:
        **kwargs:

    Returns:
           Json of the format
          {
            "type": "CONFERENCE",
            "room_id": "01_conf_01",
            "is_authorized": true,
            "is_available": true,
            "next_available": "2025 December 90"
        }
    """

    num = kwargs.get("number_of_people")
    floor_number = kwargs.get("floor_number")

    queryset = DivisionModel.objects(type=DivisionTypeEnum.CONFERENCE)

    if num:
        queryset = queryset.filter(capacity__gte=num)

    if floor_number:
        queryset = queryset.filter(floor_number=floor_number)

    for room in queryset:
        if room.occupancy_status == OccupancyStatusEnum.FREE:
            return {
                "type": "CONFERENCE",
                "room_id": room.room_id,
                "is_authorized": True,
                "is_available": True,
                "capacity": room.capacity,
                # "next_available": "2025 December 90"
            }

    if queryset:
        return {
            "type": "CONFERENCE",
            "room_id": queryset[0].room_id,
            "is_authorized": True,
            "is_available": True,
            "capacity": queryset[0].capacity,
            # "next_available": "2025 December 90"
        }

    return None
