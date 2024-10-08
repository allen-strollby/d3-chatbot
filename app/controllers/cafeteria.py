from databases.documents.divisions import DivisionModel
from databases.embedded_documents.food_menu import FoodMenuEmbeddedModel
from databases.enums.division_type import DivisionTypeEnum
from databases.enums.occupancy_status import OccupancyStatusEnum


def get_cafeteria_food(**kwargs) -> FoodMenuEmbeddedModel:
    food_type = kwargs.get("food_type")

    queryset = DivisionModel.objects(
        type=DivisionTypeEnum.CAFETERIA,
        occupancy_status=OccupancyStatusEnum.FREE,
    )

    if food_type:
        cafeterias: list[DivisionModel] = list(queryset)

        for cafeteria in cafeterias:
            cf = cafeteria.divisions
            menu: list[FoodMenuEmbeddedModel] = cf.menu
            for item in menu:
                if item.name == food_type and item.available:
                    return item

    if queryset:
        ca: DivisionModel = queryset[0]
        return {
            "type": "FOOD_COURT",
            "room_id": ca.room_id,
            "options": [
                {"title": item.name, "number": item.available_number}
                for item in ca.divisions.menu
                if item.available
            ],
        }

    return None
