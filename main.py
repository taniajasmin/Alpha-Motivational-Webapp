import openai
from dotenv import load_dotenv
import os
from datetime import datetime
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_motivational_message(age, name, gender, language, mission, tone, grind_level):
    current_time = datetime.now().strftime("%I:%M %p %z on %A, %B %d, %Y")
    prompt = f"Generate a 1-2 sentence, uplifting motivational message in {language} for a {age} year-old named {name}, identified as {gender}. Their mission is to {mission.lower()}, delivered in a {tone.lower()} tone to match a {grind_level.lower()} grind level, tailored to the current time: {current_time}."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a motivational coach crafting concise, personalized 1-2 sentence messages."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50  # Limit to ensure 1-2 sentences
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating message: {str(e)}")

@app.get("/", response_class=HTMLResponse)
async def get_form():
    with open("demo.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.post("/generate")
async def generate_message(
    age: str = Form(...),
    name: str = Form(...),
    gender: str = Form(...),
    language: str = Form(...),
    mission: str = Form(...),
    tone: str = Form(...),
    grind_level: str = Form(...)
):
    message = get_motivational_message(age, name, gender, language, mission, tone, grind_level)
    return {"motivation": message}