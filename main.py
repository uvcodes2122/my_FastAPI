from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, UVCodes"}

@app.get ("/about")
def about():
    return {"message": "This is about page of my fastapi project."}

@app.get("/test1")
def test():
    return {"message": "This is test page of my fastapi project."}

