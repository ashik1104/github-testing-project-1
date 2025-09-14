import fastapi
app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"string": "Hello, This is my first FastAPI app!"}