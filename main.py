import os
import discord
import time
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

TOKEN = os.environ['token']

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as {0.user}!'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('kasino'):
		voice_channel = message.author.voice

		if voice_channel != None:
			voice_channel = voice_channel.channel
			vc = await voice_channel.connect()
			vc.play(discord.FFmpegPCMAudio(source="sabadaco.mp3"))

			# Sleep while audio is playing.
			while vc.is_playing():
				await asyncio.sleep(0.3)
			await vc.disconnect()

		# Delete command after the audio is done playing.
		await message.delete()

	if message.content.startswith('shake it'):
		voice_channel = message.author.voice

		if voice_channel != None:
			voice_channel = voice_channel.channel
			vc = await voice_channel.connect()
			vc.play(discord.FFmpegPCMAudio(source="shake it.mp3"))

			# Sleep while audio is playing.
			while vc.is_playing():
				await asyncio.sleep(0.3)
			await vc.disconnect()

		# Delete command after the audio is done playing.
		await message.delete()

	if message.content.startswith('jet music'):
		voice_channel = message.author.voice

		if voice_channel != None:
			voice_channel = voice_channel.channel
			vc = await voice_channel.connect()
			vc.play(discord.FFmpegPCMAudio(source="jet music.mp3"))

			# Sleep while audio is playing.
			while vc.is_playing():
				await asyncio.sleep(0.3)
			await vc.disconnect()

		# Delete command after the audio is done playing.
		await message.delete()

client.run(TOKEN)
