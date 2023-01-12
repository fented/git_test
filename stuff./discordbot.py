import discord
from discord.ext import commands

TOKEN = ''

intents = discord.Intents()

client = commands.Bot(command_prefix='cat.', intents=intents)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
