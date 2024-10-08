import string
import random

from datetime import datetime

from poli_enum.country import Country

from databases.documents.company import CompanyModel
from databases.documents.divisions import DivisionModel
from databases.documents.events import EventModel
from databases.documents.people import EntityModel
from databases.embedded_documents import (
    ConferenceEmbeddedModel,
    OfficeEmbeddedModel,
    CafeteriaEmbeddedModel,
    AmenityEmbeddedModel,
    BankDetailsEmbeddedModel,
    AtmEmbeddedModel,
    TechBarEmbeddedModel,
    StoreEmbeddedModel,
    SecurityEmbeddedModel,
    ReceptionEmbeddedModel,
    MainHallEmbeddedModel,
    TrainingEmbeddedModel,
    RecreationEmbeddedModel,
    ServerEmbeddedModel,
    GymEmbeddedModel,
    InsuranceEmbeddedModel,
    HrEmbeddedModel,
    HealthEmbeddedModel,
)
from databases.embedded_documents.food_menu import FoodMenuEmbeddedModel
from databases.embedded_documents.health_items import HealthItemsEmbeddedModel
from databases.embedded_documents.job_description import JobDescriptionEmbeddedModel
from databases.embedded_documents.security_items import LostItemsEmbeddedModel
from databases.embedded_documents.store_items import StoreItemsEmbeddedModel
from databases.embedded_documents.tech_tems import TechCategoryEmbeddedModel
from databases.enums import (
    OccupancyStatusEnum,
    DivisionTypeEnum,
    AmenityTypeEnum,
    HealthTypeEnum,
    EntityTypeEnum,
    EntityStatusEnum,
)


def random_string():
    return "".join([random.choice(string.ascii_lowercase) for _ in range(8)])


def populate_people(ust_ind, ust_us, ust_au):
    ceo_office = DivisionModel.objects(name="CEO").get()
    ceo_data = {
        "company": ust_us.pk,
        "office": ceo_office.pk,
        "name": "Alex Peirson",
        "entity_type": EntityTypeEnum.CEO,
        "entity_status": EntityStatusEnum.OOO,
    }
    EntityModel.objects.create(**ceo_data)
    hr_manager_office = DivisionModel.objects(name="HR-HEAD").get()
    ceo = EntityModel.objects(entity_type=EntityTypeEnum.CEO).get()
    hr_manager_data = {
        "company": ust_au.pk,
        "office": hr_manager_office.pk,
        "manager": ceo.pk,
        "name": "Robert Thomson",
        "entity_type": EntityTypeEnum.HR,
        "entity_status": EntityStatusEnum.LEAVE,
    }
    EntityModel.objects.create(**hr_manager_data)
    hr_manager = EntityModel.objects(company=ust_au.pk).get()
    hr_office = DivisionModel.objects(name="HR").get()
    hr_data = [
        {
            "company": ust_ind.pk,
            "office": hr_office.pk,
            "manager": hr_manager.pk,
            "name": "David Livingston",
            "entity_type": EntityTypeEnum.HR,
            "entity_status": EntityStatusEnum.MEETING,
        },
        {
            "company": ust_ind.pk,
            "office": hr_office.pk,
            "manager": hr_manager.pk,
            "name": "Ram Kumar",
            "entity_type": EntityTypeEnum.HR,
            "entity_status": EntityStatusEnum.OFFICE,
        },
    ]
    for hr in hr_data:
        EntityModel.objects.create(**hr)

    account_1 = DivisionModel.objects(name="Strollby").get()
    account_2 = DivisionModel.objects(name="Automation").get()
    account_3 = DivisionModel.objects(name="Mobility").get()

    hr_1 = EntityModel.objects(name="David Livingston").get()
    hr_2 = EntityModel.objects(name="Ram Kumar").get()

    associate_data = [
        {
            "company": ust_ind.pk,
            "office": account_1.pk,
            "manager": hr_1.pk,
            "name": "Anil K",
            "entity_type": EntityTypeEnum.ASSOCIATE,
            "entity_status": EntityStatusEnum.OFFICE,
        },
        {
            "company": ust_ind.pk,
            "office": account_2.pk,
            "manager": hr_2.pk,
            "name": "Robert Brown",
            "entity_type": EntityTypeEnum.ASSOCIATE,
            "entity_status": EntityStatusEnum.OFFICE,
        },
        {
            "company": ust_ind.pk,
            "office": account_3.pk,
            "manager": hr_1.pk,
            "name": "Shwetha S",
            "entity_type": EntityTypeEnum.ASSOCIATE,
            "entity_status": EntityStatusEnum.OFFICE,
        },
    ]
    for data in associate_data:
        EntityModel.objects.create(**data)


