from fastapi import FastAPI
from routes.emp_router import router as emp_router
app=FastAPI()

@app.get("/")
def application_root():
    return {'msg':'Application Root'}

app.include_router(emp_router)