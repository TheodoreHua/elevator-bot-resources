import discord
import math
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
from random import choice,randint
from random_word import RandomWords
from PyDictionary import PyDictionary
from unit_converter.converter import converts
from googlesearch import search
from googletrans import Translator
import asyncio
import arrow
import typing

client = commands.Bot(command_prefix = 's!')
df = "Elevator Server Bot Ver.13.30.60 Developed By: Kanade Tachibana"
game = cycle(["A Bot for the Elevator Discord Server!",'Developed By: Kanade Tachibana','STFU Pokecord with your annoying level up messages!','Use s!help to see my commands!',df.replace(" Developed By: Kanade Tachibana","")])
hc = 0x8681bb
client.remove_command('help')
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Developed by Kanade Tachibana'))
    change_game.start()
    print("Bot is ready.")

@tasks.loop(seconds=10)
async def change_game():
    await client.change_presence(activity=discord.Game(next(game)))

@client.event
async def on_message(message):
    if len(message.embeds) >= 1:
        for em in message.embeds:
            try:
                if 'is now level' in em.title.lower() or 'is now level' in em.description.lower():
                    embed = discord.Embed(
                        description="STFU POKECORD!",
                        colour=hc
                    )
                    embed.set_footer(text=df)
                    await message.delete()
                    msg = await message.channel.send(embed=embed)
                    await msg.delete(delay=10)
            except:
                pass
    if 'niger' in message.content.lower():
        embed = discord.Embed(
            description=f"{message.author.mention} the N word is forbidden! Please don't say it. This message will self destruct in 30 seconds!",
            colour=hc
        )
        embed.set_footer(text=df)
        await message.delete()
        msg = await message.channel.send(embed=embed)
        await msg.delete(delay=30)
    await client.process_commands(message)

@client.command()
async def help(ctx,page='1'):
    help_embed = discord.Embed(
        title='Help',
        description="Here are the commands for the Elevator Discord Bot:",
        colour=hc
    )
    help_embed.set_footer(text=df)
    if page == '1':
        help_embed.add_field(name='s!help <page number>',
                             value='Responds with the page your looking at right now!',
                             inline=False
                             )
        help_embed.add_field(name='s!test',
                             value='Responds with a message if the bot is online!',
                             inline=False
                             )
        help_embed.add_field(name='s!pfp <user> | s!profile <user> | s!avatar <user>',
                             value='Responds the mentioned users profile picture!',
                             inline=False
                             )
        help_embed.add_field(name='s!mock <phrase>',
                             value='Responds with your phrase in weird capitalization!',
                             inline=False
                             )
        help_embed.add_field(name='s!pickupline | s!pl | s!pickup',
                             value='Responds with a random pickup line!',
                             inline=False
                             )
        help_embed.add_field(name='rp!hug <user>',
                             value='Responds with a message telling people that you are hugging them with a random image.',
                             inline=False
                             )
        help_embed.add_field(name='rp!kiss <user>',
                             value='Responds with a message telling people that you are kissing them with a random image.',
                             inline=False
                             )
        help_embed.add_field(name='rp!pat <user>',
                             value='Responds with a message telling people that you are patting them with a random image.',
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='1/7')
    elif page == '2':
        help_embed.add_field(name='rp!facepalm',
                             value='Responds with a message telling people that you are facepalming with a image.',
                             inline=False
                             )
        help_embed.add_field(name='rp!sigh',
                             value='Responds with a message telling people that you are sighing with a image.',
                             inline=False
                             )
        help_embed.add_field(name='rp!cute <user>',
                             value='Responds with a message telling people that you are think they are cute with a image.',
                             inline=False
                             )
        help_embed.add_field(name='rp!sleep | rp!sleepy',
                             value='Responds with a random message and a random GIF or image saying that you are sleepy.',
                             inline=False
                             )
        help_embed.add_field(name='rp!rps <your choice> | rp!rockpaperscissors <your choice>',
                             value='Play a game of Rock Paper Scissors with the bot, to choose your option use "Rock", "Paper", "Scissors" or "R", "P", "S". This command is case-insensitive.',
                             inline=False
                             )
        help_embed.add_field(name='rp!8ball <your question> | rp!8b <your question>',
                             value='Ask the Magic 8 Ball a question and it will answer!',
                             inline=False
                             )
        help_embed.add_field(name='rp!dice <out of>',
                             value='It will generate a random number out of the range you specify, if you do not specify a range the default will be 6',
                             inline=False
                             )
        help_embed.add_field(name='rp!kill <user> <reason>',
                             value='Responds with a random kill message and a random GIF or image with a optional reason.',
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='2/7')
    elif page == '3':
        help_embed.add_field(name='rp!say <message>',
                             value='Says a message as the bot',
                             inline=False
                             )
        help_embed.add_field(name='rp!dm <user> <message>',
                             value='DMs the user as the bot.',
                             inline=False
                             )
        help_embed.add_field(name='rp!slap <user> <reason>',
                             value="Responds with a message that tells the person that you slapped them with a random image and a optional reason.",
                             inline=False
                             )
        help_embed.add_field(name='rp!punch <user> <reason>',
                             value="Responds with a message that tells the person that you punched them with a random image and a optional reason.",
                             inline=False
                             )
        help_embed.add_field(name='rp!sad <reason> | rp!cry <reason>',
                             value='Responds with a random message telling people that you are crying or are sad with a random GIF or image.',
                             inline=False
                             )
        help_embed.add_field(name='rp!mad <reason> | rp!angry <reason>',
                             value='Responds with a random message telling people that you are angry or mad with a random GIF or image.',
                             inline=False
                             )
        help_embed.add_field(name='rp!ship <user 1> <user 2>',
                             value="Responds with a ship name for the 2 mentioned people, I am currently working on a ship image but don't expect that to come anytime soon.",
                             inline=False
                             )
        help_embed.add_field(name='rp!steal <user> <item>',
                             value="Responds with a message telling the person you mentioned that you are stealing the item you mentioned from him/her!",
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='3/7')
    elif page == '4':
        help_embed.add_field(name='rp!punish <user> <reason>',
                             value="Responds with a message telling everyonethat you are punishing the user you mentioned with a optional reason!",
                             inline=False
                             )
        help_embed.add_field(name='rp!insult <user> <reason>',
                             value="Responds with a message telling everyone that you are insulting the user you mentioned with a optional reason!",
                             inline=False
                             )
        help_embed.add_field(name='rp!highfive <user> | rp!hf <user>',
                             value="Responds with a message telling everyone that you are high-fiving the user you mentioned!",
                             inline=False
                             )
        help_embed.add_field(name='rp!chatkilled <user> | rp!ck <user>',
                             value="Responds with a message telling everyone that the chat was killed with a optional user!",
                             inline=False
                             )
        help_embed.add_field(name='rp!flipacoin | rp!fac',
                             value="Responds with heads or tails!",
                             inline=False
                             )
        help_embed.add_field(name='rp!goodjob <user> <reason> | rp!gj <user> <reason>',
                             value="Responds with a message telling everyone that you are congratualating the user you mentioned for doing a good job with a optional reason!",
                             inline=False
                             )
        help_embed.add_field(name='rp!agree <user>',
                             value="Responds with a message telling everyone that you agree with a optional person that you agree with!",
                             inline=False
                             )
        help_embed.add_field(name='rp!give <user> <item>>',
                             value="Responds with a message telling everyone that you are giving the user you mentioned a item!",
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='4/7')
    elif page == '5':
        help_embed.add_field(name='rp!invite',
                             value="Responds with a message with the invite to the server!",
                             inline=False
                             )
        help_embed.add_field(name='rp!x <user> | rp!doubt <user>',
                             value="Responds with a message telling everyone to spam x to doubt with a optional user!",
                             inline=False
                             )
        help_embed.add_field(name='rp!f <user> | rp!respects <user>',
                             value="Responds with a message telling everyone to press f to pay respects with a optional user!",
                             inline=False
                             )
        help_embed.add_field(name='rp!hb <user> | rp!happybirthday <user> | rp!birthday <user>',
                             value="Responds with a message wishing the user you mentioned a happy birthday!",
                             inline=False
                             )
        help_embed.add_field(name='rp!boredom | rp!bored | rp!boredom.exe',
                             value="Responds with a message telling everyone that you are bored with a random message!",
                             inline=False
                             )
        help_embed.add_field(name='rp!thinking | rp!think | rp!thinking.exe',
                             value="Responds with a message telling everyone that you are thinking with a random message and a random image!",
                             inline=False
                             )
        help_embed.add_field(name='rp!oof <user>',
                             value="Responds with a message telling everyone that you or a optional user you mentioned oofed!",
                             inline=False
                             )
        help_embed.add_field(name='rp!serverinfo',
                             value="Responds with a message telling you various information about the server!",
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='5/7')
    elif page == '6':
        help_embed.add_field(name='rp!hangman',
                             value='Play a game of hangman!',
                             inline=False)
        help_embed.add_field(
            name='rp!uc <number> <unit of number> <target unit> | rp!unitconvert <number> <unit of number> <target unit>',
            value="Convert from a one unit to another!",
            inline=False)
        help_embed.add_field(
            name='rp!numguess <lives> <max> | rp!numberguess <lives> <max> | rp!ng <lives> <max>',
            value="Play a number guessing game. The max number is default 100 if not specified!",
            inline=False)
        help_embed.add_field(
            name='rp!ciz <timezone> | rp!currentinzone <timezone>',
            value="Show the current time and date in the timezone specified, you can use UTC, GMT, and the abbreviation for the timezone.",
            inline=False)
        help_embed.add_field(
            name='rp!cfz <hour> <minute> <original timezone> <target timezone> | rp!convertfromzone <hour> <minute> <original timezone> <target timezone>',
            value="Converts the time from the timezone specified to the target timezone, if the timezone has multiple word, put quotation marks on both sides of the timezone." +
                  " Make sure you enter the time in 24 hour format. You can use UTC, GMT, and the abbreviation for the timezone.",
            inline=False)
        help_embed.add_field(
            name='rp!google <text>',
            value="Googles the text specified and returns the first result, with an option to return up to 5 results",
            inline=False)
        help_embed.add_field(name='rp!translate <phrase>',
                             value='Translates the phrase into english!',
                             inline=False
                             )
        help_embed.add_field(name='rp!translateto <language> <phrase>',
                             value='Translates the phrase into the language you specified!',
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='6/7')
    elif page == '7':
        help_embed.add_field(name='rp!translatefrom <language> <phrase>',
                             value='Translates the phrase from the language you specified!',
                             inline=False
                             )
        help_embed.add_field(name='rp!backwardsname <user> | rp!backname <user> | rp!bn <user>',
                             value="Shows the mentioned user's name backwards! If you don't mention a user, it'll show your own name backwards.",
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='7/7')
    else:
        error_embed = discord.Embed(title='Invalid Page Number',colour=discord.Colour.red())
        error_embed.set_image(url='https://i.imgur.com/XgqWMei.jpg')
        await ctx.message.channel.send(embed=error_embed)
        return
    await ctx.message.channel.send(embed=help_embed)

