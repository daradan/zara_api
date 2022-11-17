import uvicorn
from fastapi import FastAPI, Depends

from routers.woman_products import router as w_router
from routers.man_products import router as m_router
from routers.promo import router as promo_router
from routers.search import router as search_router

from dependencies import check_token

app = FastAPI(title='Zara Parser API')
app.include_router(w_router)
app.include_router(m_router)
app.include_router(promo_router)
app.include_router(search_router, dependencies=[Depends(check_token)])

if __name__ == "__main__":
    uvicorn.run(app)