def populate_events(ust_ind):
    hr_office = DivisionModel.objects(name="HR").get()
    main_hall = DivisionModel.objects(type=DivisionTypeEnum.MAIN_HALL).get()

    event_data = [
        {
            "company": ust_ind.pk,
            "venue": hr_office.pk,
            "date": datetime(year=2024, month=10, day=11),
            "name": "SPARK",
            "description": "Quiz Competition (1 pm - 2pm)",
            "event_link": "https://www.w3.org/Provider/Style/dummy.html",
        },
        {
            "company": ust_ind.pk,
            "venue": hr_office.pk,
            "date": datetime(year=2024, month=10, day=12),
            "name": "CHESS MANIA",
            "description": "Chess Competition (4 pm - 6pm)",
            "event_link": "https://www.w3.org/Provider/Style/dummy.html",
        },
        {
            "company": ust_ind.pk,
            "venue": main_hall.pk,
            "date": datetime(year=2024, month=10, day=8),
            "name": "Trailblazer",
            "description": "",
            "event_link": "https://www.w3.org/Provider/Style/dummy.html",
        },
    ]
    for data in event_data:
        EventModel.objects.create(**data)


def populate_division(ust_ind, ust_au, ust_us):
    populate_conference(ust_ind)
    populate_office(ust_ind, ust_us)
    populate_cafeteria(ust_ind)
    populate_amenity(ust_ind)
    populate_bank(ust_ind)
    populate_atm(ust_ind)
    populate_tech_bar(ust_ind)
    populate_store(ust_ind)
    populate_security(ust_ind)
    populate_reception(ust_ind)
    populate_main_hall(ust_ind)
    populate_training_room(ust_ind)
    populate_recreation(ust_ind)
    populate_server(ust_ind)
    populate_gym(ust_ind)
    populate_insurance(ust_ind)
    populate_hr(ust_ind, ust_au)
    populate_health(ust_ind)


def populate_company():
    company_data = [
        {
            "country": Country.US,
            "name": "UST-US",
            "state": "Alabama",
            "district": "4th District",
            "floor_count": 15,
        },
        {
            "country": Country.AU,
            "name": "UST-AU",
            "state": "Victoria",
            "district": "6th District",
            "floor_count": 10,
        },
        {
            "country": Country.IN,
            "name": "UST-IN",
            "state": "Kerala",
            "district": "Trivandrum",
            "floor_count": 10,
        },
    ]
    for data in company_data:
        CompanyModel.objects.create(**data)