@client.command()
async def test(ctx):
    embed = discord.Embed(
        title="The bot works fine!",
        colour=hc
    )
    embed.set_footer(text=df)
    await ctx.channel.send(embed=embed)

@client.command(pass_context=True, aliases=['pfp','profile','avatar'])
async def _avatar(ctx, member: discord.Member='None'):
    if member == "None":
        member = ctx.message.author
    a_embed = discord.Embed(
        title=f"{member.display_name}'s Avatar/Profile Picture",
        colour=hc
    )
    a_embed.set_footer(text=df)
    a_embed.set_image(url=f'{member.avatar_url}')

    await ctx.message.channel.send(embed=a_embed)

@client.command()
async def mock(ctx,*,phrase:str):
    mock = ''
    for x in phrase:
        if x == ' ':
            mock += ' '
            continue
        rand = randint(1,2)
        if rand == 1:
            mock += x.upper()
            continue
        mock += x.lower()
    if 'theodore' in phrase.lower() or 'kanade' in phrase.lower():
        mock = f"How dare you insult my owner. {ctx.message.author.mention} go f*ck yourself!"
    embed = discord.Embed(
        title="Here is your mocking sentence",
        description=mock,
        colour=hc
    )
    embed.set_footer(text=df)
    embed.set_image(url='https://i.imgur.com/qDhQKQb.gif')
    if 'theodore' in phrase.lower() or 'kanade' in phrase.lower():
        embed.set_image(url='https://nationalpostcom.files.wordpress.com/2019/06/flip-2.png?w=780')

    await ctx.message.channel.send(embed=embed)

