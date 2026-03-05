from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from starlette.exceptions import HTTPException
from api.config.config import logger
from api.config.exceptions import (
    all_http_exception_handler,
    response_validation_exception_handler,
    validation_exception_handler,
)
from api.routers import call


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Приложение запущено")
    yield
    logger.info("Работа приложения завершена")


app = FastAPI(lifespan=lifespan, debug=True)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, all_http_exception_handler)
app.add_exception_handler(
    ResponseValidationError, response_validation_exception_handler
)

app.include_router(call.calls_router)