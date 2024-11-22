from enum import Enum
from typing import Union
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel

app = FastAPI(
        title="AsyncAPI",
        description="Desenvolvida com FastAPI para buscar dados de CNPJ, \
                     utilizando RabbitMQ para gerenciamento de filas e Redis \
                     para armazenamento temporário de resultados, \
                     com suporte a implantação via Docker.",
        version="0.0.1",
        default_response_class=ORJSONResponse,
        contact={
            "name": "João Lima",
            "url": "https://limadeveloper.com/",
            "email": "joao@limadeveloper.com",
        },
        debug=True,
)


class Tags(Enum):
    items = "items"
    users = "users"


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/",
         status_code=status.HTTP_200_OK,
         description="sadasd sada s")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if not item_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"item_name": item.name, "item_id": item_id}


@app.post("/items/",
          status_code=status.HTTP_201_CREATED,
          description="sadasd sada s",
          response_model=Item)
async def create_item(item: Item):
    return item
