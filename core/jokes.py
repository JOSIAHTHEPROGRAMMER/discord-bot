import requests

def get_joke() -> str:
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("joke", "I couldn't find a joke for you right now.")
    except requests.RequestException:
        pass
    return "I couldn't retrieve a joke for you right now."
