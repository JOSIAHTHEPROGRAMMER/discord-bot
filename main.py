from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import logging

from server_scenarios import get_scenario

# ------------------------------
# Logging setup
# ------------------------------
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

# ------------------------------
# Load environment variables
# ------------------------------
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("DISCORD_TOKEN not found in .env file")

# ------------------------------
# Discord client setup
# ------------------------------
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Command prefix
COMMAND_PREFIX: Final[str] = "?wgp"


# ------------------------------
# Message handling
# ------------------------------
async def send_message(message: Message, user_question: str) -> None:
    """Handles a valid ?wgp command and sends a PUBLIC response."""
    try:
        # Remove the prefix and any extra spaces
        user_question = user_question[len(COMMAND_PREFIX):].strip()

        if not user_question:
            await message.channel.send("You must include a question after `?wgp`.")
            return

        # Get the scenario response
        response: str = get_scenario(user_question)

        # Send response in the same channel
        await message.channel.send(response)
        logging.info(f"Sent response in {message.channel} to {message.author}")

    except Exception as e:
        logging.error(f"Error while handling message: {e}")
        try:
            await message.channel.send("Sorry, something went wrong while processing your request.")
        except Exception:
            pass


# ------------------------------
# Discord event handlers
# ------------------------------
@client.event
async def on_ready():
    logging.info(f"Logged in as {client.user}")


@client.event
async def on_message(message: Message) -> None:
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    content = message.content.strip()

    # Only respond to messages starting with ?wgp
    if not content.startswith(COMMAND_PREFIX):
        return  # ignore everything else

    logging.info(f"[Command] {message.author}: '{content}'")
    await send_message(message, content)


# ------------------------------
# Entry point
# ------------------------------
def main() -> None:
    logging.info("Starting Discord bot...")
    client.run(TOKEN)


if __name__ == "__main__":
    main()