def populate_amenity(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 1,
            "name": "UCafe",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.AMENITY,
            "is_open": True,
            "divisions": AmenityEmbeddedModel(
                maintenance_status=False, amenity_type=AmenityTypeEnum.WATER
            ),
        },
        {
            "company": ust_ind.pk,
            "floor_number": 2,
            "name": "UCafe",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.AMENITY,
            "is_open": True,
            "divisions": AmenityEmbeddedModel(
                maintenance_status=False, amenity_type=AmenityTypeEnum.TOILET
            ),
        },
        {
            "company": ust_ind.pk,
            "floor_number": 3,
            "name": "UCafe",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.AMENITY,
            "is_open": True,
            "divisions": AmenityEmbeddedModel(
                maintenance_status=False, amenity_type=AmenityTypeEnum.VENDING_MACHINE
            ),
        },
    ]
    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_conference(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 1,
            "name": "CONF-16",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "capacity": 16,
            "type": DivisionTypeEnum.CONFERENCE,
            "is_open": True,
            "divisions": ConferenceEmbeddedModel(authorized_entities=[]),
        },
        {
            "company": ust_ind.pk,
            "floor_number": 5,
            "name": "CONF-8",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "capacity": 8,
            "type": DivisionTypeEnum.CONFERENCE,
            "is_open": True,
            "divisions": ConferenceEmbeddedModel(authorized_entities=[]),
        },
    ]
    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_office(ust_ind, ust_us):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 2,
            "name": "Strollby",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "capacity": 30,
            "type": DivisionTypeEnum.OFFICE,
            "is_open": True,
            "divisions": OfficeEmbeddedModel(
                email="strollby@gmail.com",
                job_openings=[
                    JobDescriptionEmbeddedModel(
                        job_id=random_string(),
                        role="Devops Engineer",
                        requirements=["AWS", "Terraform", "Kubernetes"],
                        yoe=1,
                        count=2,
                    )
                ],
            ),
        },
        {
            "company": ust_ind.pk,
            "floor_number": 3,
            "name": "Automation",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "capacity": 20,
            "type": DivisionTypeEnum.OFFICE,
            "is_open": True,
            "divisions": OfficeEmbeddedModel(
                email="automation@gmail.com",
                job_openings=[
                    JobDescriptionEmbeddedModel(
                        job_id=random_string(),
                        role="Software Developer",
                        requirements=["Python", "grpc", "Kafka"],
                        yoe=1,
                        count=2,
                    )
                ],
            ),
        },
        {
            "company": ust_ind.pk,
            "floor_number": 4,
            "name": "Mobility",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "capacity": 40,
            "type": DivisionTypeEnum.OFFICE,
            "is_open": True,
            "divisions": OfficeEmbeddedModel(email="mobility@gmail.com"),
        },
        {
            "company": ust_us.pk,
            "floor_number": 1,
            "name": "CEO",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "capacity": 30,
            "type": DivisionTypeEnum.OFFICE,
            "is_open": True,
            "divisions": OfficeEmbeddedModel(
                email="usceo@gmail.com",
            ),
        },
    ]
    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_cafeteria(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 1,
            "name": "UCafe",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.CAFETERIA,
            "is_open": True,
            "divisions": CafeteriaEmbeddedModel(
                menu=[
                    FoodMenuEmbeddedModel(name="Biriyani", available=True, price=120),
                    FoodMenuEmbeddedModel(name="Noodles", available=False, price=140),
                    FoodMenuEmbeddedModel(
                        name="Dosa",
                        available=True,
                        price=10,
                    ),
                ]
            ),
        }
    ]
    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_bank(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 1,
            "name": "ICICI Bank",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.BANK,
            "is_open": True,
            "divisions": BankDetailsEmbeddedModel(
                email="icici@gmail.com", phone="+9112345678"
            ),
        },
        {
            "company": ust_ind.pk,
            "floor_number": 1,
            "name": "Federal Bank",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.BANK,
            "is_open": True,
            "divisions": BankDetailsEmbeddedModel(
                email="federalbank@gmail.com", phone="+9112345678"
            ),
        },
    ]
    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_atm(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 2,
            "name": "HDFC ATM",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.ATM,
            "is_open": True,
            "divisions": AtmEmbeddedModel(),
        }
    ]
    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_store(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 1,
            "name": "UStore",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.STORE,
            "is_open": True,
            "divisions": StoreEmbeddedModel(
                items=[
                    StoreItemsEmbeddedModel(name="Sanitary Napkin", price=40),
                    StoreItemsEmbeddedModel(name="Notepad", price=30),
                ]
            ),
        }
    ]

    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_tech_bar(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 1,
            "name": "Tech Bar",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.TECH_BAR,
            "is_open": True,
            "divisions": TechBarEmbeddedModel(
                category=[
                    TechCategoryEmbeddedModel(
                        repair_type="Software", phone="+9112345678"
                    ),
                    TechCategoryEmbeddedModel(
                        repair_type="Hardware", phone="+9112345678"
                    ),
                ]
            ),
        }
    ]

    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_security(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 1,
            "name": "Security",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.SECURITY,
            "is_open": True,
            "divisions": SecurityEmbeddedModel(
                phone="+9112345678",
                category=[
                    LostItemsEmbeddedModel(name="ID Card", count=2),
                    LostItemsEmbeddedModel(name="Mobile", count=1),
                ],
            ),
        }
    ]

    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_reception(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 2,
            "name": "Reception",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.RECEPTION,
            "is_open": True,
            "divisions": ReceptionEmbeddedModel(
                phone="+9112345678",
            ),
        }
    ]

    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_main_hall(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 1,
            "name": "UST Square",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.MAIN_HALL,
            "is_open": True,
            "divisions": MainHallEmbeddedModel(
                phone="+9112345678",
            ),
        }
    ]

    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_training_room(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 2,
            "name": "TR-1",
            "occupancy_status": OccupancyStatusEnum.OCCUPIED,
            "capacity": 30,
            "type": DivisionTypeEnum.TRAINING,
            "is_open": True,
            "divisions": TrainingEmbeddedModel(
                phone="+9112345678",
                training_batch_id=12345,
                training_in_progress=True,
                training_tech_stack="Python",
            ),
        },
        {
            "company": ust_ind.pk,
            "floor_number": 4,
            "name": "TR-2",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "capacity": 20,
            "type": DivisionTypeEnum.TRAINING,
            "is_open": True,
            "divisions": TrainingEmbeddedModel(
                phone="+9112345678",
                training_batch_id=67896,
                training_in_progress=False,
                training_tech_stack="Java",
            ),
        },
    ]
    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_recreation(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 2,
            "name": "Recreation",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.RECREATION,
            "is_open": True,
            "divisions": RecreationEmbeddedModel(
                games=["Fusball", "Table Tennis", "Pool"]
            ),
        }
    ]

    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_server(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 2,
            "name": "Micro Data Center",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.SERVER,
            "is_open": True,
            "divisions": ServerEmbeddedModel(server_type="Data Center"),
        }
    ]

    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_gym(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 5,
            "name": "UFitness",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.GYM,
            "is_open": True,
            "divisions": GymEmbeddedModel(phone="+9112345678", fee_details=600),
        }
    ]

    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_insurance(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 5,
            "name": "UInsurance",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.INSURANCE,
            "is_open": True,
            "divisions": InsuranceEmbeddedModel(
                phone="+9112345678", working_days=["Monday, Wednesday"]
            ),
        }
    ]

    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_hr(ust_ind, ust_au):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 4,
            "name": "HR",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.HR,
            "is_open": True,
            "divisions": HrEmbeddedModel(phone="+9112345678"),
        },
        {
            "company": ust_au.pk,
            "floor_number": 1,
            "name": "HR-HEAD",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.HR,
            "is_open": True,
            "divisions": HrEmbeddedModel(phone="+9112345678"),
        },
    ]

    for data in generic_data:
        DivisionModel.objects.create(**data)


