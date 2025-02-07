from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/version")
async def version():
    return {"version": "0.1.0"}

@app.get("/endpoint")
async def endpoint():
    return {"message": "Hello from endpoint"}

@app.get("/new_test")
async def new_test():
    return {"message": "This is a new test"}