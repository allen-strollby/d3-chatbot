from databases.documents.divisions import DivisionModel
from databases.enums.amenity_type import AmenityTypeEnum
from databases.enums.division_type import DivisionTypeEnum
from databases.enums.occupancy_status import OccupancyStatusEnum


def get_amenities(**kwargs) -> DivisionModel | None:
    amenity_type = kwargs.get("type")

    if amenity_type.lower() not in AmenityTypeEnum:
        return None

    queryset = DivisionModel.objects(
        type=DivisionTypeEnum.AMENITY,
        divisions__amenity_type=AmenityTypeEnum(amenity_type),
        occupancy_status=OccupancyStatusEnum.FREE,
    )

    if queryset:
        model = queryset[0]
        return {
            "type": "AMENITY",
            "room_id": model.room_id
        }

    return None
