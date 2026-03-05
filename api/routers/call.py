from fastapi import APIRouter, Depends, status,Request
from api.config.schemas import MSG
from api.function.func import call_func
from fastapi.templating import Jinja2Templates
import os
import json


calls_router = APIRouter(tags=["Совершение вызова"])

templates = Jinja2Templates(directory=os.path.abspath(os.path.expanduser('ui')))

@calls_router.get("/", name="main_route")
async def main_func(request:Request):
    json_path = os.path.join("/book", 'telephonebook.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            phonebook_data = json.load(f)
    except:
        phonebook_data = {}
    return templates.TemplateResponse(name='index.html', context={
        'request': request,
        'phonebook_data': json.dumps(phonebook_data, ensure_ascii=False)
    })


@calls_router.post(
    "/api/calls",
    status_code=status.HTTP_200_OK,
    response_model=MSG,
    name="Создание вызова Абонентом",
    description="Создание вызова Абонентом",
)
async def post_call_route(result=Depends(call_func)) -> MSG:
    return result