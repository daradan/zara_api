from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from dependencies import get_db
from models import ZaraWomanProducts, ZaraWomanPrices, ZaraManProducts, ZaraKidProducts, ZaraBeautyProducts, ZaraOriginsProducts
from schemas import SearchSchema, ZaraWomanProductsSchema

router = APIRouter(prefix='/products/search', tags=['Products Search'])


@router.post('/all')
def filter_all_products(
    filters: SearchSchema,
    db: Session = Depends(get_db)
):
    tables = [ZaraWomanProducts, ZaraManProducts, ZaraKidProducts, ZaraBeautyProducts, ZaraOriginsProducts]
    res = []
    for table in tables:
        products = db.query(table).filter(table.name.ilike(f"%{filters.name}%")).all()
        res += products
    return res
