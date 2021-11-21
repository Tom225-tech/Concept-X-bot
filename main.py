import discord
import os
import datetime
import pytz
from discord.ext import tasks
from alive import keep_alive
from itertools import cycle

client = discord.Client(activity=discord.Game(name='my game'))

activity = discord.Activity(name='Math', type=discord.ActivityType.playing)
client = discord.Client(activity=activity)
status = cycle(['Math', 'FLE', 'Amath', 'PhysX', 'Chemistry', 'CS'])

dt = datetime.datetime.now(tz=pytz.UTC)
mmtime = dt.astimezone(pytz.timezone('Asia/Rangoon'))
format = int(mmtime.strftime('%H'))
channel = client.get_channel("901148149169659937")


@client.event
async def on_ready():
    change_status.start()
    print('We have logged in as {0.user}'.format(client))


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!day'):
        dt = datetime.datetime.now(tz=pytz.UTC)
        mmtime = dt.astimezone(pytz.timezone('Asia/Rangoon'))
        format = mmtime.strftime(' %B %d, %Y')
        await message.channel.send(format)

    if message.content.startswith('!help'):

        embed = discord.Embed(title='Welcome From ConceptX',
                              description='This is a description',
                              colour=discord.Color.blue())

        embed.set_footer(text='This is a footer')
        embed.set_image(
            url=
            'https://cdn.discordapp.com/attachments/907658039849525269/908981906878652446/8DwdtAoUC9ItYAAAAASUVORK5CYII.png'
        )
        embed.set_thumbnail(
            url=
            'https://cdn.discordapp.com/attachments/907658039849525269/908993989259173938/images.png'
        )

        await message.author.send(embed=embed)

    if message.content.startswith('!time'):
        dt = datetime.datetime.now(tz=pytz.UTC)
        mmtime = dt.astimezone(pytz.timezone('Asia/Rangoon'))
        time = mmtime.strftime('%H:%M')
        await message.channel.send(time)


keep_alive()
client.run(os.getenv('TOKEN'))
