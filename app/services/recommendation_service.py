from app.services.movie_service import get_movies_by_genres

# TMDb Genre IDs
EMOTION_TO_GENRES = {
    "joy": [35, 10751],          # Comedy, Family
    "sadness": [18],             # Drama
    "anger": [28],               # Action
    "fear": [35, 12],            # Comedy, Adventure
    "love": [10749],             # Romance
    "surprise": [878, 14],       # Sci-Fi, Fantasy
    "neutral": [18, 35]          # Drama, Comedy
}


def recommend_movies(emotion: str):
    """
    Return recommended movies based on emotion.
    """

    genres = EMOTION_TO_GENRES.get(
        emotion.lower(),
        [18]
    )

    return get_movies_by_genres(genres)


if __name__ == "__main__":

    movies = recommend_movies("sadness")

    for movie in movies:
        print(movie["title"])