import uvicorn
from fastapi import FastAPI

from routers.woman_products import router as w_router
from routers.man_products import router as m_router
from routers.promo import router as promo_router

app = FastAPI(title='Zara Parser API')
app.include_router(w_router)
app.include_router(m_router)
app.include_router(promo_router)

if __name__ == "__main__":
    uvicorn.run(app)
