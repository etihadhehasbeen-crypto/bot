import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
  print(f'ล็อกอินสำเร็จในชื่อ: {bot.user}')
  await bot.change_presence(
      activity=discord.Game(name='ออนไลน์ 24 ชม. | พิมพ์ !ping')
  )


@bot.command()
async def ping(ctx):
  await ctx.send(f'Pong! ความหน่วง {round(bot.latency * 1000)}ms')


keep_alive()

TOKEN = os.environ.get('DISCORD_TOKEN')
bot.run(TOKEN)