from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.services.movie_service import get_trending_movies

app = FastAPI(title="MoodFlix")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request):

    movies = get_trending_movies()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "movies": movies
        },
    )