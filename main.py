import discord
import os
import requests
import random
# from discord import Game
import json
from discord.ext import commands
from discord import Intents
import giphy_client
from giphy_client.rest import ApiException
from keep_alive import keep_alive
import asyncio
import datetime
import pytz
from discord import guild
import datetime
import editdistance
import re
# from tinydb import TinyDB, Query
from discord.ext.commands import Bot
from urllib.parse import urlparse
# import httpx

import logging

intents = Intents.default()
intents.members = True
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
from random import choice

client = commands.Bot(command_prefix=commands.when_mentioned_or("."),
                      description="A Multipurpose discord  bot.",
                      intents=intents)
client.remove_command("help")


@client.event
async def on_ready():
    print('bot is ready.')


##quotes


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n-" + json_data[0]['a']

    return (quote)


@client.command()
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)


@client.event
async def on_message(message):
    if message.mention == client.user:
        await ctx.send("My prefix is ' . '}")


##some commands
@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title="Help",
        description=
        "Use .help <command> for extended information on that command.",
        color=ctx.author.color)
    em.add_field(
        name="weather",
        value="This command gives you the weather report of a particular place."
    )
    em.add_field(name="gif",
                 value="This command shows the gif that you desire .")
    em.add_field(
        name="avatar",
        value="This command shows you the avater of any member in the server.")
    em.add_field(name="ping", value="This command shows ping of the server .")
    em.add_field(
        name="snipe",
        value="This command shows the recently deleted message in the server.")
    em.add_field(name="fun", value="kiss,hug,pat,spank,coinflip")
    em.add_field(
        name="server info",
        value=
        "This command gives you everything that you want to know about this server."
    )
    em.add_field(
        name="user info",
        value="This command gives you some details about the particluar person."
    )

    await ctx.send(embed=em)


@help.command()
async def weather(ctx):
    em = discord.Embed(title="Weather", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=".w <city>")
    await ctx.send(embed=em)


@help.command()
async def gif(ctx):
    em = discord.Embed(title="GIF", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=".gif <name of gif>")
    await ctx.send(embed=em)


@help.command()
async def avatar(ctx):
    em = discord.Embed(title="Avatar", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=".av <mention a user>")
    await ctx.send(embed=em)


@help.command()
async def ping(ctx):
    em = discord.Embed(title="Ping", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=".ping")
    await ctx.send(embed=em)


@help.command()
async def snipe(ctx):
    em = discord.Embed(title="Snipe", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=".snipe")
    await ctx.send(embed=em)


@help.command()
async def kiss(ctx):
    em = discord.Embed(title="Kiss", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=".kiss <mention a member>")
    await ctx.send(embed=em)


@help.command()
async def hug(ctx):
    em = discord.Embed(title="Hug", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=".hug <mention a member>")
    await ctx.send(embed=em)


@help.command()
async def pat(ctx):
    em = discord.Embed(title="Pat", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=".pat <mention a member>")
    await ctx.send(embed=em)


@help.command()
async def spank(ctx):
    em = discord.Embed(title="Spank", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=".spank <mention a member>")
    await ctx.send(embed=em)


@help.command()
async def serverinfo(ctx):
    em = discord.Embed(title="SERVER INFO", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=".serverinfo ")
    await ctx.send(embed=em)


@help.command()
async def userinfo(ctx):
    em = discord.Embed(title="User Info", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=".userinfo <mention a member>")
    await ctx.send(embed=em)


@help.command()
async def coinflip(ctx):
    em = discord.Embed(title="Coin Flip", color=ctx.author.color)
    em.add_field(name="**Syntax**", value=".coinflip")
    await ctx.send(embed=em)


@client.command()
async def hello(ctx):
    await ctx.send(f"Hello!{ctx.author.mention}")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! : {round(client.latency*1000)}ms")


@client.command()
async def namaste(ctx):
    await ctx.send('Namaste!')


@client.event
async def on_message(message):
    print('A use has sent a message.')
    await client.process_commands(message)


import random
from random import choice

determine_flip = [1, 0]


