from datetime import datetime, timedelta

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
    if num == 0:
        return None

    floor_number = kwargs.get("floor_number")
    user = kwargs.get("user")
    auth_user = False
    availability = False

    queryset = DivisionModel.objects(type=DivisionTypeEnum.CONFERENCE)

    if floor_number:
        queryset = queryset.filter(floor_number=floor_number)

    if num:
        queryset = queryset.filter(capacity__gte=num)
        if queryset is None:
            return None



    for room in queryset:
        if user in room.divisions.authorized_entities:
            auth_user = True
        if room.occupancy_status == OccupancyStatusEnum.FREE:
            availability = True
        if (
            room.occupancy_status == OccupancyStatusEnum.FREE
            and user in room.divisions.authorized_entities
        ):
            return {
                "type": "CONFERENCE",
                "room_id": room.room_id,
                "is_authorized": True,
                "is_available": True,
                "capacity": room.capacity,
            }
    available_time = datetime.now() + timedelta(hours=2)
    if queryset:
        return {
            "type": "CONFERENCE",
            "room_id": queryset[0].room_id,
            "is_authorized": auth_user,
            "is_available": availability,
            "capacity": queryset[0].capacity,
            "next_available": available_time,
        }

    return None
