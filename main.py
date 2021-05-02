import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
import asyncio, os, aiohttp, youtube_dl
import random
import json

load_dotenv()

client = commands.Bot(command_prefix="#")

statelist = ('states/al.png', 'states/ak.png', 'states/az.png', 'states/ar.png', 'states/ca.png', 'states/co.png', 'states/ct.png', 'states/de.png', 'states/fl.png', 'states/ga.png', 'states/hi.png', 'states/id.png', 'states/il.png', 'states/in.png', 'states/ia.png', 'states/ks.png', 'states/ky.png', 'states/la.png', 'states/me.png', 'states/md.png', 'states/ma.png', 'states/mi.png', 'states/mn.png', 'states/ms.png', 'states/mo.png', 'states/mt.png', 'states/ne.png', 'states/nv.png', 'states/nh.png', 'states/nj.png', 'states/nm.png', 'states/ny.png', 'states/nc.png', 'states/nd.png', 'states/oh.png', 'states/ok.png', 'states/or.png', 'states/pa.png', 'states/ri.png', 'states/sc.png', 'states/sd.png', 'states/tn.png', 'states/tx.png', 'states/ut.png', 'states/vt.png', 'states/va.png', 'states/wa.png', 'states/wv.png', 'states/wi.png', 'states/wy.png')
stateguesses = ('alab', 'alas', 'ariz', 'arka', 'cali', 'colo', 'conn', 'dela', 'flor', 'geor', 'haw', 'ida', 'illi', 'indi', 'iowa', 'kans', 'kent', 'louis', 'main', 'mary', 'mass', 'mich', 'minn', 'missi', 'misso', 'mont', 'nebr', 'nevad', 'new ham', 'new jer', 'new mex', 'new yor', 'north car', 'north dak', 'ohio', 'okla', 'oreg', 'pennsy', 'rhod', 'south car', 'south dak', 'tenn', 'texas', 'utah', 'verm', 'virg', 'washi', 'west vir', 'wisco', 'wyom')
stateanswers = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')

dict = {}
trophy = 'https://library.kissclipart.com/20180923/ouq/kissclipart-transparent-trophy-cartoon-clipart-trophy-clip-art-ebb7c5fad5a04dee.jpg'

@client.event
async def on_ready():
    print("GeoBot is online g.\n")


botToken = os.getenv("TOKEN")


@client.command()
async def country(ctx, msg):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://restcountries.eu/rest/v2/name/'+msg)

        countryjson = await request.json()

        embedV1 = discord.Embed(title="Country:"+(countryjson[0]['name']), description=(' '), color=0x641ED2)
        embedV1.add_field(name="Capital", value=(countryjson[0]['capital']), inline=True)
        embedV1.add_field(name="Language", value=(countryjson[0]['languages'][0]['name']), inline=True)
        embedV1.add_field(name="Currency", value=(countryjson[0]['currencies'][0]['name']), inline=True)
        embedV1.add_field(name="Land Area", value=(str(countryjson[0]['area'])+" km²"), inline=True)
        embedV1.add_field(name="Population", value=(countryjson[0]['population']), inline=True)
        embedV1.add_field(name="Currency Symbols", value=(countryjson[0]['currencies'][0]['code']+" "+countryjson[0]['currencies'][0]['symbol']), inline=True)
        embedV1.add_field(name="Flag", value=':flag_'+(str(countryjson[0]['alpha2Code']+':')).swapcase(), inline=True)

        await ctx.send(embed=embedV1)

"""@client.event
async def on_message(message):
    if (message.content.startswith('#') == False):
        author = str(message.author)
        msg = message.content.lower()
        time = str(message.created_at)
        dateshort = time[0:10]
        timeshort = time[11:19]
        if (author != client.user):
            print('On '+dateshort+'\tat '+timeshort+',\t'+author+'  \tsaid\t"'+msg+'"')"""


@client.command()
async def sb(ctx):
    dict = json.load(open('scores'))

    embedVar = discord.Embed(title='Scoreboard', color=0x00ff00)
    embedVar.set_thumbnail(url=trophy)
    for user, score in dict.items():
        embedVar.add_field(name=f"{user}", value=f"{score} points", inline=False)

    await ctx.send(embed=embedVar)


