from fastapi import FastAPI

import settings  # noqa
from routers import health_check_router


app = FastAPI()

app.include_router(health_check_router, prefix="")
