from databases.enums.division_type import DivisionTypeEnum
from .amenities import get_amenities
from .bank import get_bank
from .cafeteria import get_cafeteria_food
from .conference_room import get_available_conference_room
from .job_vacancy import get_job_vacancies

controller_map = {
    DivisionTypeEnum.CAFETERIA: get_cafeteria_food,
    DivisionTypeEnum.CONFERENCE: get_available_conference_room,
    DivisionTypeEnum.ACCOUNT: get_job_vacancies,
    DivisionTypeEnum.AMENITY: get_amenities,
    DivisionTypeEnum.BANK: get_bank,
}
