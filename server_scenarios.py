import requests, re
from random import choice, randint



def get_joke() -> str:
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get('joke', "I couldn't find a joke for you right now, sorry!")
    except requests.RequestException:
        pass
    return "I couldn't retrieve a joke for you right now, sorry!"

    


def clean_text(text: str) -> str:
    return re.sub(r'[^a-z0-9 ?!]', '', text.lower())

def get_scenario(user_question: str) -> str:
    lowered = clean_text(user_question.strip())
    ...


    if not lowered:
        return 'Well, you are silent'
    
    greetings = ['hi', 'hello', 'hey', 'greetings']
    if any(greeting in lowered for greeting in greetings):
        return 'Hello! How can I assist you today?'
    
    elif 'how are you' in lowered or 'how are you doing' in lowered:
        return 'I am just a bot, but I am here to help you! How can I assist you?'
    
    elif 'what is your name' in lowered or 'who are you' in lowered:
        return 'I am your friendly Discord bot. How can I assist you today?'
    
    elif 'help' in lowered:
        return 'Sure! How can I help you? You can ask me about commands or any other questions you might have.'
    
    elif 'thank you' in lowered or 'thanks' in lowered:
        return 'You\'re welcome! If you have any more questions, feel free to ask.'
    
    elif 'bye' in lowered or 'goodbye' in lowered:
        return 'Goodbye! Have a great day!'
    
    elif 'what can you do' in lowered or 'your capabilities' in lowered:
        return 'I can assist with various tasks such as providing information, answering questions, and much more. Just ask!'
    
    elif 'joke' in lowered:
        return get_joke()
    
    elif 'weather' in lowered:
        return 'I can\'t check the weather right now, but you can try asking me about other things!'
    
    elif 'time' in lowered:
        return 'I can\'t tell the exact time, but I can help you with many other queries!'
    
    elif 'date' in lowered:
        return 'I can\'t provide the current date, but let me know how else I can assist you!'
    
    elif 'your creator' in lowered or 'who made you' in lowered:
        return 'I was created by a developer using the Discord API and some clever programming.'
    
    elif any(word in lowered for word in ['favorite', 'like']):
        if 'color' in lowered:
            return 'I don’t have a favorite color, but I think all colors are great!'
        elif 'food' in lowered:
            return 'I don’t eat, but I’ve heard pizza is popular!'
        elif 'movie' in lowered:
            return 'I can’t watch movies, but I hear sci-fi is great!'
        elif 'music' in lowered:
            return 'I don’t listen to music, but every genre has its magic!'
        elif 'game' in lowered:
            return 'I can’t play, but I know games are fun!'

    
    elif 'where are you from' in lowered:
        return 'I exist in the digital realm, here to help you on Discord!'
    
    elif 'age' in lowered or 'how old are you' in lowered:
        return 'I don\'t have an age like humans do, but I\'m as old as the code that runs me!'
    
 
   
    elif 'we go pass' in lowered:
        return 'We go pass'
    
    elif 'tyrese is a cool' in lowered:
        return 'He is indeed'
    
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    
    elif 'coin flip' in lowered:
        return f'The coin landed on: {choice(["heads", "tails"])}'

    elif 'guess number' in lowered:
        number = randint(1, 10)
        return f'Guess a number between 1 and 10. I am thinking of {number}. Try to guess it!'

    if '?' in lowered:
        return 'That\'s an interesting question. Let me see if I can help you with that.'

    random_responses = [
        'I\'m not sure how to respond to that. Can you please clarify or ask another question?',
        'That\'s a good one! Can you tell me more?',
        'Hmm, I\'m not quite sure. Let\'s try something else!',
        'I\'m a bit confused by that. Could you rephrase it?',
        'Interesting! What else can I help with?',
        'I\'m not programmed to understand that just yet. Can you ask another way?',
        'I wish I knew the answer to that. Maybe try asking something different?',
        'Good question! Unfortunately, I don\'t have the answer.',
        'I\'m stumped! How about asking something else?',
        'Let\'s talk about something else. What\'s on your mind?'
    ]

    return choice(random_responses)

