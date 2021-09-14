import os
import discord
import time

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
		voice_channel = message.author.voice.channel

		if voice_channel != None:
			vc = await voice_channel.connect()
			vc.play(discord.FFmpegPCMAudio(source="sabadaco.mp3"))
			
			# Sleep while audio is playing.
			while vc.is_playing():
				time.sleep(.1)
			await vc.disconnect()
		else:
			await message.send(str(message.author.name) + "is not in a channel.")

		# Delete command after the audio is done playing.
		await message.message.delete()

client.run(TOKEN)