@client.command(aliases=['pickup','pickupline','pl'])
async def _pickuplines(ctx):
    lines = [
        'Hey did you hear about the restaurant on the moon? The food was great but it had no atmosphere. -Jasmine',
        "If i was a gardener, I'd put our tu-lips together. -Jasmine",
        "I'm sorry, were you talking to me? (No) Well then, please start :) - Megan",
        "I'm not a photographer but I can picture me and you together - Megan",
        "Did your licenses get suspended for driving these guys/girls crazy? - Megan",
        "If you were words on a page, it'd be fine print - Megan",
        "Do you believe in love at first sight or should I walk past you again? -Jasmine",
        "Are you a bank loan? Because you've got my interest. -Jasmine",
        "Are you an alien? Because there's nothing like you on Earth (This can technically be an insult but whtevr) - Megan",
        "If nothing lasts forever, will you be my nothing? - Megan",
        "Hey you're pretty and I'm cute, together we'd be pretty cute ;) - Megan",
        "Did you just come out of the oven because WOO you're hot - Megan",
        "Are you a dictionary? Because you add meaning to my life - Megan",
        "Can I follow you home? Because my parents told me to always follow my dreams - Megan",
        "Feel my shirt. It's made of boyfriend/girlfriend material - Megan",
        "What's on this menu? Me 'N' U - Megan",
        "If I could change one thing about you it'd be to..... change your last name - Megan",
        "Are you my phone charger? Because I'd die without you - Megan",
        "Thank god I brought my library card! Because I am totally checking you out - Megan",
        "I'm studying to become a historian. I'm especially interested in a date (The only history joke I'd ever use) - Megan",
        "Could you please grab my arm so I can tell my friends I've been touched my an angel? - Megan",
        "There must be something wrong with my eyes because I can't take my eyes off you - Megan",
        "Do you have an extra heart? Because you just stole mine :( - Megan",
        "Whoever said Disney Land is the happiest place on Earth. H A H A clearly they haven't stood beside you - Megan",
        "Is there an airport near by or is my heart taking off - Megan",
        "I must be in a museum because you're a work of art ! - Megan",
        "Hi, I'm Microsoft. Can I crash at your place tonight? - Megan",
        "Did you invent the airplane? Because you seem just Wright - Megan",
        "Are you religious? Because you're the answer to all my prayers - Megan",
        "Can I tie your shoes? Because I don't want you falling for anyone else - Megan',"
        "If I can rearrange the alphabet, I'd put U and I together <3 - Megan",
        "Are you a magician because whenever I look at you, you make everyone else disappear! - Megan",
        "I'm lost, can you give me directions to your heart? - Megan",
        "Are you a magnet? Because you're attracting me from over -here!! - Megan",
        "HELP MY PHONES NOT WORKING! IT DOESN'T HAVE YOUR NUMBER - Megan",
        "Are you a camera? Because I smile at you whenever I see you - Megan",
        "Are you a parking ticket because you got fine written all over you - Megan",
        "CALL THE COPS! IT'S A CRIME TO STEAL MY HEART - Megan",
        "Are you French? Because Eiffel for you - Megan",
        "Is your dad a boxer? Because you're a knockout! - Megan",
        "I seem to have lost my number, may i have yours? - Megan",
        "Is it hot in here? Or is it just you.",
        "Are you Google? Because you are all I've been searching for - Megan",
        "Are you a phaser from Star Trek? Because you're set to stun - Megan"
    ]
    line = choice(lines)
    embed = discord.Embed(
        title=f"{ctx.message.author.name} here is your pickup line.",
        description=line,
        colour=hc
    )
    embed.set_footer(text=df)
    embed.set_image(url='https://g2x4w9d4.stackpathcdn.com/wp-content/uploads/2017/02/cheesy.gif')

    await ctx.message.channel.send(embed=embed)

@client.command()
async def hug(ctx,users:commands.Greedy[discord.User]):
    random_hug_image_gif = ['https://i.imgur.com/FICmRtv.jpg',
                            'https://i.imgur.com/Ourqcvo.jpg',
                            'https://i.imgur.com/QIWmEhg.jpg',
                            'https://i.imgur.com/Rcee4gW.png',
                            'https://i.imgur.com/YmiehhV.png',
                            'https://i.imgur.com/hxmRmTm.png',
                            'https://i.imgur.com/fvlm134.jpg',
                            'https://i.imgur.com/m8DXSgw.jpg'
                            ]
    rhi = choice(random_hug_image_gif)
    user = ', '.join(x.display_name for x in users)
    if user != ctx.message.author.display_name and len(users) >= 1:
        msg = f'{ctx.message.author.display_name} has hugged {user}'
    else:
        msg = f'{ctx.message.author.display_name} is hugging themselves?'
    a_embed = discord.Embed(
        title=msg,
        colour=hc
    )
    a_embed.set_footer(text=df)
    a_embed.set_image(url=rhi)

    await ctx.message.channel.send(embed=a_embed)

@client.command()
async def kiss(ctx,users:commands.Greedy[discord.User]):
    random_kiss_image_gif = ['https://i.imgur.com/0CUZcy1.jpg',
                             'https://i.imgur.com/Bo6FcYk.jpg',
                             'https://i.imgur.com/Gc9eUHC.jpg'
                             ]
    rki = choice(random_kiss_image_gif)
    user = ', '.join(x.display_name for x in users)
    if user != ctx.message.author.display_name and len(users) >= 1:
        msg = f'{ctx.message.author.display_name} has kissed {user}'
    else:
        msg = f'{ctx.message.author.display_name} is kissing themselves?'
    k_embed = discord.Embed(
        title=msg,
        colour=hc
    )
    k_embed.set_footer(text=df)
    k_embed.set_image(url=rki)

    await ctx.message.channel.send(embed=k_embed)

@client.command()
async def pat(ctx,users:commands.Greedy[discord.User]):
    random_pats_image_gif = ['https://i.imgur.com/pUfhIEx.jpg',
                             'https://i.imgur.com/6IEORJr.jpg',
                             'https://i.imgur.com/26Deeck.jpg',
                             'https://i.imgur.com/Gj0fj7m.jpg',
                             'https://i.imgur.com/xOv9bY1.jpg',
                             'https://i.imgur.com/4t3drCT.jpg'
                             ]
    rpi = choice(random_pats_image_gif)
    user = ', '.join(x.display_name for x in users)
    if user != ctx.message.author.display_name and len(users) >= 1:
        msg = f'{ctx.message.author.display_name} is patting {user}!'
    else:
        msg = f'{ctx.message.author.display_name} is patting themselves?'
    p_embed = discord.Embed(
        title=msg,
        colour=hc
    )
    p_embed.set_footer(text=df)
    p_embed.set_image(url=rpi)

    await ctx.message.channel.send(embed=p_embed)

@client.command()
async def facepalm(ctx):
    f_embed = discord.Embed(
        title=f'{ctx.message.author.display_name} is facepalming!',
        colour=hc
    )
    f_embed.set_footer(text=df)
    f_embed.set_image(url='https://i.imgur.com/e1NsTzQ.jpg')

    await ctx.message.channel.send(embed=f_embed)

@client.command()
async def sigh(ctx):
    s_embed = discord.Embed(
        title=f'{ctx.message.author.display_name} has sighed!',
        colour=hc
    )
    s_embed.set_footer(text=df)
    s_embed.set_image(url='https://i.imgur.com/JWeTHLT.jpg')

    await ctx.message.channel.send(embed=s_embed)

@client.command()
async def cute(ctx,*,user:discord.Member='empty'):
    random_cute_image_gif = ['https://i.imgur.com/r6CB5T0.jpg',
                             'https://i.imgur.com/pV9V1zj.jpg',
                             'https://i.imgur.com/FICmRtv.jpg',
                             'https://i.imgur.com/IpBEWZK.jpg',
                             'https://i.imgur.com/lLwkl9v.jpg',
                             'https://i.imgur.com/ez9K9wU.gif',
                             'https://i.imgur.com/S5M8tNM.jpg',
                             'https://i.imgur.com/8F4Y4vT.jpg',
                             'https://i.imgur.com/K4QDlLP.jpg',
                             'https://i.imgur.com/K4QDlLP.jpg',
                             'https://i.imgur.com/t8fvHeK.jpg',
                             'https://i.imgur.com/VM0Me3O.png',
                             'https://i.imgur.com/KUBa7EZ.jpg',
                             'https://i.imgur.com/D0qcnNz.jpg',
                             'https://i.imgur.com/NvCX3uF.jpg',
                             'https://i.imgur.com/hpoFYF3.jpg'
                             ]
    rci = choice(random_cute_image_gif)
    if user != 'empty':
        msg = f'{ctx.message.author.display_name} thinks that {user.display_name} is cute!'
    else:
        msg = f'{ctx.message.author.display_name} is calling themselves cute?'
    c_embed = discord.Embed(
        title=msg,
        colour=hc
    )
    c_embed.set_footer(text=df)
    c_embed.set_image(url=rci)

    await ctx.message.channel.send(embed=c_embed)

