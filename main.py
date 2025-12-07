from dotenv import load_dotenv
load_dotenv()

import os
import asyncio
import logging
from typing import Final
from discord import Intents, Client, Message

from core.server_scenarios import get_scenario
import core.ai as ai 

# Logging
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

# Discord setup
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKEN not found in .env file")

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

COMMAND_PREFIX: Final[str] = "?wgp"

# Message handling
async def send_message(message: Message, user_question: str) -> None:
    user_question = user_question[len(COMMAND_PREFIX):].strip()
    if not user_question:
        await message.channel.send("You must include a question after `?wgp`.")
        return

    # AI command
    if user_question.lower().startswith("ai "):
        prompt = user_question[3:].strip()
        if not prompt:
            await message.channel.send("Please provide a prompt after `?wgp ai`.")
            return

        loop = asyncio.get_running_loop()
        answer = None
        responder = None

        try:
            answer, responder = await loop.run_in_executor(None, ai.ask_ai, prompt)
        except Exception:
            answer = None

     

        if not answer:
            await message.channel.send("Both AI services are unavailable. Try again later.")
            return

       
     
        personality = f"{answer}"
        await message.channel.send(personality)
        logging.info(f"AI reply sent in {message.channel} to {message.author} using {responder}")
        return

    # Rule-based / hybrid
    try:
        response: str = get_scenario(user_question)
        await message.channel.send(response)
        logging.info(f"Sent response in {message.channel} to {message.author}")
    except Exception as e:
        logging.error(f"Error while handling message: {e}")
        try:
            await message.channel.send("Sorry, something went wrong while processing your request.")
        except Exception:
            pass

# Discord events
@client.event
async def on_ready():
    logging.info(f"Logged in as {client.user}")

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    content = message.content.strip()
    if not content.startswith(COMMAND_PREFIX):
        return

    logging.info(f"[Command] {message.author}: '{content}'")
    await send_message(message, content)

# Entry point
def main() -> None:
    logging.info("Starting Discord bot...")
    client.run(TOKEN)

if __name__ == "__main__":
    main()
