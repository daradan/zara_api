from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from models import ZaraWomanProducts, ZaraWomanPrices
from schemas import SearchSchema, ZaraWomanProductsSchema

router = APIRouter(prefix='/products/woman', tags=['Woman Products'])


@router.get('/{product_id}', response_model=ZaraWomanProductsSchema)
def get_woman_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(ZaraWomanProducts).filter_by(id=product_id).first()
    if not product:
        return HTTPException(status_code=404)
    return product


@router.post('/search')
def filter_woman_product(
    filters: SearchSchema,
    db: Session = Depends(get_db)
):
    query_filters = [ZaraWomanProducts.name.ilike(f"%{filters.name}%")]
    if filters.category:
        query_filters.append(ZaraWomanProducts.category == filters.category)
    if filters.color:
        query_filters.append(ZaraWomanProducts.color == filters.color)
    products = db.query(ZaraWomanProducts).filter(*query_filters).all()
    return products


@router.get('/{product_id}/prices')
def get_product_prices(
    product_id: int,
    db: Session = Depends(get_db)
):
    prices = db.query(ZaraWomanPrices).filter_by(product_id=product_id).all()
    return prices
