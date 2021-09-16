import os
import discord
import asyncio

TOKEN = os.environ['token']

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as {0.user}!'.format(client))

@client.event
async def on_message(message: discord.Message):
	if message.author == client.user:
		return

	if message.content == 'kasino':
		voice_channel = message.author.voice
		await play_song("./mp3/sabadaco.mp3", voice_channel)

		# Delete command after the audio is done playing.
		await message.delete()

	elif message.content == 'shake it':
		voice_channel = message.author.voice
		await play_song("./mp3/shake it.mp3", voice_channel)

		# Delete command after the audio is done playing.
		await message.delete()

	elif message.content == 'jet music':
		voice_channel = message.author.voice
		await play_song("./mp3/jet music.mp3", voice_channel)

		# Delete command after the audio is done playing.
		await message.delete()

	elif message.content in ['compania', 'companhia']:
		voice_channel = message.author.voice
		await message.delete()

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

		await message.delete()

async def play_song(filename: str, voice_channel: discord.VoiceState):
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
