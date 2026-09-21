from fastapi import FastAPI
from routes.user_router import router as user_router
app=FastAPI()

@app.get("/")
def home_page():
  return {'msg':'root request'}


app.include_router(user_router)