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
    if num:
        queryset = DivisionModel.objects(
            type=DivisionTypeEnum.CONFERENCE,
            occupancy_status=OccupancyStatusEnum.FREE,
            capacity__gte=num,
        )
    else:
        queryset = DivisionModel.objects(
            type=DivisionTypeEnum.CONFERENCE, occupancy_status=OccupancyStatusEnum.FREE
        )
    if queryset:
        model = queryset[0]
        return {
            "type": "CONFERENCE",
            "room_id": model.room_id,
            "is_authorized": True,
            "is_available": True,
            "capacity": model.capacity,
            # "next_available": "2025 December 90"
        }
