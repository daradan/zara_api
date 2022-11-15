import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from models import ZaraWomanProducts, ZaraWomanPrices
from schemas import SearchSchema, ZaraWomanProductsSchema

router = APIRouter(prefix='/promo', tags=['Promo'])


@router.get('/discounts')
def get_discounts(
    db: Session = Depends(get_db)
):
    discounts = db.query(ZaraWomanPrices.product_id).filter(
        ZaraWomanPrices.discount < 0,
        ZaraWomanPrices.created > datetime.datetime.now() - datetime.timedelta(days=7)
    ).distinct().all()
    product_ids = [discount[0] for discount in discounts]
    products = db.query(ZaraWomanProducts).filter(ZaraWomanProducts.id.in_(product_ids)).all()
    response = []
    for product in products:
        price = db.query(ZaraWomanPrices).filter_by(product_id=product.id).order_by(ZaraWomanPrices.created.desc()).first()
        response.append({
            'product': product,
            'price': price
        })
    return response