@client.command(aliases=['rockpaperscissors','rps'])
async def _rps(ctx,choose):
    choose = choose.lower()
    if choose == 'rock' or choose == 'r':
        is_rps = True
        p_choose = 'Rock'
    elif choose == 'scissors' or choose == 's':
        is_rps = True
        p_choose = "Scissors"
    elif choose == 'paper' or choose == 'p':
        is_rps = True
        p_choose = "Paper"
    else:
        is_rps = False
        embed = discord.Embed(title="Invalid Option, Try again!",colour=discord.Colour.red())
        embed.set_image(url='https://i.imgur.com/XgqWMei.jpg')
    if is_rps:
        RPS_options = ['Rock', 'Paper', 'Scissors']
        b_choose = choice(RPS_options)
        #True = Bot Win False = Player Win Tie = Tie
        if b_choose == p_choose:
            wlt = "Tie"
        elif b_choose == 'Rock':
            if p_choose == "Scissors":
                wlt = True
            if p_choose == "Paper":
                wlt = False
        elif b_choose == "Scissors":
            if p_choose == "Rock":
                wlt = False
            if p_choose == "Paper":
                wlt = True
        elif b_choose == "Paper":
            if p_choose == "Rock":
                wlt = True
            if p_choose == "Scissors":
                wlt = False
        if wlt != "Tie":
            if wlt:
                embed = discord.Embed(title=f"I choose {b_choose}, You chose {p_choose}. I Win!",colour=discord.Colour.red())
            else:
                embed = discord.Embed(title=f"I choose {b_choose}, You chose {p_choose}. I Lose!",colour=discord.Colour.green())
        else:
            embed = discord.Embed(title=f"I choose {b_choose}, You chose {p_choose}. We Tie!",colour=discord.Colour.gold())
        if b_choose == "Rock":
            img = 'https://i.imgur.com/xQQE5UA.jpg'
        elif b_choose == "Scissors":
            img = 'https://i.imgur.com/WAuWmFI.png'
        elif b_choose == "Paper":
            img = 'https://i.imgur.com/SK50Kvl.png'
        embed.set_image(url=img)
    embed.set_footer(text=df)
    await ctx.message.channel.send(embed=embed)

@client.command(aliases=['8ball','8b'])
async def _8ball(ctx,*,question):
    responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
     "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
     "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
     "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
     "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]

    sel_response = choice(responses)

    embed = discord.Embed(title=f'{sel_response}!',description=f'Your Question: {question}!',colour=hc)
    embed.set_image(url='https://i.imgur.com/Es4mCIe.jpg')
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command()
async def dice(ctx,out_of='6'):
    con = True
    try:
        out_of_int = int(out_of)
    except ValueError as e:
        embed = discord.Embed(title='Please enter a actual number!', colour=discord.Colour.red())
        embed.set_image(url='https://i.imgur.com/XgqWMei.jpg')
        embed.add_field(name="Error:", value=str(e))
        con = False
    if con:
        ran_num = str(randint(1,out_of_int))
        embed = discord.Embed(title=f'The Dice Says: {ran_num}', colour=hc)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command(pass_context=True)
async def kill(ctx,user:discord.Member,*,reason='None'):
    random_kill_message = [f'{ctx.message.author.display_name} has killed {user.display_name}',
                           f'{ctx.message.author.display_name} has headshotted {user.display_name}',
                           f'{user.display_name} was shot by {ctx.message.author.display_name}']
    random_kill_gif = ['https://i.imgur.com/qflLsJu.gif',
                       'https://i.imgur.com/Za8sxpF.gif',
                       'https://i.ibb.co/bsYTnQ4/killgif2.gif'
                       ]
    km = choice(random_kill_message)
    kg = choice(random_kill_gif)
    k_embed = discord.Embed(
        title=km,
        colour=hc
    )
    k_embed.set_footer(text=df)
    k_embed.set_image(url=kg)
    if reason != "None":
        k_embed.add_field(name="Reason:",value=reason)
    await ctx.message.channel.send(embed=k_embed)

@client.command()
async def dm(ctx,member: discord.Member,*,message):
    await ctx.message.delete()
    await member.send(message)

@client.command()
async def say(ctx,*,message):
    await ctx.message.delete()
    await ctx.send(message)

@client.command()
async def slap(ctx,user:discord.Member,*,reason="None"):
    random_slap_image_gif = ['https://i.imgur.com/8yJ9qoh.jpg',
                             'https://i.imgur.com/LLIKgWT.png'
    ]
    rsi = choice(random_slap_image_gif)
    c_embed = discord.Embed(
        title=f'{ctx.message.author.display_name} has slapped {user.display_name}!',
        colour=hc
    )
    c_embed.set_footer(text=df)
    c_embed.set_image(url=rsi)
    if reason != "None":
        c_embed.add_field(name="Reason:",value=reason)

    await ctx.message.channel.send(embed=c_embed)

@client.command()
async def punch(ctx,user:discord.Member,*,reason='None'):
    random_punch_image_gif = ['https://i.ibb.co/bsYTnQ4/killgif2.gif',
                             'https://i.imgur.com/Za8sxpF.gif'
    ]
    rpi = choice(random_punch_image_gif)
    p_embed = discord.Embed(
        title=f'{ctx.message.author.display_name} has punched {user.display_name}!',
        colour=hc
    )
    p_embed.set_footer(text=df)
    p_embed.set_image(url=rpi)
    if reason != "None":
        p_embed.add_field(name="Reason:",value=reason)

    await ctx.message.channel.send(embed=p_embed)

@client.command(aliases=['cry','sad'])
async def _crysad(ctx,*,reason="None"):
    random_cry_sad_image = ['https://i.imgur.com/2idqzX5.jpg',
                            'https://i.imgur.com/21qHg4N.jpg',
                            'https://i.imgur.com/WEIMm9N.jpg',
                            'https://i.imgur.com/DgYa47G.png',
                            'https://i.imgur.com/ED5vXzC.jpg',
                            'https://i.imgur.com/weekaqO.png',
                            'https://i.imgur.com/yR0oqj8.jpg',
                            'https://i.imgur.com/sM6SvUm.jpg',
                            'https://i.imgur.com/ceHRXvU.jpg'
    ]
    random_cry_sad_message = [f"{ctx.message.author.display_name} is sad!",
                              f"{ctx.message.author.display_name} is crying!",
                              f"{ctx.message.author.display_name} is sad! Someone go hug him/her!",
                              f"{ctx.message.author.display_name} is crying! Someone go hug him/her!"
    ]
    rcsi = choice(random_cry_sad_image)
    rcsm = choice(random_cry_sad_message)
    embed = discord.Embed(title=rcsm,colour=hc)
    embed.set_image(url=rcsi)
    embed.set_footer(text=df)
    if reason != "None":
        embed.add_field(name="Reason:",value=reason)
    await ctx.message.channel.send(embed=embed)

