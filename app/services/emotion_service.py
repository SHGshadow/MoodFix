from transformers import pipeline

# Load the model only once when the application starts
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)


def detect_emotion(text: str) -> str:
    """
    Detect the dominant emotion from user input.
    """

    result = emotion_classifier(text)

    return result[0][0]["label"]

if __name__ == "__main__":
    text = "I had a stressful day at university."

    emotion = detect_emotion(text)

    print(emotion)