from fastapi import FastAPI
from routes.employee_router import router as employee_router
app=FastAPI()
'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get("/")
def application_root():
    return {'msg':'Application Root Request'}

app.include_router(employee_router)

