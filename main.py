from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, UVCodes"}

@app.get ("/about")
def about():
    return {"message": "This is about page of my fastapi project."}

