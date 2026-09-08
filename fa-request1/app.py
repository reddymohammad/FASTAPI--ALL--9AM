from fastapi import FastAPI
from routes.product_router import router as product_router
app=FastAPI()

@app.get("/")
def home_page():
  return {'msg':'root request'}


app.include_router(product_router)