def populate_health(ust_ind):
    generic_data = [
        {
            "company": ust_ind.pk,
            "floor_number": 5,
            "name": "Wellness Clinic",
            "occupancy_status": OccupancyStatusEnum.FREE,
            "type": DivisionTypeEnum.HEALTH,
            "is_open": True,
            "divisions": HealthEmbeddedModel(
                health_category=[
                    HealthItemsEmbeddedModel(
                        phone="+9112345678",
                        type=HealthTypeEnum.HEALTH_CLINIC,
                        available_days=["Tuesday", "Thursday"],
                    ),
                    HealthItemsEmbeddedModel(
                        phone="+9112345678",
                        type=HealthTypeEnum.DENTAL,
                        available_days=["Monday", "Friday"],
                    ),
                ]
            ),
        }
    ]

    for data in generic_data:
        DivisionModel.objects.create(**data)


def main():
    populate_company()
    ust_ind = CompanyModel.objects(country=Country.IN).get()
    ust_us = CompanyModel.objects(country=Country.US).get()
    ust_au = CompanyModel.objects(country=Country.AU).get()
    populate_division(ust_ind, ust_us, ust_au)
    populate_people(ust_ind, ust_us, ust_au)
    populate_events(ust_ind)


if __name__ == "__main__":
    import settings  # noqa

    main()
