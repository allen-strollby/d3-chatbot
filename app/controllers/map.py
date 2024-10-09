from databases.enums.division_type import DivisionTypeEnum
from .cafeteria import get_cafeteria_food
from .conference_room import get_available_conference_room
from .health import return_health_query
from .job_vacancy import get_job_vacancies

controller_map = {
    DivisionTypeEnum.CAFETERIA: get_cafeteria_food,
    DivisionTypeEnum.CONFERENCE: get_available_conference_room,
    DivisionTypeEnum.ACCOUNT: get_job_vacancies,
    DivisionTypeEnum.HEALTH: return_health_query,
}
