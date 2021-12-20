from bot.bot import Bot
from bot.constants import Config
from bot.exts import walk_extensions

bot = Bot()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

for ext in walk_extensions():
    bot.load_extension(ext)

bot.run(Config.token)
