from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/greet/{name}")
async def greet_name(name:str)->dict:
    return {"message":f"Hello, {name}!"}

def start():
    """Start the FastAPI server."""
    uvicorn.run("book_api.main:app", host="127.0.0.1", port=8080, reload=True)

if __name__ == "__main__":
    start()