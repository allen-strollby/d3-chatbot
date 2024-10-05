from poli_enum.country import Country

from databases.documents.company import CompanyModel


def populate_people():
    pass


def populate_events():
    pass


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


def populate_amenity():
    pass


def populate_division():
    pass


def main():
    populate_company()


if __name__ == "__main__":
    import settings  # noqa

    main()
