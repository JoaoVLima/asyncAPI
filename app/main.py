from enum import Enum
from typing import Union
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import ORJSONResponse, RedirectResponse
from pydantic import BaseModel

app = FastAPI(
        title="AsyncAPI",
        description="Desenvolvida com FastAPI para buscar dados de CNPJ, \
                     utilizando RabbitMQ para gerenciamento de filas e Redis \
                     para armazenamento temporário de resultados, \
                     com suporte a implantação via Docker.",
        version="0.0.1",
        contact={
            "name": "João Lima",
            "url": "https://limadeveloper.com/",
            "email": "joao@limadeveloper.com",
        },
        default_response_class=ORJSONResponse,
        debug=True,
)


class Tags(Enum):
    items = "items"
    users = "users"


@app.get("/",
         status_code=status.HTTP_200_OK,
         description="Home request, the root url redirects to /docs.")
async def root():
    return RedirectResponse("/docs")


@app.post("/scrape",
         status_code=status.HTTP_200_OK,
         description="Scrape request, sends the cnpj to the task queue")
async def scrape(cnpj: str):
    # task_id = await send_task_to_queue(cnpj)
    return {"task_id": 1}


@app.get("/results/{task_id}",
         status_code=status.HTTP_200_OK,
         description="Get Results request, get the results from the tasks")
async def get_results(task_id: str):
    # status = await get_task_status(task_id)
    status = "wait"
    if status == "completed":
        # result = await get_task_result(task_id)
        return {"status": status, "result": "deu certo"}
    return {"status": status}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


class Message(BaseModel):
    detail: str


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.put("/items/{item_id}",
         responses={404: {"model": Message}})
async def update_item(item_id: int, item: Item):
    if item_id == 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {"item_name": item.name, "item_id": item_id}


@app.post("/items/",
          status_code=status.HTTP_201_CREATED,
          description="sadasd sada s",
          response_model=Item)
async def create_item(item: Item):
    return item