@client.command()
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(
            title="Coinflip | NAMASTE",
            description=f"{ctx.author.mention} Flipped coin, we got **Heads**!"
        )
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title="Coinflip | NAMASTE",
            description=f"{ctx.author.mention} Flipped coin, we got **Tails**!"
        )
        await ctx.send(embed=embed)


##poll


@client.command()
async def poll(ctx, *, message):
    emb = discord.Embed(title="POLL", description=f"{message}")
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction('1️⃣')
    await msg.add_reaction('2️⃣')


##gif


@client.command()
async def gif(ctx, *, q="random"):

    api_key = os.getenv("API")
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key,
                                                    q,
                                                    limit=5,
                                                    rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q, )
        emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


##welcomer


@client.event
async def on_member_join(member):

    embed = discord.Embed(
        title="स्वागत छ !  🎉  ",
        description=
        f"✨  {member.name} तिमिलाई   ✨ \n ━━━\n- Be sure to check out <#782155999913050133>  and <#779973925680840734> \n- Introduce yourself in <#845184842194354206>\n- BUT most importantly have fun ^^"
    )
    embed.set_footer(text="🙏 NAMASTE !")
    embed.set_thumbnail(url=member.avatar_url)
    await member.guild.get_channel(779974983626784780).send(
        f"{member.mention} | <@&887336192423628800>", embed=embed)


#weather

api_key = os.getenv("WAPI")
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@client.command()
async def w(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel

    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(
                round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            embed = discord.Embed(
                title=f"Weather in {city_name}",
                color=ctx.guild.me.top_role.color,
                timestamp=ctx.message.created_at,
            )
            embed.add_field(name="Descripition",
                            value=f"**{weather_description}**",
                            inline=False)
            embed.add_field(name="Temperature(C)",
                            value=f"**{current_temperature_celsiuis}°C**",
                            inline=False)
            embed.add_field(name="Humidity(%)",
                            value=f"**{current_humidity}%**",
                            inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)",
                            value=f"**{current_pressure}hPa**",
                            inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
        await channel.send(embed=embed)
    else:
        await channel.send("City not found.")


tz = pytz.timezone("Asia/Kathmandu")


##@client.event
##async def on_ready():
#await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Luki Dum"))
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # Ensure you create the task inside an asynchronous context
    async def change_presence():
        await client.wait_until_ready()

        statuses = [
            ".help | Namaste",
            "Luki Dum",
        ]

        while not client.is_closed():
            status = random.choice(statuses)
            await client.change_presence(activity=discord.Game(name=status))
            await asyncio.sleep(5)

    client.loop.create_task(change_presence())

#avater


@client.command()
async def av(ctx, user: discord.User = None):

    if not user:
        user = ctx.author

    embed = discord.Embed(title=f"{user.name}'s Avatar",
                          description="Awww so cute",
                          color=ctx.author.color)
    embed.set_image(url=user.avatar_url)

    await ctx.send(embed=embed)


@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send('Joined 👌')


# # command to play sound from a youtube URL
# @client.command()
# async def play(ctx, url):
#     channel = ctx.message.author.voice.channel
#     voice = get(client.voice_clients, guild=ctx.guild)
#     if voice and voice.is_connected():
#         await voice.move_to(channel)
#     else:
#         voice = await channel.connect()
#     YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
#     FFMPEG_OPTIONS = {
#         'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
#     voice = get(client.voice_clients, guild=ctx.guild)

#     if not voice.is_playing():
#         with YoutubeDL(YDL_OPTIONS) as ydl:
#             info = ydl.extract_info(url, download=False)
#         URL = info['url']
#         voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
#         voice.is_playing()
#         await ctx.send('Music is playing 🎶')

# # check if the bot is already playing
#     else:
#         await ctx.send("Music is already playing 🎶")
#         return

# # command to resume voice if it is paused
# @client.command()
# async def resume(ctx):
#     voice = get(client.voice_clients, guild=ctx.guild)

#     if not voice.is_playing():
#         voice.resume()
#         await ctx.send('Music is resuming ⏯')

# # command to pause voice if it is playing
# @client.command()
# async def pause(ctx):
#     voice = get(client.voice_clients, guild=ctx.guild)

#     if voice.is_playing():
#         voice.pause()
#         await ctx.send('Music has been paused ▶')

# # command to stop voice
# @client.command()
# async def stop(ctx):
#     voice = get(client.voice_clients, guild=ctx.guild)

#     if voice.is_playing():
#         voice.stop()
#         await ctx.send('Stopped 🛑')

# # @client.command()
# # async def dc(ctx):
# #     channel = ctx.message.author.voice.channel
# #     voice = get(client.voice_clients, guild=ctx.guild)
# #     await voice.disconnect()
# #     await ctx.send('disconnected 👋')

# snipe_message_author = {}
# snipe_message_content = {}

# @client.event
# async def on_message_delete(message):
#      snipe_message_author[message.channel.id] = message.author
#      snipe_message_content[message.channel.id] = message.content
#      await asyncio.sleep(60)
#      del snipe_message_author[message.channel.id]
#      del snipe_message_content[message.channel.id]

# @client.command(name = 'snipe')
# async def snipe(ctx):
#     channel = ctx.channel
#     try: #This piece of code is run if the bot finds anything in the dictionary
#         em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
#         em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
#         await ctx.send(embed = em)
#     except: #This piece of code is run if the bot doesn't find anything in the dictionary
#         await ctx.send(f"There are no recently deleted messages in #{channel.name}")

##command to clear channel messages0

# @client.command()
# @commands.has_permissions(manage_messages=True)

# async def clear(ctx,*, amount:int):
#    await ctx.channel.purge(limit=amount)
#    await ctx.send("Message deleted")

# @client.command(description="Unmutes a specified user.")
# @commands.has_permissions(manage_messages=True)
# async def unmute(ctx, member: discord.Member):
#    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

#    await member.remove_roles(mutedRole)
#    await member.send(f" you have unmutedd from: - {ctx.guild.name}")
#    embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
#    await ctx.send(embed=embed)

# @client.command(description="Mutes the specified user.")
# @commands.has_permissions(manage_messages=True)
# async def mute(ctx, member: discord.Member, *, reason=None):
#     guild = ctx.guild
#     mutedRole = discord.utils.get(guild.roles, name="Muted")

#     if not mutedRole:
#         mutedRole = await guild.create_role(name="Muted")

#         for channel in guild.channels:
#             await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
#     embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
#     embed.add_field(name="reason:", value=reason, inline=False)
#     await ctx.send(embed=embed)
#     await member.add_roles(mutedRole, reason=reason)
#     await member.send(f" you have been muted from: {guild.name} reason: {reason}")


@client.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title=name + " Server Information",
                          description=description,
                          color=discord.Color.blue())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    embed.add_field(
        name='Created At',
        value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'),
        inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command()
async def userinfo(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user) + 1))
    embed.add_field(name="Registered",
                    value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles) + 1),
                        value=role_string,
                        inline=True)
    #perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    #embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)


