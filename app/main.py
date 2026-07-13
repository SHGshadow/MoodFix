from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.services.movie_service import get_trending_movies
from fastapi import Form
from app.services.emotion_service import detect_emotion
from app.services.recommendation_service import recommend_movies


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

@app.post("/recommend")
def recommend(request: Request, feeling: str = Form(...)):

    emotion = detect_emotion(feeling)

    movies = recommend_movies(emotion)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "movies": movies,
            "emotion": emotion,
            "feeling": feeling
        }
    )