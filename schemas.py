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
    url: str = None
    store_id: int = None
    name: str = None
    color: str = None
    category: str = None
    description: str = None
    availability: str = None
    image: str = None


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
