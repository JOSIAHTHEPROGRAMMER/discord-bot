# WGP Discord Bot

A friendly Discord bot that can chat, tell jokes, play simple games, and respond to user commands.

## Features

- Responds to greetings and common questions.
- Provides random jokes from [JokeAPI](https://v2.jokeapi.dev/).
- Plays mini-games like dice rolls, coin flips, and guessing numbers.
- Handles simple conversational scenarios.
- Can be extended with more commands and features in the future.

## Requirements

- Python >= 3.11
- `discord.py` library
- `requests` library
- `python-dotenv` library

## Installation

### 1. Clone the repository:  

```bash
git clone https://github.com/JOSIAHTHEPROGRAMMER/discord-bot.git
cd wgp-discord-bot
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Create a .env file in the project root and add your Discord bot token:

```ini
DISCORD_TOKEN=your_bot_token_here
```

### 4. Usage

#### Run the bot locally with:

```bash
python bot.py
```

#### The bot will respond to messages starting with the command prefix:

```php-template
?wgp <your message>
```
#### Example commands:
![Example test](images/example.jpg)



###  Notes
>Running locally means the bot will only be online while your machine is running.

>This bot is actively maintained and will receive updates in the future with new features and improvements.
