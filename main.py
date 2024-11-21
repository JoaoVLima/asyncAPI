from typing import Union
from fastapi import FastAPI
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


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
