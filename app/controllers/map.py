from databases.enums.division_type import DivisionTypeEnum
from .cafeteria import get_cafeteria_food
from .conference_room import get_available_conference_room
from .location import get_location_details

controller_map = {DivisionTypeEnum.CAFETERIA: get_cafeteria_food,
                  DivisionTypeEnum.CONFERENCE: get_available_conference_room,
                  DivisionTypeEnum.PLACE:get_location_details
                  }
