from fastapi import FastAPI
import asyncio
app=FastAPI()
'''

Rest API URL: http://127.0.0.1:8000/welcome
Method Type:GET
'''
@app.get("/welcome")
async def welcome():
    await asyncio.sleep(5)
    return {"msg":"Welcome to FastAPI"}