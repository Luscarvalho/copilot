"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    # Atividades Esportivas
    "Soccer Team": {
        "description": "School soccer team with regular practice and competitions",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 22,
        "participants": ["alex@mergington.edu", "lucas@mergington.edu"]
    },
    "Swimming Club": {
        "description": "Swimming lessons and competitive training",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["julia@mergington.edu", "noah@mergington.edu"]
    },
    # Atividades Artísticas
    "Theater Club": {
        "description": "Drama, acting and annual school play production",
        "schedule": "Wednesdays, 3:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["emily@mergington.edu", "james@mergington.edu"]
    },
    "Art Workshop": {
        "description": "Painting, drawing and various art technique exploration",
        "schedule": "Fridays, 2:00 PM - 4:00 PM",
        "max_participants": 15,
        "participants": ["sarah@mergington.edu", "david@mergington.edu"]
    },
    # Atividades Intelectuais
    "Debate Team": {
        "description": "Public speaking, argumentation, and competitive debates",
        "schedule": "Mondays and Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["grace@mergington.edu", "ethan@mergington.edu"]
    },
    "Science Olympiad": {
        "description": "Science competitions preparation and team challenges",
        "schedule": "Tuesdays, 3:30 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["oliver@mergington.edu", "ava@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail=f"Student {email} is already signed up for {activity_name}")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
