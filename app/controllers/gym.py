from databases.documents.divisions import DivisionModel
from databases.enums import DivisionTypeEnum


def get_gym_details(**kwargs) -> dict:
    contact_details = kwargs.get("contact_details")
    maintenance_status = kwargs.get("maintenance_status")
    fee_structure = kwargs.get("fee_structure")
    application_process = kwargs.get("application_process")
    documents_needed = kwargs.get("documents_needed")

    # Assuming you have a GymModel for your gym data
    queryset = DivisionModel.objects(
        type=DivisionTypeEnum.GYM,
    )

    gym_info = {}

    if contact_details:
        gym_info["contact_details"] = queryset[0].division.phone if queryset else None

    if maintenance_status:
        gym_info["maintenance_status"] = queryset[0].maintenance if queryset else None

    if fee_structure:
        gym_info["fee_structure"] = queryset[0].fee_structure if queryset else None

    if application_process:
        gym_info["application_process"] = queryset[0].application_process if queryset else None

    if documents_needed:
        gym_info["documents_needed"] = queryset[0].documents_needed if queryset else None

    if gym_info:
        return gym_info

    return None
