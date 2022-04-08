from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/penis", response_class=FileResponse)
async def penis():
    html_content = "views/signin.html"

    return FileResponse(html_content)

