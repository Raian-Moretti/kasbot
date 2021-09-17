import os
import discord
import asyncio

TOKEN = os.environ['token']

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as {0.user}!'.format(client))

	# Canal do KASINO
	await client.get_channel(887381114124136461).connect()

@client.event
async def on_message(message: discord.Message):
	if message.author == client.user:
		return

	if message.content == 'kasino':
		await play_song("./mp3/sabadaco.mp3", message.author)

	elif message.content == 'shake it':
		await play_song("./mp3/shake it.mp3", message.author)

	elif message.content == 'jet music':
		await play_song("./mp3/jet music.mp3", message.author)

	elif message.content in ['compania', 'companhia']:
		voice_channel = message.author.voice
		if voice_channel == None:
			return

		voice_channel = voice_channel.channel
		await voice_channel.connect()

	elif message.content == 'pare':
		voice_channel = message.author.voice
		if voice_channel == None:
			return

		voice_clients = client.voice_clients
		for vc in voice_clients:
			if vc.channel == voice_channel.channel:
				await vc.disconnect()
				break

	# Delete command after action is done.
	await message.delete()

async def play_song(filename: str, author: discord.Member):
	voice_channel = author.voice
	if voice_channel == None:
		return

	voice_channel = voice_channel.channel
	voice_client = await voice_channel.connect()
	voice_client.play(discord.FFmpegPCMAudio(source=filename))

	# Sleep while audio is playing, then disconnect
	while voice_client.is_playing() and voice_client.is_connected():
		await asyncio.sleep(0.3)
	await voice_client.disconnect()


# #
# Inicializar o bot
# #

try:
	alive = os.environ['alive']
	if alive is not None:
		from keepalive import keep_alive
		keep_alive()
except:
	pass

client.run(TOKEN)