@client.command(aliases=['angry','mad'])
async def _angry(ctx,*,reason="None"):
    random_angry_image = ['https://i.imgur.com/1VXQ0cl.jpg',
                          'https://i.imgur.com/lrXbqIq.jpg',
                          'https://i.imgur.com/xCZ8qEr.png'
    ]
    random_angry_message = [f"{ctx.message.author.display_name} is mad!",
                              f"{ctx.message.author.display_name} is angry!",
                              f"{ctx.message.author.display_name} is mad! Don't piss him/her off more",
                              f"{ctx.message.author.display_name} is angry! Someone go hug him/her!",
                              f"{ctx.message.author.display_name} is mad! Tread lightly",
                              f"{ctx.message.author.display_name} is angry! Tread lightly!"
    ]
    rai = choice(random_angry_image)
    ram = choice(random_angry_message)
    embed = discord.Embed(title=ram,colour=hc)
    embed.set_image(url=rai)
    embed.set_footer(text=df)
    if reason != "None":
        embed.add_field(name="Reason:",value=reason)
    await ctx.message.channel.send(embed=embed)

@client.command()
async def ship(ctx,user1: discord.Member,user2: discord.Member):
    length_u1 = math.floor(len(user1.display_name)/2)
    length_u2 = math.floor(len(user2.display_name)/2)
    u1 = user1.display_name[0:length_u1]
    u2 = user2.display_name[length_u2:len(user2.display_name)]
    ship_name = u1 + u2
    ship_embed = discord.Embed(
        title=ship_name,
        description=f"{user1.display_name} and {user2.display_name}'s Ship Name",
        colour=hc
    )
    ship_embed.set_footer(text=df)
    await ctx.message.channel.send(embed=ship_embed)

@client.command()
async def steal(ctx,user: discord.Member,*,item):
    random_steal_message = [f"{ctx.message.author.display_name} has stolen {item} from {user.display_name}!",
                            f"{ctx.message.author.display_name} has taken {item} from {user.display_name}!",
                            f"{user.display_name}'s {item} is missing! It seems {ctx.message.author.display_name} has taken it!",
                            f"{ctx.message.author.display_name} really likes {user.display_name}'s {item} so he/she took it!"
                            ]
    rsm = choice(random_steal_message)
    s_embed = discord.Embed(
        title=rsm,
        colour=hc
    )
    s_embed.set_footer(text=df)
    s_embed.set_image(url='https://i.imgur.com/gQNFxGj.jpg')
    await ctx.message.channel.send(embed=s_embed)

@client.command()
async def punish(ctx,user: discord.Member,*,reason="None"):
    p_embed = discord.Embed(
        title=f"{ctx.message.author.display_name} has punished {user.display_name}!",
        colour=hc
    )
    p_embed.set_footer(text=df)
    p_embed.set_image(url='https://i.imgur.com/RyEErwy.jpg')
    if reason != "None":
        p_embed.add_field(name="Reason:",value=reason)
    await ctx.message.channel.send(embed=p_embed)


@client.command()
async def insult(ctx,user:discord.Member,*,reason="None"):
    random_embed_message = [
        f"{ctx.message.author.display_name} has insulted {user.display_name}!",
        f"{ctx.message.author.display_name} has insulted {user.display_name}, what a savage!",
        f"{user.display_name} has been insulted by {ctx.message.author.display_name}!"
    ]
    rem = choice(random_embed_message)
    i_embed = discord.Embed(
        title=rem,
        colour=hc
    )
    i_embed.set_image(url='https://i.imgur.com/uaz7WXM.jpg')
    if reason != "None":
        i_embed.add_field(name="Reason:",value=reason)
    i_embed.set_footer(text=df)
    await ctx.message.channel.send(embed=i_embed)

@client.command(aliases=['hf','highfive'])
async def _highfive(ctx,user:discord.Member):
    h_embed = discord.Embed(
        title=f"{ctx.message.author.display_name} has high-fived {user.display_name}",
        colour=hc
    )
    h_embed.set_image(url='https://i.imgur.com/CBdjdbi.jpg')
    h_embed.set_footer(text=df)

    await ctx.message.channel.send(embed=h_embed)

@client.command(aliases=['chatkilled','ck'])
async def _chatkilled(ctx,user:discord.Member="None"):
    if user != "None":
        msg = f"{ctx.message.author.display_name} thinks {user.display_name} has killed the chat! Someone revive it!"
    else:
        msg = f"{ctx.message.author.display_name} thinks the chat has been killed. Someone revive it!"
    c_embed = discord.Embed(
        title=msg,
        colour=hc
    )
    c_embed.set_footer(text=df)
    c_embed.set_image(url='https://i.imgur.com/6Z4bVys.jpg')

    await ctx.message.channel.send(embed=c_embed)

@client.command(aliases=['flipacoin','fac'])
async def _flipacoin(ctx):
    sides = ["Heads","Tails"]
    ans = choice(sides)
    r_embed = discord.Embed(
        title=f"You got {ans}!",
        colour=hc
    )
    if ans == "Heads":
        r_embed.set_image(url='https://i.imgur.com/vmuGKvI.png')
    else:
        r_embed.set_image(url='https://i.imgur.com/47kev45.png')
    r_embed.set_footer(text=df)

    await ctx.message.channel.send(embed=r_embed)

@client.command()
async def agree(ctx,user:discord.Member="None"):
    if user != "None":
        msg = f"{ctx.message.author.display_name} agrees with what {user.display_name} said!"
    else:
        msg = f"{ctx.message.author.display_name} agrees with what was said!"
    a_embed = discord.Embed(
        title=msg,
        colour=hc
    )
    a_embed.set_footer(text=df)
    a_embed.set_image(url="https://i.imgur.com/sxu72BJ.jpg")

    await ctx.message.channel.send(embed=a_embed)

@client.command()
async def give(ctx,user: discord.Member,*,item):
    random_give_image = ['https://i.imgur.com/H0dXCW0.jpg',
                         'https://i.imgur.com/6fR6XYD.jpg',
                         'https://i.imgur.com/54wX55D.png'
                            ]
    rgi = choice(random_give_image)
    g_embed = discord.Embed(
        title=f"{ctx.message.author.display_name} has given {item} to {user.display_name}",
        colour=hc
    )
    g_embed.set_footer(text=df)
    g_embed.set_image(url=rgi)
    await ctx.message.channel.send(embed=g_embed)

client.command()
async def invite(ctx):
    #put invite here
    invite = 'https://discord.gg/Cr43nuF'
    i_embed = discord.Embed(
        title="Here is the invite for the Elevator Server",
        colour=hc
    )
    i_embed.set_footer(text=df)
    i_embed.add_field(name="Invite:",value=invite)

    await ctx.message.channel.send(embed=i_embed)

@client.command(aliases=['goodjob','gj'])
async def _goodjob(ctx,user:discord.Member,*,reason="None"):
    random_goodjob_message = [
        f"{ctx.message.author.display_name} thinks {user.display_name} did a good job!",
        f"{ctx.message.author.display_name} is congratulating {user.display_name} for doing a good job!",
        f"{user.display_name} is getting praised by {ctx.message.author.display_name} for doing a good job!"
    ]
    rgjm = choice(random_goodjob_message)

    g_embed = discord.Embed(
        title=rgjm,
        colour=hc
    )
    g_embed.set_footer(text=df)
    g_embed.set_image(url='https://i.imgur.com/YciY7Qo.jpg')
    if reason != "None":
        g_embed.add_field(name="Reason:",value=reason)

    await ctx.message.channel.send(embed=g_embed)

