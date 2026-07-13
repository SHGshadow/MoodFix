# 🎬 MoodFlix AI

An AI-powered movie recommendation web application that understands users' emotions from natural language and recommends personalized movies using Machine Learning and the TMDb API.


## 🚀 Features

- 🤖 AI-powered emotion detection using Hugging Face Transformers
- 🎭 Natural Language Processing (NLP) for understanding user feelings
- 🎬 Personalized movie recommendations
- 🔥 Real-time Trending Movies
- ⭐ Movie ratings and posters
- 📱 Modern responsive user interface
- ⚡ FastAPI backend
- 🌐 TMDb API integration


## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- Jinja2

### AI / Machine Learning
- Hugging Face Transformers
- DistilRoBERTa Emotion Classification Model
- Natural Language Processing (NLP)

### Frontend
- HTML5
- CSS3
- JavaScript

### API
- TMDb (The Movie Database) API

### Version Control
- Git
- GitHub


# 🧠 How It Works


User Input
      │
      ▼
Emotion Detection
(Hugging Face Transformer)
      │
      ▼
Emotion Mapping
      │
      ▼
TMDb API
      │
      ▼
Movie Recommendations
      │
      ▼
MoodFlix Web Interface



## 📂 Project Structure

MoodFlix/
│
├── app/
│   ├── routes/
│   ├── services/
│   │   ├── emotion_service.py
│   │   ├── movie_service.py
│   │   └── recommendation_service.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   ├── utils/
│   └── main.py
│
├── docs/
├── tests/
├── requirements.txt
├── .env
└── README.md


## ⚙️ Installation

### Clone the repository

git clone https://github.com/yourusername/MoodFlix.git

cd MoodFlix

### Create a virtual environment

python -m venv venv


### Activate the environment

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

### Install dependencies

pip install -r requirements.txt


## 🔑 Environment Variables

Create a `.env` file.

TMDB_API_KEY=YOUR_TMDB_API_KEY


## ▶️ Run the Project

uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000


## 📸 Screenshots

### Homepage

<img width="1917" height="917" alt="1" src="https://github.com/user-attachments/assets/17c2798b-b2a2-40ab-beca-31c1240b040f" />


### AI Emotion Detection

<img width="1917" height="911" alt="4" src="https://github.com/user-attachments/assets/175ffc79-bad0-4817-a999-27a091c0b3ec" />


### Movie Recommendations

<img width="1917" height="911" alt="5" src="https://github.com/user-attachments/assets/4847dc64-7765-4b0d-9710-d5c09625cd9f" />

## 🎯 Key Learning Outcomes

- Machine Learning Integration
- Natural Language Processing
- Emotion Classification
- REST API Integration
- FastAPI Development
- AI-powered Recommendation Systems
- Frontend & Backend Integration
- Git & GitHub Workflow


## 🚀 Future Improvements

- User Authentication
- Movie Search
- Trailer Integration
- Watchlist
- Favorite Movies
- Recommendation History
- Cloud Deployment on AWS
- Docker Support
- CI/CD Pipeline


## 👨‍💻 Author

**Shenal Gunasekara**

Bachelor of Computing Honours in Software Engineering

University of Sri Jayewardenepura

GitHub: (https://github.com/SHGshadow)

LinkedIn: (https://www.linkedin.com/in/shenal-gunasekera-a89bb730b?utm_source=share_via&utm_content=profile&utm_medium=member_ios)


## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
