import discord
from discord.ext import commands, tasks
import os
from datetime import datetime
import json
from dotenv import load_dotenv
import urllib.request
import asyncio
import schedule, time #libreria time para el sleep, schedule para hacer el evento una vez al dia
import pytz #libreria para la timezone de todo el mundo
import pandas as pd #libreria para leer el excel
import xlwt

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #token de discord

tz_bsas = pytz.timezone('America/Argentina/Buenos_Aires') #timezone de argentina
bot = commands.Bot(command_prefix='!') #prefijo de comando

#Comandos del bot
@bot.event
async def on_ready():
        await bot.change_presence(activity=discord.Game(name="Hecho con amor"),status=discord.Status.online)
    

@bot.command()
async def start(ctx):
    while True:
        datetime_bsas = datetime.now(tz_bsas) #guarda la hora de bsas
        hora = datetime_bsas.strftime("%d/%m/%Y:%H:%M") #formatea la hora y la guarda en la variable hora

        print(hora,"hora actual")
        xls = pd.read_excel("horarios.xls", sheet_name="Hoja 1", )
        c=-1
        for col in xls["Dia"]:
            c = c+1
            print(col)
            if str(col) == hora:
                await ctx.send("Hoy hay zoom de: " + str(xls.at[c,"Materia"]))
        await asyncio.sleep(60)

@bot.command()
async def startt(ctx):
    
    while True:
        datetime_bsas = datetime.now(tz_bsas) #guarda la hora de bsas
        hora = datetime_bsas.strftime("%d/%m/%Y:%H:%M") #formatea la hora y la guarda en la variable hora
        #AL FORMATO HAY QUE AÑADIRLE LOS SEGUNDOS ASI NO ESTA TODO EL MINUTO ENTERO ENVIANDO EL MENSAJE HACER ESTO ES LO PROXIMO
        #POR AHORA ESTA ES LA FUNCIÓN QUE ESTOY EDITANDO, ESTA IGUAL A "start", SOLO POR LO COMENTADO ARRIBA. LO QUE FALTA ES 
        #ACTUALIZAR EL EXCEL UNA VEZ QUE HAYA MANDADO EL MENSAJE. LO ESTOY INTENTANDO EN ./test.py
        print(hora,"hora actual")
        xls = pd.read_excel("horarios.xls", sheet_name="Hoja 1", )
        c=-1
        for col in xls["Dia"]:
            c = c+1
            print(col)
            if str(col) == hora:
                v=1
                await ctx.send("@everyone Hoy hay zoom de: " + str(xls.at[c,"Materia"])+" a las: " + str(xls.at[c,"Hora"]))
                
                
                fecha = xls.at[c,"Dia"]
                fecha_obj = datetime.strptime(fecha,"%d/%m/%Y:%H:%M")
                xls.at[c,"Dia"] = datetime.strftime(fecha_obj + pd.Timedelta("2 W"),"%d/%m/%Y:%H:%M")
                xls = pd.DataFrame(xls)
                xls.to_excel('horarios.xls', sheet_name='Hoja 1', index=False)
                #await asyncio.sleep(60) #el await esta para, ademas de que no este todo el minuto
                                        #enviando  el mensaje "Hoy hay zoom de..." (porque la comprobación en el if es por minuto, o sea que estaría todo un minuto
                                        # con el if diciendo HAY UN HORARIO EN EL EXCEL QUE COINCIDE CON LA HORA ACTUAL, entonces sirve para detenerlo y que solamente
                                        # de una vuelta, enviando un mensaje unico) sirve para darle tiempo a las demas funciones de que hagan lo que tengan que hacer, 
                                        #como el evento on_ready, sino el bot aparece desconectado. luego del await (ya con el minuto pasado), vuelve a funcionar el while
                                        #revisando el excel a ver si hay un horario
                                        #Nota: Esto podría ser mas eficiente si se hiciera que el bot revise el excel una vez por dia unicamente. Pero hay que ejecutarlo 
                                        # a las 00:00 y no tuve ganas de esperar hasta ese horario, pero solamente bastaría con añadir otro wait asyncio con el tiempo de
                                        # 86340 segundos (un dia - el minuto que esta el sleep en el for)
        await asyncio.sleep(20)

@bot.command()
async def gptd(ctx):
    await ctx.send("pong")

bot.run(TOKEN)