import datetime

from pydantic import BaseModel


class SearchSchema(BaseModel):
    name: str
    category: str = None
    color: str = None


class ZaraWomanProductsSchema(BaseModel):
    id: int
    created: datetime.datetime
    market: str
    url: str
    store_id: int
    name: str
    color: str
    category: str
    description: str
    availability: str
    image: str


class ZaraManProductsSchema(BaseModel):
    id: int
    created: datetime.datetime
    market: str
    url: str
    store_id: int
    name: str
    color: str
    category: str
    description: str
    availability: str
    image: str
