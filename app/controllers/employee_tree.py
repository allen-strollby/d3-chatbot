from databases.documents.people import EntityModel
from databases.enums import EntityTypeEnum


def return_employee_tree(**kwargs):
    user = kwargs.get("user")
    entity_type = kwargs.get("entity_type")
    employee = EntityModel.objects(employee_id=user).get()
    room_id = None
    match entity_type.upper():
        case "CEO":
            room_id = employee.ceo.office.room_id
        case "HR":
            room_id = employee.hr.office.room_id
        case "MANAGER":
            room_id = employee.manager.office.room_id

    return {
        "type": "PEOPLE",
        "name": employee.name,
        "status": employee.entity_status.value,
        "room_id": room_id if room_id is not None else employee.office.room_id,
        "entity": EntityTypeEnum(entity_type.upper()),
    }
