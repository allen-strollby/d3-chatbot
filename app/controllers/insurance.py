from datetime import datetime, timedelta

from databases.documents.divisions import DivisionModel
from databases.enums import DivisionTypeEnum

DAY_NAME_TO_NUM = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}


def get_nearest_day_of_week(target_day_names):
    today = datetime.now()
    today_day_num = today.weekday()

    nearest_day = None
    min_diff = float("inf")

    for day_name in target_day_names:
        target_day_num = DAY_NAME_TO_NUM[day_name]
        day_diff = (target_day_num - today_day_num) % 7
        future_day = today + timedelta(days=day_diff)

        if day_diff == 0:
            return today.date()

        if day_diff < min_diff:
            min_diff = day_diff
            nearest_day = future_day

    return nearest_day.date()


def return_insurance_query(**kwargs):  # noqa
    query_set = DivisionModel.objects(type=DivisionTypeEnum.INSURANCE).get()
    response_json = {
        "type": query_set.type.value,
        "room_id": query_set.room_id,
        "phone": query_set.divisions.phone,
    }
    available = False
    if query_set:
        nearest_day = get_nearest_day_of_week(query_set.divisions.working_days)
        if nearest_day == datetime.now().date():
            available = True
        else:
            next_available = nearest_day
        if available:
            response_json.update({"available": available})
        else:
            response_json.update({"next_available": next_available})

        return response_json
