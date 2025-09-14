import fastapi
app = fastapi.FastAPI()

@app.get("/")
def read_root():
    my_friends = ["Rifat", "Imtiaz", "Rakib", "Toky", "Arafat", "Noyon"]
    return {"friends": my_friends}