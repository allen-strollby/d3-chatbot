from databases.documents.divisions import DivisionModel
from databases.enums import HealthTypeEnum, DivisionTypeEnum
from mongoengine.queryset.visitor import Q


def return_insurance_query(
    type: str | None = None,
    booking: bool | None = False,
    availability: bool | None = False,
):
    med_type = (
        HealthTypeEnum.DENTAL if type == "dentist" else HealthTypeEnum.HEALTH_CLINIC
    )
    query_set = DivisionModel.objects(type=DivisionTypeEnum.HEALTH).get()
    if query_set:
        print(query_set.divisions.health_category)
