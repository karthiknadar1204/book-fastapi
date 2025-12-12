from fastapi import FastAPI,Header
import uvicorn
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/greet/{name}")
async def greet_name(name:Optional[str]="User",age:int=0)->dict:
    return {"message":f"Hello, {name}! You are {age} years old."}

class BookCreateModel(BaseModel):
    title:str
    author:str

@app.post("/create_book")
async def create_book(book_data:BookCreateModel):
    return {"message":f"Book {book_data.title} created successfully for author {book_data.author}."}


@app.get("/get_headers")
async def get_headers(
    accept:str=Header(None),
    content_type:str=Header(None)
):
    request_headers={}
    request_headers["Accept"]=accept
    request_headers["Content-Type"]=content_type
    return request_headers

def start():
    """Start the FastAPI server."""
    uvicorn.run("book_api.main:app", host="127.0.0.1", port=8080, reload=True)

if __name__ == "__main__":
    start()