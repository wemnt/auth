from typing import List

from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from models.utils import as_form

app = FastAPI()

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
