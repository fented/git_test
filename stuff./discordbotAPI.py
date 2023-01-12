import discord
from discord.ext import commands

TOKEN = 'MTA2MjAxMDExNTc5Mzg4MzIyNA.GFRItA.L0yqQyr1AzF-DVHm_zTu7mp6o6lryNpKDsKLDo'

intents = discord.Intents()

client = commands.Bot(command_prefix='cat.', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def hello(ctx):
    channel = client.get_channel(1052222737092968473)

    await channel.send(f'hello there {ctx.author.mention}')
#####
#####
## Insert other functions here
#####
#####



client.run(TOKEN)


