from databases.documents.divisions import DivisionModel
from databases.enums.amenity_type import AmenityTypeEnum
from databases.enums.division_type import DivisionTypeEnum
from databases.enums.occupancy_status import OccupancyStatusEnum


def get_amenities(**kwargs) -> dict | None:
    amenity_type = kwargs.get("type")
    floor_number = kwargs.get("floor-number")

    if not amenity_type:
        return None

    if amenity_type.lower() not in AmenityTypeEnum:
        return None

    queryset = DivisionModel.objects(
        type=DivisionTypeEnum.AMENITY,
        divisions__amenity_type=AmenityTypeEnum(amenity_type),
        occupancy_status=OccupancyStatusEnum.FREE,
    )
    if floor_number is not None:
        queryset = queryset.filter(floor_number=floor_number)

    if queryset:
        model = queryset[0]
        return {"type": "AMENITY", "room_id": model.room_id}

    return None
