from databases.documents.divisions import DivisionModel
from databases.enums import DivisionTypeEnum


def get_gym_details(**kwargs) -> dict | None:
    contact_details = kwargs.get("contact_details")
    maintenance_status = kwargs.get("maintenance_status")
    fee_structure = kwargs.get("fee_structure")
    application_process = kwargs.get("application_process")
    documents_needed = kwargs.get("documents_needed")

    # Assuming you have a GymModel for your gym data
    queryset = DivisionModel.objects(
        type=DivisionTypeEnum.GYM,
    )

    gym_info = {"type": "GYM"}

    if contact_details:
        gym_info["contact_details"] = queryset[0].divisions.phone if queryset else None

    if maintenance_status:
        gym_info["maintenance_status"] = (
            queryset[0].divisions.maintenance_status if queryset else None
        )

    if fee_structure:
        gym_info["fee_structure"] = (
            queryset[0].divisions.fee_details if queryset else None
        )

    if application_process:
        gym_info["application_process"] = (
            f"Either you can apply through our HRMS website or {queryset[0].divisions.phone}"
            if queryset
            else None
        )

    if documents_needed:
        gym_info["documents_needed"] = "Fitness Certificate"

    if gym_info:
        return gym_info

    return None
