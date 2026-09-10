from fastapi import FastAPI
from routes.product_router import router as product_router
app=FastAPI()

@app.get("/")
def application_root():
    return {'msg':'Application Root'}

app.include_router(product_router)