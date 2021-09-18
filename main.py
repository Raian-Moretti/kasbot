import os
import discord

from discord.ext import commands
from player import Music
from kasino import Kasino

client = commands.Bot(command_prefix=['-', ''], description='Yet another music client.')
music = Music(client)
kasino = Kasino(client)
client.add_cog(music)
client.add_cog(kasino)

kasino_commands = []
for cmd in kasino.get_commands():
	kasino_commands.append(cmd.name)

@client.event
async def on_ready():
	print('Logged in as {0.user}!'.format(client))

	# Canal do KASINO
	# await client.get_channel(887381114124136461).connect()

@client.event
async def on_message(message: discord.Message):
	# Verifica se é um comando ou não
	if message.content in kasino_commands or message.content.startswith('-'):
		await client.process_commands(message)

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