@client.command(aliases=['f','respects'])
async def _f(ctx,user:discord.Member="None"):
    random_f_image = [
            'https://i.imgur.com/Qn4lHqJ.png',
            'https://i.imgur.com/Li6lOuw.jpg'
    ]
    rfi = choice(random_f_image)
    if user != "None":
        msg = f"Press F to pay respects to {user.display_name}"
    else:
        msg = "Press F to pay respects!"
    f_embed = discord.Embed(
        title=msg,
        colour=hc
    )
    f_embed.set_footer(text=df)
    f_embed.set_image(url=rfi)

    await ctx.message.channel.send(embed=f_embed)

@client.command(aliases=['x','doubt'])
async def _x(ctx,user:discord.Member="None"):
    random_x_image = [
        'https://i.imgur.com/0GETcS1.jpg',
        'https://i.imgur.com/wutBLAX.png'
    ]
    rxi = choice(random_x_image)
    if user != "None":
        msg = f"Spam X to doubt {user.display_name}!"
    else:
        msg = "Spam X to doubt!"
    x_embed = discord.Embed(
        title=msg,
        colour=hc
    )
    x_embed.set_footer(text=df)
    x_embed.set_image(url=rxi)

    await ctx.message.channel.send(embed=x_embed)

@client.command(aliases=['hb','happybirthday','birthday'])
async def _happybirthday(ctx,user:discord.Member):
    random_birthday_image = [
            'https://i.imgur.com/sgJBE5E.jpg',
            'https://i.imgur.com/oHVZmQm.jpg',
            'https://i.imgur.com/SlRPSvc.png'
    ]
    rbi = choice(random_birthday_image)
    b_embed = discord.Embed(
        title=f"{ctx.message.author.display_name} wishes a happy birthday to {user.display_name}",
        colour=hc
    )
    b_embed.set_footer(text=df)
    b_embed.set_image(url=rbi)

    await ctx.message.channel.send(embed=b_embed)

@client.command(aliases=['boredom','bored','boredom.exe'])
async def _boredom(ctx):
    random_boredom_message = [
        f'{ctx.message.author.display_name} is bored!',
        f'{ctx.message.author.display_name} has started the process boredom.exe!',
        f'{ctx.message.author.display_name} is bored! Someone RP with him/her!'
    ]
    rbm = choice(random_boredom_message)
    b_embed = discord.Embed(
        title=rbm,
        colour=hc
    )
    b_embed.set_footer(text=df)
    b_embed.set_image(url='https://i.imgur.com/JpSbAji.jpg')

    await ctx.message.channel.send(embed=b_embed)

@client.command(aliases=['thinking','think','thinking.exe'])
async def _thinking(ctx):
    random_thinking_message = [
        f'{ctx.message.author.display_name} is thinking!',
        f'{ctx.message.author.display_name} has started the process thinking.exe!',
    ]
    random_thinking_image = [
        'https://i.imgur.com/tgUNcwr.jpg',
        'https://i.imgur.com/akIMMK9.jpg',
        'https://i.imgur.com/ebHYDox.jpg'
    ]
    rtm = choice(random_thinking_message)
    rti = choice(random_thinking_image)
    t_embed = discord.Embed(
        title=rtm,
        colour=hc
    )
    t_embed.set_footer(text=df)
    t_embed.set_image(url=rti)

    await ctx.message.channel.send(embed=t_embed)

@client.command()
async def oof(ctx,user: discord.Member="None"):
    random_oof_message = [
        f'{ctx.message.author.display_name} got oofed!',
        f'{ctx.message.author.display_name} had a oof moment!',
    ]
    if user != "None":
        random_oof_message.append(f'{ctx.message.author.display_name} thinks {user.display_name} had a oof moment!')
        random_oof_message.append(f'{ctx.message.author.display_name} has oofed {user.display_name}!')
    random_oof_image = [
        'https://i.imgur.com/x4nl4Le.jpg',
        'https://i.imgur.com/yDyG5YY.jpg',
        'https://i.imgur.com/jYJoP7i.jpg'
    ]
    rom = choice(random_oof_message)
    roi = choice(random_oof_image)
    o_embed = discord.Embed(
        title=rom,
        colour=hc
    )
    o_embed.set_footer(text=df)
    o_embed.set_image(url=roi)

    await ctx.message.channel.send(embed=o_embed)

@client.command()
async def serverinfo(ctx):
    guild = ctx.author.guild
    roles = ""
    counter = 0
    for x in guild.roles:
        name = x.name
        if not counter == len(guild.roles) - 1:
            roles += name + ", "
        else:
            roles += name
        counter += 1
    creation_time = guild.created_at
    creation_time = creation_time.strftime("%Y-%m-%d %H:%M UTC")

    i_embed = discord.Embed(
        title=f"Server Info for {guild.name}",
        colour=hc
    )
    i_embed.set_footer(text=df)
    i_embed.add_field(name="Name:",value=guild.name)
    i_embed.add_field(name="Region:", value=str(guild.region))
    i_embed.add_field(name="ID:", value=guild.id)
    i_embed.add_field(name="Owner:", value=guild.owner.display_name)
    i_embed.add_field(name="Member Count:", value=guild.member_count)
    i_embed.add_field(name="Creation Time:", value=creation_time)
    if len(roles) > 1000:
        i_embed.add_field(name="Roles:",value="There are too many roles to be displayed in this message.")
    else:
        i_embed.add_field(name="Roles:", value=roles)

    await ctx.message.channel.send(embed=i_embed)

@client.command()
async def hangman(ctx):
    m = RandomWords()
    d = PyDictionary()
    word = m.get_random_word(hasDictionaryDef='true').lower()
    definition = d.meaning(word)
    if definition == None:
        definition = "Definition Not Found"
    #remove after test
    print(f"Answer: {word}")
    lives = 6
    word_list = []
    guessed_letters = []
    win = False
    for x in word:
        word_list.append('%')
    s_embed = discord.Embed(
        title=''.join(x for x in word_list),
        description="Welcome to Hangman! You have 6 lives. You can only guess one letter at a time (no full word guesses). Type your response. To quit, enter the word 'quit'."
        + " The word can be any word in the english dictionary, and can contain dashes('-').",
        colour=hc
    )
    s_embed.set_footer(text=df)
    s_embed.add_field(name="Lives:",value=str(lives))
    s_embed.add_field(name="Letters Left:",value=str(len([i for i,l in enumerate(word_list) if l == '%'])))
    await ctx.message.channel.send(embed=s_embed)

    def check(message):
        if message.author == ctx.message.author:
            return True
        else:
            return False
    def result(msg,rnr):
        if rnr:
            c = discord.Colour.dark_green()
        else:
            c = discord.Colour.dark_red()
        t_embed = discord.Embed(
            title=''.join(x for x in word_list),
            colour=c
        )
        t_embed.set_footer(text=df)
        t_embed.add_field(name="You Guessed:",value=msg.upper())
        t_embed.add_field(name="Lives:",value=str(lives))
        t_embed.add_field(name="Letters Left:", value=str(len([i for i, l in enumerate(word_list) if l == '%'])))

        return t_embed
    def check_win():
        num_left = len([i for i,l in enumerate(word_list) if l == '%'])
        if num_left == 0:
            return True
        return False

    while True:
        if lives <= 0:
            break
        msg = await client.wait_for('message',check=check,timeout=None)
        msg = msg.content.lower()
        if msg == 'quit':
            break
        if not len(msg) == 1 or msg in guessed_letters:
            await ctx.message.channel.send("You have either already guessed that letter before or you have entered more or less than 1 letter")
            continue
        indexes = [i for i,l in enumerate(word) if l == msg]
        if len(indexes) == 0:
            lives -= 1
            rnr = False
        else:
            for x in indexes:
                word_list[int(x)] = msg
            rnr = True
        guessed_letters.append(msg)
        await ctx.message.channel.send(embed=result(msg,rnr))
        if check_win():
            win = True
            break
    if win:
        e_embed = discord.Embed(
            title="You win!!!",
            colour=discord.Colour.green()
        )
        e_embed.set_footer(text=df)
        e_embed.add_field(name="Word:",value=word)
        e_embed.add_field(name="Lives Left:",value=str(lives))
        e_embed.add_field(name="Definition:",value=definition,inline=False)
    else:
        e_embed = discord.Embed(
            title="You lose!!!",
            colour=discord.Colour.red()
        )
        e_embed.set_footer(text=df)
        e_embed.add_field(name="Word:", value=word)
        e_embed.add_field(name="Letters Left:", value=str(len([i for i, l in enumerate(word_list) if l == '%'])))
        e_embed.add_field(name="Definition:", value=definition, inline=False)
    await ctx.message.channel.send(embed=e_embed)

