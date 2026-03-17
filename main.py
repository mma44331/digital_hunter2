import uvicorn
from fastapi import FastAPI
from routes import route


app = FastAPI()

app.include_router(route)

if __name__ == "main":
    uvicorn.run("main:app",host="localhost",port=8000,reload=True)