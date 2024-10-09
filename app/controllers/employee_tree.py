from databases.documents.people import EntityModel


def return_employee_tree(**kwargs):
    user = kwargs.get("user")
    type = kwargs.get("type")
    employee = EntityModel.objects(employee_id=user).get()
    return {
        "type": "PEOPLE",
        "name": employee.name,
        "status": employee.entity_status.value,
        "room_id": employee.office.room_id,
        "entity": type,
    }
