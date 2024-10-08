from databases.enums.division_type import DivisionTypeEnum
from .cafeteria import get_cafeteria_food
from .conference_room import get_available_conference_room
from .job_vacancy import get_job_vacancies
from .amenities import get_amenities

controller_map = {
    DivisionTypeEnum.CAFETERIA: get_cafeteria_food,
    DivisionTypeEnum.CONFERENCE: get_available_conference_room,
    DivisionTypeEnum.ACCOUNT: get_job_vacancies,
    DivisionTypeEnum.AMENITY: get_amenities,
}
