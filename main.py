import os

from discord.ext import commands
from player import Music
from kasino import Kasino

client = commands.Bot(command_prefix=['-', ''], description='Yet another music client.')
client.add_cog(Music(client))
client.add_cog(Kasino(client))

@client.event
async def on_ready():
	print('Logged in as {0.user}!'.format(client))

	# Canal do KASINO
	# await client.get_channel(887381114124136461).connect()

# #
# Inicializar o bot
# #

try:
	alive = os.environ['alive']
	if alive is not None:
		from utils.keepalive import keep_alive
		keep_alive()
except:
	pass

client.run(os.getenv("TOKEN"))
