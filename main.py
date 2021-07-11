import os
import time
import discord
from stream import Stream
from discord.ext import commands
from dotenv import load_dotenv; load_dotenv()

s = Stream(token)
token = os.getenv("token")
bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
	print('Ready')


@bot.command()
async def p(ctx):
	voice = ctx.message.author.voice

	if ctx.message.author.voice is None:
		return await ctx.send('You need to be in a voice channel to use this command')

	url = ctx.message.content.split()[1]
	print(voice)


bot.run(token)


# s.load_video("./tmp/video")
# s.open_guild()
# s.join()
# s.start()
# s.play()

# time.sleep(20)

# s.pause()
# s.stop()