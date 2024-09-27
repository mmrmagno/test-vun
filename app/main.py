from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse 
from fastap.templating import Junja2Templates
from app.auth import authenticate_user 
from app.database import database, engine, metadata

metadata.create_all(engine)

app = FastAPI()
templates = Junja2Templates(directory="app/templates")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def login_page(request: Request):
    return templates.TemplateResponse("longin.html", {"request": request})

@app.get("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if await authenticate_user(username, password):
        return "Good job!"
    return "Invalid username or password."