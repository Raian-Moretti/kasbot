import discord
import asyncio
from discord.ext import commands

class Kasino(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='kasino')
    async def _kasino(self, ctx: commands.Context):
        await self.play_song("./mp3/sabadaco.mp3", ctx.message.author)
        await ctx.message.delete()

    @commands.command(name='shake it')
    async def _shake_it(self, ctx: commands.Context):
        await self.play_song("./mp3/shake it.mp3", ctx.message.author)
        await ctx.message.delete()

    @commands.command(name='jet music')
    async def _jet_music(self, ctx: commands.Context):
        await self.play_song("./mp3/jet music.mp3", ctx.message.author)
        await ctx.message.delete()

    @commands.command(name='companhia', aliases=['compania'])
    async def _companhia(self, ctx: commands.Context):
        voice_channel = ctx.message.author.voice
        if voice_channel == None:
            return

        voice_channel = voice_channel.channel
        await voice_channel.connect()
        await ctx.message.delete()

    @commands.command(name='pare')
    async def _pare(self, ctx: commands.Context):
        voice_channel = ctx.message.author.voice
        if voice_channel == None:
            return

        voice_clients = self.client.voice_clients
        for vc in voice_clients:
            if vc.channel == voice_channel.channel:
                await vc.disconnect()
                break

        # Delete command after action is done.
        await ctx.message.delete()

    async def play_song(self, filename: str, author: discord.Member):
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