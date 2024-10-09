from databases.enums.division_type import DivisionTypeEnum
from .amenities import get_amenities
from .bank import get_bank
from .cafeteria import get_cafeteria_food
from .conference_room import get_available_conference_room
from .health import return_health_query
from .insurance import return_insurance_query
from .job_vacancy import get_job_vacancies
from .atm import get_atm
from .store import get_store
from .tech_bar import get_tech_bar
from .location import get_location_details
from .gym import get_gym_details
from .security import get_security
from .recreation import get_recreation

controller_map = {
    DivisionTypeEnum.CONFERENCE: get_available_conference_room,
    DivisionTypeEnum.ACCOUNT: get_job_vacancies,
    DivisionTypeEnum.HEALTH: return_health_query,
    DivisionTypeEnum.CAFETERIA: get_cafeteria_food,
    DivisionTypeEnum.AMENITY: get_amenities,
    DivisionTypeEnum.BANK: get_bank,
    # DivisionTypeEnum.ATM: get_atm,
    DivisionTypeEnum.STORE: get_store,
    DivisionTypeEnum.TECH_BAR: get_tech_bar,
    DivisionTypeEnum.INSURANCE: return_insurance_query,
    DivisionTypeEnum.PLACE: get_location_details,
    DivisionTypeEnum.GYM: get_gym_details,
    DivisionTypeEnum.SECURITY: get_security,
    DivisionTypeEnum.RECREATION: get_recreation,
}
