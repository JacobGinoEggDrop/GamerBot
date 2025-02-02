import discord
from discord.ext import commands
from URLReader import URLReader

import random

token = open("token.txt", "r").read()

PREFIX = '-g '

client = commands.Bot(command_prefix = PREFIX)

def begins(text, start):
    return text.content.lower().startswith(PREFIX+start)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    
    if begins(message, 'ping'):
        await message.channel.send(f'Pong! {round(client.latency * 1000)}ms')

    if begins(message, 'typerace'):
        words = message.content.split()

        if len(words)<3:
            await message.channel.send('https://www.nitrotype.com/race/'+message.author.name)
            return

        await message.channel.send('https://www.nitrotype.com/race/'+words[2])

    if begins(message, 'chess'):
        words = message.content.split()
        await message.channel.send('https://www.chess.com/play/'+words[2])

    if begins(message, 'dice'):
        words = message.content.split()

        if len(words) < 3:
            await message.channel.send(str(int(random.random()*6)+1))
            return

        if words[2].isnumeric() and int(words[2])>=2 and int(words[2])<=1000000:
            await message.channel.send(str(int(random.random()*int(words[2]))+1))
            return

        await message.channel.send('Give number of sides [2, 1000000]')

client.run(token)
