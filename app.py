from typing import List
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from database.connect import database
from models.utils import as_form
from routes import users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])

templates = Jinja2Templates(directory="views")


class Test1(BaseModel):
    a: str
    b: int


@as_form
class Test(BaseModel):
    username: str
    password: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/penis", response_class=HTMLResponse)
async def penis(request: Request):
    html_content = "views/signin.html"

    return templates.TemplateResponse("signin.html", {"request": request})


@app.post("/penis", response_model=Test)
async def read_login(request: Request, form: Test = Depends(Test.as_form)):
    return form

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()