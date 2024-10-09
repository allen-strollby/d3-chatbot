from databases.documents.divisions import DivisionModel
from databases.enums.division_type import DivisionTypeEnum
from databases.embedded_documents.security_items import LostItemsEmbeddedModel


def get_security(**kwargs) -> dict | None:
    user_item = kwargs.get("item")

    if not user_item:
        return {
            "type": DivisionTypeEnum.SECURITY,
            "room_id": "01_sc_01",
        }

    cabin: list[DivisionModel] = DivisionModel.objects(type=DivisionTypeEnum.SECURITY)
    for c in cabin:
        categories: list[LostItemsEmbeddedModel] = c.divisions.category  # type: ignore
        for item in categories:
            if str(item.name).lower() == str(user_item).lower():
                return {
                    "type": DivisionTypeEnum.SECURITY,
                    "room_id": "01_sc_01",
                    "is_found": True,
                }

    return {"type": DivisionTypeEnum.SECURITY, "room_id": "01_sc_01", "is_found": False}
