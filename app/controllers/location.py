from databases.documents.divisions import DivisionModel


def get_location_details(**kwargs):
    name = kwargs.get("name")
    divisions: list[DivisionModel] = DivisionModel.objects.all()
    if name == "HR":
        return {
                "type": "HR",
                "room_id": "03_hr_01",
                # "phone_number": result.divisions.phone,
                "is_authorized": True,
                "is_available": True,
            }

    for room in divisions:
        if str(room.name).lower() == name.lower():
            return {
                "type": name,
                "room_id": room.room_id,
                # "phone_number": result.divisions.phone,
                "is_authorized": True,
                "is_available": True,
            }

    return None
