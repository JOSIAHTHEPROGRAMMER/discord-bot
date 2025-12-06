import re
from random import choice, randint
from .jokes import get_joke

from .weather import get_weather




def clean_text(text: str) -> str:
    return re.sub(r'[^a-z0-9 ?!]', '', text.lower())

def get_scenario(user_question: str) -> str:
    lowered = clean_text(user_question.strip())
    if not lowered:
        return "Well, you are silent."

    greetings = ["hi", "hello", "hey", "greetings"]
    if any(g in lowered for g in greetings):
        return "Hello! How can I assist you today?"

    if "how are you" in lowered or "how are you doing" in lowered:
        return "I am just a bot, but I am here to help! How can I assist you?"

    if "what is your name" in lowered or "who are you" in lowered:
        return "I am your friendly We Go Pass bot. How can I assist you today?"

    if "help" in lowered:
        return "Sure! You can ask me about commands, jokes, weather, or even AI with `?wgp ai ...`."

    if "thank you" in lowered or "thanks" in lowered:
        return "You're welcome! Ask me anything else if you like."

    if "bye" in lowered or "goodbye" in lowered:
        return "Goodbye! Have a great day!"

    if "what can you do" in lowered or "your capabilities" in lowered:
        return "I can tell jokes, flip coins, roll dice, play small games, check weather, and answer AI questions with `?wgp ai ...`."

    if "joke" in lowered:
        return get_joke()

    if "weather" in lowered:
        parts = lowered.split("weather", 1)
        location = parts[1].strip() if len(parts) > 1 else ""
        if not location:
            return "Please provide a city/country. Example: `?wgp weather London,GB`"

        return get_weather(location)


    if "time" in lowered:
        return "I can't tell the exact time, but you can ask other questions!"

    if "date" in lowered:
        return "I can't provide the current date, but I can answer lots of other stuff!"

    if "your creator" in lowered or "who made you" in lowered:
        return "I was created by a developer using Discord API and some clever programming."

    preferences = {
        "color": "I don’t have a favorite color, but I think all colors are great!",
        "food": "I don’t eat, but pizza seems to be everyone's favorite!",
        "movie": "I can't watch movies, but sci-fi sounds exciting!",
        "music": "I don't listen to music, but every genre has its magic!",
        "game": "I can’t play games, but I know they are fun!"
    }
    for key, val in preferences.items():
        if key in lowered and any(w in lowered for w in ["favorite", "like"]):
            return val

    if "where are you from" in lowered:
        return "I exist in the digital realm, helping on Discord!"

    if "age" in lowered or "how old are you" in lowered:
        return "I don't have an age, but I'm as old as the code that runs me!"

    if "we go pass" in lowered:
        return "We go pass"

    if "tyrese is a cool" in lowered:
        return "He is indeed!"

    if "roll dice" in lowered:
        return f"You rolled: {randint(1,6)}"

    if "coin flip" in lowered:
        return f"The coin landed on: {choice(['heads','tails'])}"

    if "guess number" in lowered:
        number = randint(1,10)
        return f"Guess a number between 1 and 10. I am thinking of {number}."

    if "?" in lowered:
        return "That's an interesting question. You might want to try `?wgp ai ...` for a funny answer."

    fallback_responses = [
        "I'm not sure how to respond to that. Maybe try another question?",
        "That's a good one! Can you tell me more?",
        "Hmm, I'm a bit confused. Let's try something else!",
        "Interesting! What else can I help with?",
        "I wish I knew the answer. Try asking differently?",
        "Good question! Unfortunately, I don't have the answer.",
        "I'm stumped! How about asking something else?"
    ]
    return choice(fallback_responses)
