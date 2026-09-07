from fastapi import FastAPI

app=FastAPI()

@app.get("/",description="Application Root Request")
def home_page():
    return {'msg':'Application Root Request'}

@app.get("/about", description="About Request")
def about_page():
    return {'msg':'About Page'}

@app.get("/contact", description="Contact Page")
def contact_page():
    return {'msg':'Contact Page'}