# main command


@client.command()
async def hug(ctx, member: discord.Member, q="anime hug"):

    api_key = os.getenv("API")
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key,
                                                    q,
                                                    limit=5,
                                                    rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(
            title=" UwU",
            description=f"✨  {member.name} is hugged by {ctx.author.name}")
        emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


@client.command()
async def kiss(ctx, member: discord.Member, q="anime kiss"):

    api_key = os.getenv("API")
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key,
                                                    q,
                                                    limit=5,
                                                    rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(
            title=" UwU",
            description=f"✨  {member.name} is kissed by {ctx.author.name}")
        emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


@client.command()
async def pat(ctx, member: discord.Member, q="anime pat"):

    api_key = os.getenv("API")
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key,
                                                    q,
                                                    limit=5,
                                                    rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(
            title=" UwU",
            description=f"✨  {member.name} is patted by {ctx.author.name}")
        emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


@client.command()
async def spank(ctx, member: discord.Member, q="anime spank"):

    api_key = os.getenv("API")
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key,
                                                    q,
                                                    limit=5,
                                                    rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(
            title=" Natkhat ",
            description=f"✨  {member.name} is spanked by {ctx.author.name}",
            color=ctx.guild.me.top_role.color)
        emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


keep_alive()
client.run(os.getenv('TOKEN'))
