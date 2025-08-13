import openai
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Mission-specific prompt styles
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

def get_motivational_message(age, name, gender, language, mission, tone, grind_level):
    current_time = datetime.now().strftime("%I:%M %p %z on %A, %B %d, %Y")
    
    # Select mission-specific style prompt
    mission_prompt = MISSION_PROMPTS.get(mission, "Write a short motivational message.")
    
    # Full dynamic prompt
    prompt = (
        f"{mission_prompt} "
        f"Write it in {language}, for a {age} year-old named {name}, identified as {gender}. "
        f"Deliver it in a {tone.lower()} tone to match a {grind_level.lower()} grind level. "
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
        print(f"Error generating message: {str(e)}")
        return "Unable to generate message at this time."

def collect_user_info():
    print("Please provide your information:")
    
    # Age options
    print("1. 13 to 17\n2. 18 to 24\n3. 25 to 34\n4. 35 to 44\n5. 45 to 54\n6. 55+")
    age_choice = int(input("Select your age group (1-6): "))
    age_options = ["13 to 17", "18 to 24", "25 to 34", "35 to 44", "45 to 54", "55+"]
    age = age_options[age_choice - 1] if 1 <= age_choice <= 6 else "25 to 34"

    # Name
    name = input("What do you want to be called?: ")

    # Gender options
    print("1. Female\n2. Male\n3. Other\n4. Prefer not to say")
    gender_choice = int(input("Select your gender (1-4): "))
    gender_options = ["Female", "Male", "Other", "Prefer not to say"]
    gender = gender_options[gender_choice - 1] if 1 <= gender_choice <= 4 else "Male"

    # Language options
    print("1. English (US)\n2. English (UK)\n3. French (FR)\n4. German (DE)")
    language_choice = int(input("Select your language (1-4): "))
    language_options = ["English (US)", "English (UK)", "French (FR)", "German (DE)"]
    language = language_options[language_choice - 1] if 1 <= language_choice <= 4 else "English (US)"

    # Mission options
    print("1. Dominate my discipline\n2. Crush my business/career\n3. Conquer my body\n4. Forge an unbreakable mindset\n5. Relentless motivation")
    mission_choice = int(input("Select your mission (1-5): "))
    mission_options = ["Dominate my discipline", "Crush my business/career", "Conquer my body", "Forge an unbreakable mindset", "Relentless motivation"]
    mission = mission_options[mission_choice - 1] if 1 <= mission_choice <= 5 else "Crush my business/career"

    # Tone options
    print("1. Hardcore\n2. Elite\n3. Hybrid")
    tone_choice = int(input("Select your motivation tone (1-3): "))
    tone_options = ["Hardcore", "Elite", "Hybrid"]
    tone = tone_options[tone_choice - 1] if 1 <= tone_choice <= 3 else "Elite"

    # Grind level options
    print("1. Starting the climb\n2. In the trenches\n3. No mercy")
    grind_choice = int(input("Select your grind level (1-3): "))
    grind_options = ["Starting the climb", "In the trenches", "No mercy"]
    grind_level = grind_options[grind_choice - 1] if 1 <= grind_choice <= 3 else "In the trenches"
    
    return {
        "age": age,
        "name": name,
        "gender": gender,
        "language": language,
        "mission": mission,
        "tone": tone,
        "grind_level": grind_level
    }

if __name__ == "__main__":
    user_data = collect_user_info()
    
    message = get_motivational_message(
        user_data["age"],
        user_data["name"],
        user_data["gender"],
        user_data["language"],
        user_data["mission"],
        user_data["tone"],
        user_data["grind_level"]
    )
    print(f"Motivational Message: {message}")