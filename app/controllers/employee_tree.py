from databases.enums import EntityTypeEnum


def return_employee_tree(**kwargs):
    type = kwargs.get("type")
    employee_type = EntityTypeEnum(type)
    print(employee_type)

