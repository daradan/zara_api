from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from models import ZaraManProducts
from schemas import SearchSchema, ZaraManProductsSchema

router = APIRouter(prefix='/products/man', tags=['Man Products'])


@router.get('/{product_id}', response_model=ZaraManProductsSchema)
def get_man_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(ZaraManProducts).filter_by(id=product_id).first()
    if not product:
        return HTTPException(status_code=404)
    return product


@router.post('/search')
def filter_woman_product(
    filters: SearchSchema,
    db: Session = Depends(get_db)
):
    query_filters = [ZaraManProducts.name.ilike(f"%{filters.name}%")]
    if filters.category:
        query_filters.append(ZaraManProducts.category == filters.category)
    if filters.color:
        query_filters.append(ZaraManProducts.color == filters.color)
    products = db.query(ZaraManProducts).filter(*query_filters).all()
    return products