@client.command(aliases=['unitconvert','uc'])
async def _unitconvert(ctx,num1,unitfrom,unitto):
    units = [
        'm/meter','g/gram','s/second','A/ampere','K/kelvin','mol/mole','cd/candela','Hz/hertz','N/newton','Pa/pascal',
        'J/joule','W/watt','C/coulomb','V/volt','Ω/ohm','S/siemens','F/farad','T/tesla','Wb/weber','H/henry',
        '°C/celsius','rad/radian','sr/steradian','lm/lumen','lx/lux','Bq/becquerel','Gy/gray','Sv/sievert','kat/katal',
        '°F/fahrenheit','th/thou','in/inch','ft/foot','yd/yard','ch/chain','fur/furlong','ml/mile','lea/league','bar',
        'min/minute','h/hour'
    ]
    full_form = num1 + ' ' + unitfrom
    try:
        ans = float(converts(full_form,unitto))
    except Exception as e:
        embed = discord.Embed(
            title="That unit doesn't exist!",
            colour=hc
        )
        embed.set_footer(text=df)
        if unitfrom in str(e):
            embed.add_field(name="Error Unit:",value=f'The unit "{unitfrom}" ' + "doesn't exist!")
        else:
            embed.add_field(name="Error Unit:",value=f'The unit "{unitto}" ' + "doesn't exist!")
        embed.add_field(name="Error:", value=str(e))
        embed.add_field(name="Supported Units",value=', '.join(x for x in units),inline=False)
        await ctx.message.channel.send(embed=embed)
        return
    embed = discord.Embed(
        title=f'{str(ans)} {unitto}',
        colour=hc
    )
    embed.add_field(name="Convert From:",value=f'{num1} {unitfrom}')
    embed.add_field(name="Convert To:",value=unitto)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command(aliases=['numguess','numberguess','ng'])
async def _numguess(ctx,lives,max=100):
    try:
        lives = int(lives)
        max = int(max)
    except:
        await ctx.message.channel.send("Please enter a number!")
        return
    truenum = randint(0,max)
    win = False
    #remove after test
    print(f"Answer: {str(truenum)}")
    start_embed = discord.Embed(
        title="Welcome to the number guessing game! Guess a number between the range below and follow the clues given to guess the correct number. Type 'quit' to quit.",
        colour=hc
    )
    start_embed.set_footer(text=df)
    start_embed.add_field(name="Lives:",value=str(lives))
    start_embed.add_field(name="Range:",value=f"0-{str(max)}")

    await ctx.message.channel.send(embed=start_embed)

    def check(message):
        if message.author == ctx.message.author:
            return True
        else:
            return False
    def result(num,highlow):
        embed = discord.Embed(
            title=f"You guessed too {highlow}!",
            colour=discord.Colour.dark_red()
        )
        embed.add_field(name="You Guessed:",value=str(num))
        embed.add_field(name='Lives Left:',value=str(lives))
        embed.set_footer(text=df)
        return embed
    while True:
        if lives <= 0:
            break
        msg = await client.wait_for('message',check=check,timeout=None)
        if msg.content == 'quit':
            break
        try:
            guessnum = int(msg.content)
        except:
            await ctx.message.channel.send("Please enter a number!")
            continue
        if guessnum > max or guessnum < 0:
            await ctx.message.channel.send(f"The number you guessed is out of the range specified! The range is 0-{str(max)}")
            continue
        if guessnum == truenum:
            win = True
            break
        else:
            lives -= 1
            if guessnum > truenum: highlow = "high"
            if guessnum < truenum: highlow = "low"
            await ctx.message.channel.send(embed=result(guessnum,highlow))
    if win:
        e_embed = discord.Embed(
            title="You win!!!",
            colour=discord.Colour.green()
        )
        e_embed.set_footer(text=df)
        e_embed.add_field(name="Number:",value=str(truenum))
        e_embed.add_field(name="Lives Left:",value=str(lives))
    else:
        e_embed = discord.Embed(
            title="You loose!!!",
            colour=discord.Colour.red()
        )
        e_embed.set_footer(text=df)
        e_embed.add_field(name="Number:", value=str(truenum))
    await ctx.message.channel.send(embed=e_embed)

@client.command(aliases=['currentinzone','ciz'])
async def _currenttimeintimezone(ctx,*,timezone):
    if ' ' in timezone:
        timezone = timezone.title()
    else:
        timezone = timezone.upper()
    utc = arrow.utcnow()
    try:
        current = utc.to(timezone)
    except Exception as e:
        e_embed = discord.Embed(
            title="Invalid Timezone!",
            description="You have may have entered a invalid timezone, if you are sure that the timezone is correct, try entering it in it's" +
            " short or long form, for example if you entered EDT, enter Eastern Daylight Time, and if you entered Eastern Standard Time enter" +
            " EST. Another important thing to keep in mind is Daylight Savings, for example in Toronto if daylight savings is active, we use EDT" +
            "(Eastern Daylight Time) but normally we use EST (Eastern Standard Time). If you were to enter EST, when daylight savings is active, " +
            "The time will be 1 hour off. The same goes for the other timezones that have Daylight Savings or something similar. " +
            "This command also works with UTC, you can enter something like 'UTC-5' which is EST, or 'UTC-4' which is EDT, The same goes for GMT-5/GMT-4. " +
            "This module is still a bit finicky so if there are bugs, rest assured that I am working on fixing it",
            colour=hc
        )
        e_embed.set_footer(text=df)
        e_embed.add_field(name="Error:",value=str(e))
        await ctx.message.channel.send(embed=e_embed)
        return
    r_embed = discord.Embed(
        title=f"Here is the current time in {timezone}",
        colour=hc
    )
    r_embed.set_footer(text=df)
    r_embed.add_field(name="Current Time:",value=current.format('YYYY-MM-DD HH:mm UTC ZZ'))
    await ctx.message.channel.send(embed=r_embed)