@client.command()
async def helpme(ctx):
    embedV = discord.Embed(title="GeoBot Help", description="List of Geobot's commands (prefix is '#')", color=0x30A6EB)
    embedV.add_field(name="play", value="plays song", inline=True)
    embedV.add_field(name="states", value="statequiz", inline=True)
    embedV.add_field(name="leave", value="Disconnects GeoBot", inline=True)
    await ctx.send(embed=embedV)


@client.command()
async def states(message):
    ctx = message.channel
    a = random.randint(0, 49)
    alive = True
    update = True
    score = 0
    dict = json.load(open('scores'))
    def checkstate(msg):
        return msg.content.lower()

    def checkchan(msg):
        return msg.channel

    while (alive):


        correctAns = (stateguesses[a])
        correctAnswerFull = (stateanswers[a])
        file=discord.File(statelist[a], filename="image.png")
        correct=discord.File('greencheck.png', filename="image.png")
        incorrect = discord.File('redx.png', filename="image.png")
        timesup = discord.File('clock.png', filename="image.png")
        embedV = discord.Embed(title="States Quiz", description="What state is this?", color=0x30A6EB)
        embedV.set_image(url="attachment://image.png")
        if update:
            await ctx.send(file=file, embed=embedV)
            update = False
        """await ctx.send('What state is this?')"""



        try:
            msg = await client.wait_for("message", check=checkstate, timeout=5)
            if msg.content.startswith(correctAns):
                score += 1

                if f'{msg.author}' in dict:
                    dict[f'{msg.author}'] += score
                else:
                    dict.update({f'{msg.author}': 10})

                json.dump(dict, open('scores', 'w'))

                embedy = discord.Embed(title="Correct!", description=("Score = " + str(score)), color=0x00FF00)
                embedy.set_thumbnail(url="attachment://image.png")
                await ctx.send(file=correct, embed=embedy)
                a = random.randint(0, 49)
                update = True

            elif checkchan(msg) == ctx:
                embedn = discord.Embed(title="Incorrect!", description=("Game Over: Score = " + str(score)), color=0xFF0000)
                embedn.add_field(name="Your Answer", value=(msg.content.lower()), inline=False)
                embedn.add_field(name="Correct Answer", value=correctAnswerFull, inline=False)
                embedn.set_thumbnail(url="attachment://image.png")
                await ctx.send(file=incorrect, embed=embedn)
                a = random.randint(0, 49)
                update = True
                alive = False

        except asyncio.TimeoutError:
            embedt = discord.Embed(title="Time's Up!!", description=("Game Over: Score = " + str(score)), color=0xFF7F00)
            embedt.add_field(name="Correct Answer", value=correctAnswerFull, inline=False)
            embedt.set_thumbnail(url="attachment://image.png")
            await ctx.send(file=timesup, embed=embedt)
            a = random.randint(0, 49)
            update = True
            alive = False

        """finally:
            a = random.randint(0, 29)"""


def is_connect(ctx):
    voice_cli = get(ctx.bot.voice_clients, guild = ctx.guild)
    return voice_cli and voice_cli.is_connected()

@client.command()
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")

    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Holding Cell')
    connected = False

    if not is_connect(ctx):
        await voiceChannel.connect()

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    embedwait = discord.Embed(title="Downloading MP3...", description="Please wait", color=0xFF0000)
    await ctx.send(embed=embedwait)


    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    embedplaying = discord.Embed(title="Download Fnished", description="Now Playing", color=0xFF2F2F)
    await ctx.send(embed=embedplaying)
    print('playing')


@client.command()
async def leave(ctx):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Holding Cell')
    if is_connect():
        await voiceChannel.disconnect()
    else:
        await ctx.send("{0.user} is not connected." .format(client))


@client.command()
async def joinback(ctx):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Holding Cell')
    if not is_connect():
        await voiceChannel.connect()
    else:
        await ctx.send("{0.user} is already connected." .format(client))


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("{0.user} is not playing audio." .format(client))


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("{0.user} is not paused." .format(client))


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command()
async def secret(ctx):
    Logo = discord.File('GeoBot.png', filename="image.png")
    embedscrt = discord.Embed(title="GeoBot", description="RU Hacks 2021", color=0x6F00FF)
    embedscrt.set_footer(text="This bot was made by the members of the Ass Car Alex Discord Server")
    embedscrt.set_image(url="attachment://image.png")
    await ctx.send(file=Logo, embed=embedscrt)



client.run(botToken)
