import discord
import os
import random


import time

from time import sleep
from keep_alive import keep_alive
from discord.ext import commands
import discord.utils
from discord.utils import get
from discord.ext.commands import Bot

import asyncio
from datetime import datetime



client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)



 # This must be exactly the name of the appropriate role


@client.event
async def on_message(message):
  whe = "-p"
  whee = "-play "
  mr = random.randint(1, 2)
  if (whe in message.content or whee in message.content) and (mr == 1):
    wher = random.randint(1, 2)
    if wher == 1:
      await message.channel.send("I don't like that song")
    else:
      await message.channel.send("I like that song")
  if message.content == "lm" or message.content == "llamas with hats":
    await message.delete()
    await message.channel.send(f"https://www.youtube.com/watch?v=jJOwdrTA8Gw")
    await message.channel.send(f"{message.author.name} that kills people!")

  wh = "what are you"
  if (wh in message.content):
    sleep(2)
    if message.content == "what are you doing?":
      wd = random.randint(1, 2)
      if wd == 1:
        await message.channel.send("Talking to you stupid")
      else:
        await message.channel.send("Doing unspeakable things")

    elif message.content == "what are you playing?":
      wp = random.randint(1, 2)
      if wp == 1:
        await message.channel.send("This game called life where you always lose")
      else:
        await message.channel.send("Hollow Knight")
      
    elif message.content == "what are you killing?":
      wk = random.randint(1, 40)
      if wk == 1:
        await message.channel.send("Absolute Radience")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763512107437129749/latest.png")
      elif wk == 2:
        await message.channel.send("Pure Radience")

      elif wk == 3:
        await message.channel.send("Vengfly king")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510282894180353/latest.png")
      elif wk == 4:
        await message.channel.send("Gruz Mother")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510332625911828/latest.png")
      elif wk == 5:
        await message.channel.send("False Knight")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510370055880714/310.png")
      elif wk == 6:
        await message.channel.send("Massive Moss Charger (aka: the bush)")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510405335089182/310.png")
      elif wk == 7:
        await message.channel.send("Hornet")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510477132791843/310.png")
      elif wk == 8:
        await message.channel.send("Gorb")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510516055801906/latest.png")
      elif wk == 9:
        await message.channel.send("Dung Defender")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510560146194472/310.png")
      elif wk == 10:
        await message.channel.send("Brooding Mawlek")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510624692338718/310.png")
      elif wk == 11:
        await message.channel.send("Brothers Oro & Mato")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510664118665236/310.png")
      elif wk == 12:
        await message.channel.send("Xero")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510696808808448/310.png")
      elif wk == 13:
        await message.channel.send("Crystal Guardian")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510731664523294/latest.png")
      elif wk == 14:
        await message.channel.send("Soul Master")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510761606610964/310.png")
      elif wk == 15:
        await message.channel.send("The oblobbles")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510793886892032/310.png")
      elif wk == 16:
        await message.channel.send("Sisters of Battle")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511164461252618/latest.png")
      elif wk == 17:
        await message.channel.send("Marmu")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511224599052329/310.png")
      elif wk == 18:
        await message.channel.send("Flukemarm")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511260314206218/latest.png")
      elif wk == 19:
        await message.channel.send("Broken Vessel")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511298461007882/latest.png")
      elif wk == 20:
        await message.channel.send("Galien")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511346209488946/latest.png")
      elif wk == 21:
        await message.channel.send("Paintmaster Sheo")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511384197169213/310.png")
      elif wk == 22:
        await message.channel.send("Hive knight")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511434561978388/latest.png")
      elif wk == 23:
        await message.channel.send("Elder Hu")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511465474392144/latest.png")
      elif wk == 24:
        await message.channel.send("The collector")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511496365441034/310.png")
      elif wk == 25:
        await message.channel.send("God Tamer")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511526506102824/310.png")
      elif wk == 26:
        await message.channel.send("Troupe Master Grimm")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511571950338098/latest.png")
      elif wk == 27:
        await message.channel.send("Watcher Knight")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511610152452136/310.png")
      elif wk == 28:
        await message.channel.send("Uumuu")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511646810800148/310.png")
      elif wk == 29:
        await message.channel.send("Winged Nosk")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511768844468244/310.png")
      elif wk == 30:
        await message.channel.send("Great Nailsage Sly")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511809172045825/latest.png")
      elif wk == 31:
        await message.channel.send("No eyes")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511858731941908/310.png")
      elif wk == 32:
        await message.channel.send("Traitor Lord")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511900335505408/310.png")
      elif wk == 33:
        await message.channel.send("Markoth")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763511972154048522/310.png")
      elif wk == 34:
        await message.channel.send("Grey Prince Zote")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763512002101641216/310.png")
      elif wk == 35:
        await message.channel.send("Failed Champion")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763510370055880714/310.png")
      elif wk == 36:
        await message.channel.send("Nightmare King Grim")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763512037229461504/310.png")
      
      else:
        await message.channel.send("Pure Vessel")
        await message.channel.send("https://cdn.discordapp.com/attachments/685347130373570611/763512068485677107/latest.png")

    elif message.content == "what are you eating?":
      we = random.randint(1, 4)
      if we == 1:
        await message.channel.send("retarded fish")
      elif we == 2:
        await message.channel.send("Spoiled rat")
      elif we == 3:
        await message.channel.send(f"@ThatGuy")
        await message.channel.send("pls search")
        sleep(3)
        await message.channel.send("air")
      else:
        await message.channel.send("your face")
      
    else:
      await message.channel.send("Nothing")
    sleep(2)
    rrand = random.randint(1, 4)
    if rrand == 1:
      response = "retard"
    elif rrand == 2:
      response = "awesome"
    elif rrand == 3:
      response = "dead"
    elif rrand == 4:
      response = "destroying something"
    else:
      response = "cranking it"
    await message.channel.send(f"Are you {response}?")
  



keep_alive()

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)

#interact.teststuff()