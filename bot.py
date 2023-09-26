import os
import discord
from discord.ext import commands
from config import get_config



class BotDiscord(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(
            command_prefix='!',
            intents=intents,
            help_command=None
        )

    async def load_cogs(self) -> None:
        for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
            if file.endswith(".py"):
                extension = file[:-3]
                try:
                    await self.load_extension(f"cogs.{extension}")
                    print(f"Loaded extension '{extension}'")
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    print(f"Failed to load extension {extension}\n{exception}")

    async def setup_hook(self) -> None:
        """
        The code in this function is executed whenever the bot will start.
        """
        await self.load_cogs()

if __name__ == '__main__':
    bot = BotDiscord()
    bot.run(get_config().DISCORD_TOKEN)