@client.command(aliases=['convertfromzone','cfz'])
async def _convertfromtimezone(ctx,hour,min,cfrom,cto):
    def error_zone(error):
        e_embed = discord.Embed(
            title="Invalid Timezone!",
            description="You have may have entered a invalid timezone, if you are sure that the timezone is correct, try entering it in it's" +
                        " short or long form, for example if you entered EDT, enter Eastern Daylight Time, and if you entered Eastern Standard Time enter" +
                        " EST. Another important thing to keep in mind is Daylight Savings, for example in Toronto if daylight savings is active, we use EDT" +
                        "(Eastern Daylight Time) but normally we use EST (Eastern Standard Time). If you were to enter EST, when daylight savings is active, " +
                        "The time will be 1 hour off. The same goes for the other timezones that have Daylight Savings or something similar. " +
                        "This command also works with UTC, you can enter something like 'UTC-5' which is EST, or 'UTC-4' which is EDT, The same goes for GMT-5/GMT-4. " +
                        "This module is still a bit finicky so if there are bugs, rest assured that I am working on fixing it",
            colour=hc
        )
        e_embed.set_footer(text=df)
        e_embed.add_field(name="Error:", value=str(error))
        return e_embed
    if ' ' in cfrom:
        cfrom = cfrom.title()
    else:
        cfrom = cfrom.upper()
    if ' ' in cto:
        cto = cto.title()
    else:
        cto = cto.upper()
    t_utc = arrow.utcnow()
    try:
        t_time_date = t_utc.to(cfrom)
    except Exception as e:
        await ctx.message.channel.send(embed=error_zone(e))
        return
    if len(hour) == 1:
        hour = '0' + hour
    if len(min) == 1:
        hour = '0' + hour
    format_for_get = t_time_date.format('YYYY-MM-DD') + ' ' + hour + ':' + min + ':00' + t_time_date.format('ZZ')
    c_time = arrow.get(format_for_get)
    try:
        current_to = c_time.to(cto)
    except Exception as e:
        await ctx.message.channel.send(embed=error_zone(e))
        return
    r_embed = discord.Embed(
        title=f"Here is the {str(hour)}:{str(min)} {cfrom} in {cto}",
        colour=hc
    )
    r_embed.set_footer(text=df)
    r_embed.add_field(name="Current Time:",value=current_to.format('YYYY-MM-DD HH:mm UTC ZZ'))
    await ctx.message.channel.send(embed=r_embed)

@client.command()
async def google(ctx,*,question):
    msg_list = []
    async def delete_message():
        for message in msg_list:
            await message.delete(delay=30)
    msg_list.append(ctx.message)
    for j in search(question, tld="co.in", num=10, stop=1, pause=0.9):
        result = j
    msg_list.append(await ctx.message.channel.send(f'Google Search Result For "{question}": {result}'))
    msg_list.append(await ctx.message.channel.send("Do you want more results? If you do, type the number of results (maximum of 5) you want below. If you don't type 'quit' or wait 30 seconds"))
    def check(message):
        if message.author == ctx.message.author:
            return True
        else:
            return False
    try:
        result_num = await client.wait_for('message', check=check, timeout=30)
        await result_num.delete(delay=30)
        if result_num.content == 'quit':
            msg_list.append(await ctx.message.channel.send('Request Quit!'))
            await delete_message()
            return
    except:
        msg_list.append(await ctx.message.channel.send("Request Timed Out"))
        await delete_message()
        return
    try:
        result_num = int(result_num.content)
    except:
        msg_list.append(await ctx.message.channel.send("That isn't a number! Request Timed Out"))
        await delete_message()
        return
    if result_num > 5:
        msg_list.append(await ctx.message.channel.send("Discord will only show a maximum of 5 results."))
        result_num = 5
    result_list = []
    for j in search(question, tld="co.in", num=10, stop=result_num, pause=1.8):
        result_list.append(j)
    result = '  |  '.join(x for x in result_list)
    msg_list.append(await ctx.message.channel.send(f'Google Search Result For "{question}": {result}'))
    await delete_message()

@client.command()
async def translate(ctx,*,text):
    translator = Translator()
    translated = translator.translate(text)
    embed = discord.Embed(
        title="Translation Completed",
        colour=hc
    )
    embed.add_field(name="Translated Text:",value=translated.text,inline=False)
    embed.add_field(name="Pronunciation:",value=translated.pronunciation,inline=True)
    embed.add_field(name="Source Language (Auto-Detected):",value=f"{LANGUAGES[translated.src]} ({translated.src})",inline=True)
    embed.add_field(name="Destination Language:",value=f"{LANGUAGES[translated.dest]} ({translated.dest})",inline=True)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command()
async def translateto(ctx,languageto,*,text):
    translator = Translator()
    try:
        translated = translator.translate(text,dest=languageto)
    except Exception as e:
        embed = discord.Embed(title="The language you mentioned doesn't exist!", colour=discord.Colour.red())
        embed.add_field(name="Supported Languages:",value="https://pastebin.com/LMuNGwAK")
        embed.add_field(name="Error:", value=str(e))
        await ctx.message.channel.send(embed=embed)
        return
    embed = discord.Embed(
        title="Translation Completed",
        colour=hc
    )
    embed.add_field(name="Translated Text:", value=translated.text, inline=False)
    embed.add_field(name="Pronunciation:", value=translated.pronunciation, inline=True)
    embed.add_field(name="Source Language (Auto-Detected):",value=f"{LANGUAGES[translated.src]} ({translated.src})",inline=True)
    embed.add_field(name="Destination Language:",value=f"{LANGUAGES[translated.dest]} ({translated.dest})",inline=True)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command()
async def translatefrom(ctx,languagefrom,*,text):
    translator = Translator()
    try:
        translated = translator.translate(text,src=languagefrom)
    except Exception as e:
        embed = discord.Embed(title="The language you mentioned doesn't exist!", colour=discord.Colour.red())
        embed.add_field(name="Supported Languages:",value="https://pastebin.com/LMuNGwAK")
        embed.add_field(name="Error:", value=str(e))
        await ctx.message.channel.send(embed=embed)
        return
    embed = discord.Embed(
        title="Translation Completed",
        colour=hc
    )
    embed.add_field(name="Translated Text:", value=translated.text, inline=False)
    embed.add_field(name="Pronunciation:", value=translated.pronunciation, inline=True)
    embed.add_field(name="Source Language:",value=f"{LANGUAGES[translated.src]} ({translated.src})",inline=True)
    embed.add_field(name="Destination Language:",value=f"{LANGUAGES[translated.dest]} ({translated.dest})",inline=True)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command(aliases=['backwardsname','backname','bn'])
async def _backwardsname(ctx,*,user:discord.Member="None"):
    if user == "None":
        user = ctx.message.author
    name = user.display_name
    backwards_name = ''.join(reversed(name))
    embed = discord.Embed(
        title=backwards_name,
        colour=hc
    )
    embed.add_field(name="Original Name:",value=name)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

client.run('Njk5Njc3MTA4NjA3MTIzNTQ4.XpX3HQ.hIfoh4Q6KzH52D25KYR-QGNMl8k')