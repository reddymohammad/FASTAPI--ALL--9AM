from fastapi import FastAPI, Depends
app=FastAPI()

def get_user():
    return "Rahul"

@app.get("/user")
def create_user(uname:str=Depends(get_user)):
    return {"user":uname}