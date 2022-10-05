import os
import json
import sys
import uvicorn
import logging
from fastapi import FastAPI
from app.config import settings
from app.routers.schedule_tasks import router as tasks_router


app = FastAPI(title="Celery API", version=settings.VERSION)


app.include_router(tasks_router)

if __name__ == "__main__":
    if (len(sys.argv) == 2) and (sys.argv[1] == "openapi"):
        from fastapi.openapi.utils import get_openapi

        with open("openapi.json", "w") as f:
            json.dump(
                get_openapi(
                    title=app.title,
                    version=app.version,
                    openapi_version=app.openapi_version,
                    description=app.description,
                    routes=app.routes,
                ),
                f,
            )

    else:
        uvicorn.run(
            "main:app",
            host="localhost",
            reload=settings.DEBUG_MODE,
            port=settings.PORT,
        )