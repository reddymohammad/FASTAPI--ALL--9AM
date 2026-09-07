from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def home_page():
  return{'msg':'application root request'}
@app.post("/create")
def create_user():
  return{'msg':'new user created'}
@app.put("/udpate")
def update_user():
  return{'msg':'user update successfully'}
@app.delete("/delete")
def delete_user():
  return{'msg':'deleted successfully'}