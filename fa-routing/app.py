from fastapi import FastAPI
app=FastAPI()
from routes.user_router import router as user_router
from routes.product_router import router as product_router

'''
Rest API - End Point: 1
--------------------------
Usage: Application Root Request 
Rest API URL: http://127.0.0.1:8000/
Method Type:GET 
Requried Fields : None 
Access Type:Public 
'''
@app.get("/",description='Application Root')
def home_page():
    return {'msg':'Application Root Request'}


app.include_router(user_router)
app.include_router(product_router)