import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
import asyncio, os, aiohttp, youtube_dl
import random
from datetime import datetime
import json

load_dotenv()

client = commands.Bot(command_prefix="#")


flags = ['ad', 'ae', 'af', 'ag', 'ai', 'ah', 'ak', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az',
         'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bo', 'bq', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz',
         'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz',
         'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr',
         'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy',
         'hk', 'hm', 'hn', 'hr', 'ht', 'ic', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp',
         'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly',
         'ma', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz',
         'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'ny', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn',
         'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm',
         'sn', 'so', 'sr', 'ss', 'st', 'sv', 'sx', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tr', 'tt', 'tv', 'tw', 'tz',
         'ua', 'ug', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'es', 'xk', 'ye', 'yt', 'za', 'zm', 'zw']


statelist = ('states/al.png', 'states/ak.png', 'states/az.png', 'states/ar.png', 'states/ca.png', 'states/co.png', 'states/ct.png', 'states/de.png', 'states/fl.png', 'states/ga.png', 'states/hi.png', 'states/id.png', 'states/il.png', 'states/in.png','states/ia.png', 'states/ks.png', 'states/ky.png', 'states/la.png', 'states/me.png', 'states/md.png', 'states/ma.png', 'states/mi.png', 'states/mn.png', 'states/ms.png', 'states/mo.png', 'states/mt.png', 'states/ne.png', 'states/nv.png', 'states/nh.png', 'states/nj.png', 'states/nm.png', 'states/ny.png', 'states/nc.png', 'states/nd.png', 'states/oh.png', 'states/ok.png', 'states/or.png', 'states/pa.png', 'states/ri.png', 'states/sc.png', 'states/sd.png', 'states/tn.png','states/tx.png', 'states/ut.png', 'states/vt.png', 'states/va.png', 'states/wa.png', 'states/wv.png', 'states/wi.png', 'states/wy.png')
stateguesses = ( 'alab', 'alas', 'ariz', 'arka', 'cali', 'colo', 'conn', 'dela', 'flor', 'geor', 'haw', 'ida', 'illi', 'indi', 'iowa', 'kans', 'kent', 'louis', 'main', 'mary', 'mass', 'mich', 'minn', 'missi', 'misso', 'mont', 'nebr', 'nevad', 'new ham', 'new jer', 'new mex', 'new yor', 'north car', 'north dak', 'ohio', 'okla', 'oreg', 'pennsy', 'rhod', 'south car', 'south dak', 'tenn', 'texas', 'utah', 'verm', 'virg', 'washi', 'west vir', 'wisco', 'wyom')
stateanswers = ( 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',  'West Virginia', 'Wisconsin', 'Wyoming')


PTlist = ('provinces/ab.png', 'provinces/bc.png', 'provinces/mb.png', 'provinces/nb.png', 'provinces/nl.png', 'provinces/ns.png', 'provinces/nt.png', 'provinces/nu.png', 'provinces/on.png', 'provinces/pe.png', 'provinces/qc.png', 'provinces/sk.png', 'provinces/yt')
PTguesses = ('alber', 'british col', 'manit', 'new bruns', 'newfoundland and lab', 'nova scot', 'northwest terr', 'nunavut', 'ontario', 'prince edward i', 'quebec', 'saskatch', 'yukon')
PTanswers = ('Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador', 'Nova Scotia', 'Northwest Territories', 'Nunavut', 'Ontario', 'Prince Edward Island', 'Quebec', 'Saskatchewan', 'Yukon')

dicts = {}
dictp = {}
dictf = {}

trophy = 'https://library.kissclipart.com/20180923/ouq/kissclipart-transparent-trophy-cartoon-clipart-trophy-clip-art-ebb7c5fad5a04dee.jpg'


@client.event
async def on_ready():
    print("GeoBot is online g.\n")


botToken = os.getenv("TOKEN")


@client.command()
async def country(ctx, msg):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://restcountries.eu/rest/v2/name/' + msg)

        countryjson = await request.json()

        embedV1 = discord.Embed(title="Country:" + (countryjson[0]['name']), description=(' '), color=0x641ED2)
        embedV1.add_field(name="Capital", value=(countryjson[0]['capital']), inline=True)
        embedV1.add_field(name="Language", value=(countryjson[0]['languages'][0]['name']), inline=True)
        embedV1.add_field(name="Currency", value=(countryjson[0]['currencies'][0]['name']), inline=True)
        embedV1.add_field(name="Land Area", value=(str(countryjson[0]['area']) + " km²"), inline=True)
        embedV1.add_field(name="Population", value=(countryjson[0]['population']), inline=True)
        embedV1.add_field(name="Currency Symbols", value=(
                    countryjson[0]['currencies'][0]['code'] + " " + countryjson[0]['currencies'][0]['symbol']),
                          inline=True)
        embedV1.add_field(name="Flag", value=':flag_' + (str(countryjson[0]['alpha2Code'] + ':')).swapcase(),
                          inline=True)

        await ctx.send(embed=embedV1)


@client.command()
async def scores(ctx):
    dicts = json.load(open('scores'))
    dictp = json.load(open('scoresp'))
    dictf = json.load(open('scoresf'))

    embedVar = discord.Embed(title='State Quiz Scoreboard', color=0x4fff00)
    embedVar.set_thumbnail(url=trophy)
    for user, score in dicts.items():
        embedVar.add_field(name=f"{user}", value=f"{score} points", inline=False)

    await ctx.send(embed=embedVar)

    embedVar = discord.Embed(title='Province Quiz Scoreboard', color=0x37ff00)
    embedVar.set_thumbnail(url=trophy)
    for user, score in dictp.items():
        embedVar.add_field(name=f"{user}", value=f"{score} points", inline=False)

    await ctx.send(embed=embedVar)

    embedVar = discord.Embed(title='Flag Quiz Scoreboard', color=0x00ff00)
    embedVar.set_thumbnail(url=trophy)
    for user, score in dictf.items():
        embedVar.add_field(name=f"{user}", value=f"{score} points", inline=False)

    await ctx.send(embed=embedVar)


@client.command()
async def helpme(ctx):
    embedVt = discord.Embed(title="GeoBot Help", description="List of Geobot's commands (prefix is '#')", color=0x30A6EB)
    embedV = discord.Embed(title="Geography", description=" ", color=0x3076DB)
    embedV.add_field(name=str(client.command_prefix)+"states", value="starts a quiz on American states", inline=True)
    embedV.add_field(name=str(client.command_prefix) + "provinces", value="starts a quiz on Canadian Provinces and Territories",inline=True)
    embedV.add_field(name=str(client.command_prefix)+"country", value="provides information about any country in the world", inline=True)
    embedV.add_field(name=str(client.command_prefix) + "cflag", value="shows flag of any country",inline=True)
    embedV.add_field(name=str(client.command_prefix) + "rflag", value="shows a random flag and asks for country of origin", inline=True)
    embedV.add_field(name=str(client.command_prefix) + "scores", value="shows scoreboard with points gained from state, province, and flag quizzes", inline=True)

    embedVm = discord.Embed(title="Music", description=" ", color=0x3046CB)
    embedVm.add_field(name=str(client.command_prefix)+"play", value="plays a song (requires youtube url)", inline=True)
    embedVm.add_field(name=str(client.command_prefix)+"pause", value="pauses music", inline=True)
    embedVm.add_field(name=str(client.command_prefix) + "resume", value="resumes playing music", inline=True)
    embedVm.add_field(name=str(client.command_prefix) + "leave", value="disconnects bot from voice channel", inline=True)
    embedVm.add_field(name=str(client.command_prefix) + "stop", value="stops the audio player", inline=True)

    embedVo = discord.Embed(title="Other", description=" ", color=0x3016EB)
    embedVo.add_field(name=str(client.command_prefix) + "helpme", value="shows this menu", inline=True)
    embedVo.add_field(name=str(client.command_prefix) + "prefix", value="changes GeoBot's prefix", inline=True)
    embedVo.add_field(name=str(client.command_prefix) + "info", value="info about GeoBot", inline=True)

    await ctx.send(embed=embedVt)
    await ctx.send(embed=embedV)
    await ctx.send(embed=embedVm)
    await ctx.send(embed=embedVo)


@client.command()
async def prefix(ctx, prefix):
    client.command_prefix = prefix
    embedPre = discord.Embed(title=f"Prefix changed to ``'{prefix}'``", color=0xD000FF)
    await ctx.send(embed=embedPre)


@client.command()
async def cflag(ctx, ff):
    embedVar = discord.Embed(title=f'{ff.upper()}', color=0x00ff00)
    embedVar.set_image(url=f"https://www.countryflags.io/{ff.lower()}/shiny/64.png")
    await ctx.send(embed=embedVar)


@client.command()
async def rflag(ctx):
    pick = random.choice(flags)

    scoref = 0
    dictf = json.load(open('scoresf'))
    correct = discord.File('greencheck.png', filename="image.png")
    timesup = discord.File('clock.png', filename="image.png")

    def check(m):
        return (m.content).lower() == f'{str(pick)}' and m.channel == ctx.channel


    embedrf = discord.Embed(title='What country is this flag from?', description="(Country Code Only)", color=0x9fdf00)
    embedrf.set_image(url=f"https://www.countryflags.io/{pick}/shiny/64.png")
    await ctx.send(embed=embedrf)

    try:
        scoref += 1
        msg = await client.wait_for('message', check=check, timeout=8)
        embedrc = discord.Embed(title=f'{msg.author} was Correct!', description=("Score = " + str(scoref)), color=0x00df5f)
        embedrc.set_thumbnail(url="attachment://image.png")
        await ctx.send(file=correct, embed=embedrc)

        if f'{msg.author}' in dictf:
            dictf[f'{msg.author}'] += 1
        else:
            dictf.update({f'{msg.author}': 1})

        json.dump(dictf, open('scoresf', 'w'))

    except asyncio.TimeoutError:
        embedrft = discord.Embed(title="Time's up!", description=("Score = " + str(scoref)),  color=0xdf9f00)
        embedrft.add_field(name="Correct answer: ", value=(f"{pick}").swapcase(), inline=False)
        embedrft.set_thumbnail(url="attachment://image.png")
        await ctx.send(file = timesup, embed=embedrft)



@client.command()
async def states(message):
    ctx = message.channel
    a = random.randint(0, 49)
    now = datetime.now()
    alive = True
    win = True
    update = True
    score = 0
    dicts = json.load(open('scores'))
    tmt = 8
    if f'{message.author}' not in dicts:
        dicts.update({f'{message.author}': 0})

    def checkstate(msg):
        return msg.content.lower() and msg.channel

    while (alive):


        correctAns = (stateguesses[a])
        correctAnswerFull = (stateanswers[a])
        file = discord.File(statelist[a], filename="image.png")
        correct = discord.File('greencheck.png', filename="image.png")
        timesup = discord.File('clock.png', filename="image.png")
        embedV = discord.Embed(title="States Quiz", description="What state is this?", color=0x30A6EB)
        embedV.set_image(url="attachment://image.png")
        if update:
            await ctx.send(file=file, embed=embedV)
            update = False
        """await ctx.send('What state is this?')"""

        try:
            later = datetime.now()
            tmt -= ((later - now).total_seconds())
            now = datetime.now()
            if tmt<0:
                tmt=0
            if win:
                tmt = 8
                win = False
            print(tmt)

            msg = await client.wait_for("message", check=checkstate, timeout=tmt)
            if msg.content.startswith(correctAns) and msg.channel == ctx:
                score += 1
                win = True

                if f'{msg.author}' in dicts:
                    dicts[f'{msg.author}'] += 1
                else:
                    dicts.update({f'{msg.author}': 1})

                json.dump(dicts, open('scores', 'w'))

                embedy = discord.Embed(title="Correct!", description=("Score = " + str(score)), color=0x00FF00)
                embedy.set_thumbnail(url="attachment://image.png")
                await ctx.send(file=correct, embed=embedy)
                a = random.randint(0, 49)
                update = True

        except asyncio.TimeoutError:
            embedt = discord.Embed(title="Time's Up!!", description=("Game Over: Score = " + str(score)),
                                   color=0xFF7F00)
            embedt.add_field(name="Correct Answer", value=correctAnswerFull, inline=False)
            embedt.set_thumbnail(url="attachment://image.png")
            await ctx.send(file=timesup, embed=embedt)
            a = random.randint(0, 49)
            update = True
            alive = False



@client.command()
async def provinces(message):
    ctx = message.channel
    b = random.randint(0, 12)
    nowp = datetime.now()
    alivep = True
    winp = True
    updatep = True
    scorep = 0
    dictp = json.load(open('scoresp'))
    tmtp = 8
    if f'{message.author}' not in dictp:
        dictp.update({f'{message.author}': 0})

    def checkprov(msg):
        return msg.content.lower() and msg.channel

    while (alivep):
        correctAnsp = (PTguesses[b])
        correctAnswerFullp = (PTanswers[b])
        file = discord.File(PTlist[b], filename="image.png")
        correct = discord.File('greencheck.png', filename="image.png")
        timesup = discord.File('clock.png', filename="image.png")
        embedVp = discord.Embed(title="States Quiz", description="What province/territory is this?", color=0x30A6EB)
        embedVp.set_image(url="attachment://image.png")
        if updatep:
            await ctx.send(file=file, embed=embedVp)
            updatep = False
        """await ctx.send('What state is this?')"""

        try:
            laterp = datetime.now()
            tmtp -= ((laterp - nowp).total_seconds())
            nowp = datetime.now()
            if tmtp<0:
                tmtp=0
            if winp:
                tmtp = 8
                winp = False
            print(tmtp)

            msg = await client.wait_for("message", check=checkprov, timeout=tmtp)
            if msg.content.startswith(correctAnsp) and msg.channel == ctx:
                scorep += 1
                winp = True

                if f'{msg.author}' in dictp:
                    dictp[f'{msg.author}'] += 1
                else:
                    dictp.update({f'{msg.author}': 1})

                json.dump(dictp, open('scoresp', 'w'))

                embedyp = discord.Embed(title="Correct!", description=("Score = " + str(scorep)), color=0x00FF00)
                embedyp.set_thumbnail(url="attachment://image.png")
                await ctx.send(file=correct, embed=embedyp)
                b = random.randint(0, 12)
                updatep = True

        except asyncio.TimeoutError:
            embedtp = discord.Embed(title="Time's Up!!", description=("Game Over: Score = " + str(scorep)), color=0xFF7F00)
            embedtp.add_field(name="Correct Answer", value=correctAnswerFullp, inline=False)
            embedtp.set_thumbnail(url="attachment://image.png")
            await ctx.send(file=timesup, embed=embedtp)
            b = random.randint(0, 12)
            updatep = True
            alivep = False


def is_connect(ctx):
    voice_cli = get(ctx.bot.voice_clients, guild=ctx.guild)
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
    if is_connect(ctx):
        await voiceChannel.disconnect()
    else:
        await ctx.send("{0.user} is not connected.".format(client))


@client.command()
async def joinback(ctx):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Holding Cell')
    if not is_connect(ctx):
        await voiceChannel.connect()
    else:
        await ctx.send("{0.user} is already connected.".format(client))


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("{0.user} is not playing audio.".format(client))


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("{0.user} is not paused.".format(client))


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command()
async def info(ctx):
    Logo = discord.File('GeoBot.png', filename="image.png")
    embedscrt = discord.Embed(title="GeoBot", description="RU Hacks 2021", color=0x6F00FF)
    embedscrt.set_footer(text="This bot was made by the members of the Ass Car Alex Discord Server")
    embedscrt.set_image(url="attachment://image.png")
    await ctx.send(file=Logo, embed=embedscrt)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embederr = discord.Embed(title="Invalid", description="Not a valid GeoBot command", color=0xFF0000)
        await ctx.send(embed=embederr)


client.run(botToken)
