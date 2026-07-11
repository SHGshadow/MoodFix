import requests

from app.config import TMDB_API_TOKEN

BASE_URL = "https://api.themoviedb.org/3"

HEADERS = {
    "Authorization": f"Bearer {TMDB_API_TOKEN}",
    "accept": "application/json"
}


def get_trending_movies():
    """
    Fetch the top 8 trending movies of the week from TMDb.
    """

    response = requests.get(
        f"{BASE_URL}/trending/movie/week",
        headers=HEADERS,
        timeout=10
    )

    response.raise_for_status()

    return response.json()["results"][:8]