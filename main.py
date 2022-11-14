import uvicorn
from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from models import ZaraWomanProducts
from database import SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class SearchSchema(BaseModel):
    name: str
    category: str = None
    color: str = None


@app.get('/products/woman/{product_id}')
def get_woman_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(ZaraWomanProducts).filter_by(id=product_id).first()
    if not product:
        return HTTPException(status_code=404)
    return product


@app.post('/products/woman/search')
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


@app.delete('/products/woman/{product_id}')
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(ZaraWomanProducts).filter_by(id=product_id).first()
    if not product:
        return HTTPException(status_code=404)
    db.query(ZaraWomanProducts).filter_by(id=product_id).delete()
    return {"message": "deleted"}


if __name__ == "__main__":
    uvicorn.run(app)

