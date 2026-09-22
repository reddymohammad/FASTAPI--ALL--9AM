from fastapi import FastAPI,HTTPException
app=FastAPI()

def verify_user():
  uname='reddy'
  if uname!='reddy':
     raise  HTTPException(status_code=404,detail='user not found')
  return uname

