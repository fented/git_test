import discord
from discord import app_commands
import os
import requests

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = 1052222737092968469))
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)


# Test Command
file_path = os.path.join('D:', 'Documents', 'VS Code Scripts', 'Bot try 2', 'Cat Api.py')

@tree.command(name="test", description="testing", guild=discord.Object(id=1052222737092968469))
async def self(interation: discord.Interaction):
    await interation.response.send_message(f"Working")

@client.event
async def on_message(message):
    if message.content.startswith('!cat'):
        api_key = ""
        # Get API key from: https://thecatapi.com/

        def ajax_get(url):
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                except ValueError as err:
                    print(err.message + " in " + response.text)
                    return
                return data

        data = ajax_get('https://api.thecatapi.com/v1/images/search?size=full')
        if data:
            url = data[0]["url"]
            await message.channel.send(url)

client.run('')
