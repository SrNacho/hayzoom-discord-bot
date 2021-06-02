import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import excel_rw

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #token de discord
bot = commands.Bot(command_prefix='!') #prefijo de comando
embed = discord.Embed()
ID_CANAL_AVISOS = os.getenv('ID_CANAL_AVISOS')
ID_CANAL_COMANDO_FECHAS = os.getenv('ID_CANAL_COMANDO_FECHAS')

#Evento onready (cuando el bot se inicia)
@bot.event
async def on_ready():
    channel = bot.get_channel(ID_CANAL_AVISOS)
    await bot.change_presence(activity=discord.Game(name="!fechas"),status=discord.Status.online)
    while True:
        startt = excel_rw.start() #si no devuelve nada almacena objeto tipo NoneType
        try:
            if startt[0] == 200:
                await channel.send("@everyone Hoy hay zoom de: " + startt[1] + " a las: " + startt[2])
        except:
            pass
        await asyncio.sleep(20)

#Comandos del bot
@bot.command()
async def gptd(ctx):
    await ctx.send("pong")

@bot.command()
async def fechas(ctx):
    channel = bot.get_channel(ID_CANAL_COMANDO_FECHAS)
    await channel.send("```ruby\n{}```".format(excel_rw.getDates()))
    pass


bot.run(TOKEN)