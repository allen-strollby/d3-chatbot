from .db_connection import *  # noqa

import os

if os.environ.get("DOCKER_COMPOSE"):
    from scripts import populate_db

    populate_db.main()
