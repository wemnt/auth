from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates



app = FastAPI()

templates = Jinja2Templates(directory="views")



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/penis", response_class=HTMLResponse)
async def penis(request: Request):
    html_content = "views/signin.html"

    return templates.TemplateResponse("signin.html", {"request": request})


@app.post("/login")
async def read_login(email: str = Form(...), password: str = Form(...)):
    form = {"email": email, "password": password}

    return form