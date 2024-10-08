from databases.documents.divisions import DivisionModel
from databases.embedded_documents.job_description import JobDescriptionEmbeddedModel
from databases.embedded_documents.office import AccountEmbeddedModel
from databases.enums.division_type import DivisionTypeEnum


def get_job_vacancies(**kwargs) -> dict | None:
    tech_stack = kwargs.get("job_vacancy")

    if not tech_stack:
        return None

    queryset = DivisionModel.objects(
        type=DivisionTypeEnum.ACCOUNT,
    )

    # TODO: Look for vacancies in a specific account
    # TODO: Look for vacancies with specific years of experience
    if not tech_stack:
        return None

    accounts: list[DivisionModel] = list(queryset)

    # First see if the tech_stack is in the job role field
    for account in accounts:
        acc: AccountEmbeddedModel = account.divisions  # type: ignore
        jobs: list[JobDescriptionEmbeddedModel] = acc.job_openings  # type: ignore

        for job in jobs:
            if str(job.role).lower() == tech_stack.lower():
                return {
                    "type": "ACCOUNT",
                    "room_id": account.room_id,
                    "job_available": True,
                    "job_position": job.role,
                    "job_requirements": [
                        requirement.title()
                        for requirement in job.requirements  # type: ignore
                    ],
                    "job_yoe": job.yoe,
                    "hide_map": True,
                }
    # See if it's in job domain
    for account in accounts:
        acc: AccountEmbeddedModel = account.divisions  # type: ignore
        jobs: list[JobDescriptionEmbeddedModel] = acc.job_openings  # type: ignore

        for job in jobs:
            if str(job.job_domain).lower() == tech_stack.lower():
                return {
                    "type": "ACCOUNT",
                    "room_id": account.room_id,
                    "job_available": True,
                    "job_position": job.role,
                    "job_requirements": [
                        requirement.title()
                        for requirement in job.requirements  # type: ignore
                    ],
                    "job_yoe": job.yoe,
                    "hide_map": True,
                }

    if len(tech_stack.split()) >= 2:
        blocklist = [
            "Developer",
            "Engineer",
            "Analyst",
            "Architect",
            "Manager",
            "Designer",
            "Consultant",
            "Administrator",
            "Scientist",
            "Specialist",
            "Technician",
            "Coordinator",
            "Lead",
            "Executive",
            "Consultant",
        ]

        for word in blocklist:
            if tech_stack.split()[-1] in [
                word,
                word.lower(),
                word.title(),
                word.upper(),
            ]:
                tech_stack = tech_stack.split()[0]

    tech_stack = tech_stack.strip().lower()

    for account in accounts:
        acc: AccountEmbeddedModel = account.divisions  # type: ignore
        jobs: list[JobDescriptionEmbeddedModel] = acc.job_openings  # type: ignore

        for job in jobs:
            if tech_stack in job.requirements:  # type: ignore
                return {
                    "type": "ACCOUNT",
                    "room_id": account.room_id,
                    "job_available": True,
                    "job_position": job.role,
                    "job_requirements": [
                        requirement.title()
                        for requirement in job.requirements  # type: ignore
                    ],
                    "job_yoe": job.yoe,
                    "hide_map": True,
                }
