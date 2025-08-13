from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Mission-specific prompt 
MISSION_PROMPTS = {
    "Dominate my discipline": (
        "Create a short, ruthless, and motivating one-sentence quote about mastering self-discipline. "
        "Make it sound aggressive, no fluff, high intensity, targeted at high-achievers and hustlers. "
        "It should trigger the reader to take immediate action and feel shame for procrastinating."
    ),
    "Crush my business/career": (
        "Generate a short, brutal business or career motivation quote that focuses on dominance, winning, "
        "and outworking the competition. It must sound confident and aggressive, aimed at someone who wants "
        "to crush all rivals and climb to the top."
    ),
    "Conquer my body": (
        "Write a powerful, aggressive one-line quote about pushing your body to its limits, destroying weakness, "
        "and forging physical greatness. It should sound like something a relentless athlete would live by."
    ),
    "Forge an unbreakable mindset": (
        "Create a short, cutting motivational sentence about building mental toughness and resilience. "
        "It should sound like advice from a battle-hardened warrior — no comfort, only truth, and the will to endure anything."
    ),
    "Relentless motivation": (
        "Write a short, hard-hitting motivational one-liner that gives a surge of unstoppable energy. "
        "No clichés, no generic phrases — it should sound raw, direct, and personal. Make the reader feel like there are no excuses left."
    )
}

class UserData(BaseModel):
    age: str
    name: str
    gender: str
    language: str
    mission: str
    tone: str
    grind_level: str

def get_motivational_message(user: UserData):
    current_time = datetime.now().strftime("%I:%M %p %z on %A, %B %d, %Y")
    
    mission_prompt = MISSION_PROMPTS.get(user.mission, "Write a short motivational message.")
    
    prompt = (
        f"{mission_prompt} "
        f"Write it in {user.language}, for a {user.age} year-old named {user.name}, identified as {user.gender}. "
        f"Deliver it in a {user.tone.lower()} tone to match a {user.grind_level.lower()} grind level. "
        f"Tailor it to the current time: {current_time}. "
        f"Limit it to 1-2 sentences."
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a motivational coach. Provide concise, uplifting messages limited to 1-2 sentences."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=40
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error generating message: {str(e)}"

@app.get("/", response_class=HTMLResponse)
async def serve_form():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Motivational Message Generator</title>
    </head>
    <body style="font-family: Arial; max-width: 500px; margin: auto; padding: 20px;">
        <h2>Motivational Message Generator</h2>
        <form id="motivationForm">
            <label>Age Group:</label>
            <select name="age">
                <option>13 to 17</option>
                <option>18 to 24</option>
                <option>25 to 34</option>
                <option>35 to 44</option>
                <option>45 to 54</option>
                <option>55+</option>
            </select><br><br>

            <label>Name:</label>
            <input type="text" name="name" required><br><br>

            <label>Gender:</label>
            <select name="gender">
                <option>Female</option>
                <option>Male</option>
                <option>Other</option>
                <option>Prefer not to say</option>
            </select><br><br>

            <label>Language:</label>
            <select name="language">
                <option>English (US)</option>
                <option>English (UK)</option>
                <option>French (FR)</option>
                <option>German (DE)</option>
            </select><br><br>

            <label>Mission:</label>
            <select name="mission">
                <option>Dominate my discipline</option>
                <option>Crush my business/career</option>
                <option>Conquer my body</option>
                <option>Forge an unbreakable mindset</option>
                <option>Relentless motivation</option>
            </select><br><br>

            <label>Tone:</label>
            <select name="tone">
                <option>Hardcore</option>
                <option>Elite</option>
                <option>Hybrid</option>
            </select><br><br>

            <label>Grind Level:</label>
            <select name="grind_level">
                <option>Starting the climb</option>
                <option>In the trenches</option>
                <option>No mercy</option>
            </select><br><br>

            <button type="submit">Generate</button>
        </form>

        <h3>Message:</h3>
        <div id="output" style="font-weight: bold; color: darkblue;"></div>

        <script>
            document.getElementById("motivationForm").addEventListener("submit", async (e) => {
                e.preventDefault();
                const formData = new FormData(e.target);
                const response = await fetch("/generate", {
                    method: "POST",
                    body: formData
                });
                const data = await response.json();
                document.getElementById("output").innerText = data.message;
            });
        </script>
    </body>
    </html>
    """

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
    user_data = UserData(
        age=age,
        name=name,
        gender=gender,
        language=language,
        mission=mission,
        tone=tone,
        grind_level=grind_level
    )
    message = get_motivational_message(user_data)
    return {"message": message}
