from os import system as s

# Installations

s("pip uninstall discord.py")
s("pip install -U python-Levenshtein")
s("pip install -U typing-extensions")
s("pip install -U giphy_client")
s("pip install -U mtranslate")
s("pip install -U langdetect")
s("pip install -U nextcord")
s("pip install -U pynacl")
s("pip install -U sympy")

s('clear')

#------------------------------------------------------------------------#

# Imports

import nextcord
import giphy_client
from random import randint, choice, random
from giphy_client.rest import ApiException
from nextcord.ui import Button, View
from nextcord.ext import commands
from langdetect import detect
from nextcord import Member
from nextcord import client
from urllib import request
from os import getenv
from sympy import *
import mtranslate
import threading
import requests
import aiohttp
import asyncio
import random
import string
import flask
import math
import time
import json

#------------------------------------------------------------------------#

# Running the website

def keepalive():

    app = flask.Flask(__name__)
    
    @app.route("/")
    
    def mainpage(): return "&nbsp;<iframe src='https://discord.com/widget?id=1096200396168503298&theme=dark' width='350' height='500' allowtransparency='true' frameborder='0' sandbox='allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts'></iframe><a href='https://discord.com/oauth2/authorize?client_id=1096876861511970896&permissions=1505856060534&scope=bot%20applications.commands' target='_blank'>Invite Me</a>&nbsp;&nbsp;<a href='https://ph4nt0m-bot.repl.co/'>Main Website</a><style>body { background: #000000; }</style><script>console.log('https://discord.com/oauth2/authorize?client_id=1096876861511970896&permissions=1505856060534&scope=bot%20applications.commands')</script>"
    
    app.run("0.0.0.0")

threading.Thread(target = keepalive).start()

#------------------------------------------------------------------------#

# Emojis for the languages

emoji_dict = {
    
    "🇺🇸": "en",
    "🇩🇪": "de",
    "🇫🇷": "fr",
    "🇪🇸": "es",
    "🇮🇹": "it",
    "🇵🇹": "pt",
    "🇷🇺": "ru",
    "🇦🇱": "sq",
    "🇸🇦": "ar",
    "🇧🇦": "bs",
    "🇧🇬": "bg",
    "🇨🇳": "zh-CN",
    "🇭🇷": "hr",
    "🇨🇿": "cs",
    "🇩🇰": "da",
    "🇪🇪": "et",
    "🇫🇮": "fi",
    "🇬🇷": "el",
    "🇭🇺": "hu",
    "🇮🇩": "id",
    "🇮🇳": "hi",
    "🇮🇪": "ga",
    "🇮🇸": "is",
    "🇮🇱": "he",
    "🇯🇵": "ja",
    "🇰🇷": "ko",
    "🇱🇻": "lv",
    "🇱🇹": "lt",
    "🇲🇹": "mt",
    "🇲🇪": "sr",
    "🇳🇱": "nl",
    "🇳🇴": "no",
    "🇵🇰": "ur",
    "🇵🇱": "pl",
    "🇵🇹": "pt",
    "🇷🇴": "ro",
    "🇷🇸": "sr",
    "🇸🇦": "ar",
    "🇸🇰": "sk",
    "🇸🇮": "sl",
    "🇸🇬": "sv",
    "🇹🇭": "th",
    "🇹🇷": "tr",
    "🇹🇼": "zh-TW",
    "🇺🇦": "uk",
    "🇻🇦": "la"
    
}

#------------------------------------------------------------------------#

# Help command JSON file

helpme = json.load(open("helpme.json"))

#------------------------------------------------------------------------#

# Colours

bla = "\033[0;30m"
red = "\033[0;31m"
gre = "\033[0;32m"
ora = "\033[0;33m"
bl = "\033[0;34m"
pur = "\033[0;35m"
cyan = "\033[0;36m"
whi = "\033[0;37m"
br_bla = "\033[0;90m"
br_red = "\033[0;91m"
br_gre = "\033[0;92m"
br_ora = "\033[0;93m"
br_bl = "\033[0;94m"
br_pur = "\033[0;95m"
br_cyan = "\033[0;96m"
br_whi = "\033[0;97m"
cyan_b = "\033[0;46m"
pur_b = "\033[0;45m"
whi_b = "\033[0;47m"
bl_b = "\033[0;44m"
ora_b = "\033[0;43m"
gre_b = "\033[0;42m"
pink_b = "\033[0;41m"
grey_b = "\033[0;40m"

def rg(r, g, b, text): return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def rgb(t):
    
    for i in t:
        
        i = rg(randint(0, 255), randint(0, 255), randint(0, 255), i)
        print(i, end = "\b", flush = True)
        dy(0.03)

    print()

#------------------------------------------------------------------------#

# Environment secrets

hugging_face_key = getenv("HUGGING_FACE_API_KEY")
api_ninja_token = getenv("API_NINJAS_TOKEN")
flickr_api_key = getenv("FLICKR_KEY")
channel_id = getenv("CHANNEL_ID")
avatar_url = getenv("AVATAR_URL")
dev_prefix2 = getenv("PREFIX2")
giphy_key = getenv("GIPHY_KEY")
dev_prefix = getenv("PREFIX")
api_key = getenv("KEY2")
id = getenv("GUILD_ID")
token = getenv("TOKEN")
key = getenv("KEY")

#------------------------------------------------------------------------#

# Bot initialization

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

bot = nextcord.ext.commands.Bot(command_prefix = ["$"], intents = intents, help_command = None)

#------------------------------------------------------------------------#

# Functions / Variables

a = '"View Audit Log"'

nouns = [
    "Mountain",
    "Forest",
    "Rain",
    "Snowflake",
    "Leaf",
    "Sunbeam",
    "Ocean",
    "Shore",
    "Butterfly",
    "Songbird",
    "Pond",
    "Stone",
    "Temple",
    "Silence",
    "Breeze",
    "Cloud",
    "Star",
    "Willow",
    "Zen",
    "Mist",
    "Bamboo",
    "Haiku",
    "Cherry blossom",
    "Dragonfly",
    "Serenity",
    "Harmony",
    "Seasons",
    "Firefly",
    "Evening",
    "Mountain peak",
    "Reflection",
    "Lotus",
    "Petal",
    "Pebble",
    "Tranquility",
    "Zen garden",
    "Cuckoo",
    "Pine tree",
    "Raindrop",
    "Whisper",
    "Shrine",
    "Harmony",
    "Serene lake",
    "Autumn leaf",
    "Evening glow",
    "Twilight",
    "Heron",
    "Waterfall",
    "Moonlit night",
    "Golden sunset"
]

verbs = [
    "Enchant",
    "Wander",
    "Reflect",
    "Glisten",
    "Soar",
    "Blossom",
    "Dance",
    "Embrace",
    "Radiate",
    "Sing",
    "Drift",
    "Illuminate",
    "Flutter",
    "Roam",
    "Transform",
    "Resonate",
    "Captivate",
    "Whisper",
    "Drench",
    "Awaken",
    "Inspire",
    "Transcend",
    "Harmonize",
    "Exhale",
    "Delight",
    "Reveal",
    "Glide",
    "Unwind"
]

adjectives = [
    "Serene",
    "Peaceful",
    "Tranquil",
    "Gentle",
    "Blissful",
    "Majestic",
    "Enchanting",
    "Harmonious",
    "Soothing",
    "Graceful",
    "Ethereal",
    "Whispering",
    "Captivating",
    "Mesmerizing",
    "Mysterious",
    "Melodic",
    "Luminous",
    "Radiant",
    "Serenading",
    "Inspiring",
    "Breathtaking",
    "Enigmatic",
    "Dreamlike",
    "Enchanted",
    "Stunning",
    "Meditative",
    "Transcendent",
    "Magical",
    "Celestial",
    "Elegant"
]

symbols = [
    "`",
    "~",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "=",
    "+",
    "/",
    "[",
    "]",
    ":",
    ";",
    "'",
    '"',
    "{",
    "}",
    "|",
    "<",
    ">",
    ",",
    ".",
    "?"
]

def setup_haiku():
    
    haiku = []

    line_patterns = [
        [nouns, verbs, nouns],
        [adjectives, nouns, verbs, adjectives, nouns],
        [adjectives, nouns, verbs, nouns],
    ]

    syllables_per_line = [5, 7, 5]

    for pattern, syllables in zip(line_patterns, syllables_per_line):
        
        line = generate_line(pattern, syllables)
        haiku.append(line.capitalize())

    return haiku

def generate_line(pattern, syllables):
    
    line = []
    line_syllables = 0

    while line_syllables < syllables:
        
        word = random.choice(pattern)
        
        if isinstance(word, list): word = random.choice(word)
            
        word_syllables = count_syllables(word)
        
        if line_syllables + word_syllables <= syllables:
            
            line.append(word)
            line_syllables += word_syllables

    return ' '.join(line)

def count_syllables(word):
    
    vowels = "aeiouy"
    count = 0
    
    word = word.lower()
    
    if word[0] in vowels: count += 1
        
    for index in range(1, len(word)):
        
        if word[index] in vowels and word[index-1] not in vowels: count += 1
            
    if word.endswith("e"): count -= 1
        
    if word.endswith("le") and len(word) > 2 and word [-3] not in vowels: count += 1
        
    return count

def generate_random_username():

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(10, 99)
    symbol = random.choice(symbols)

    username = f"{adjective.capitalize()}{noun.capitalize()}{number}{symbol}"
    
    return username

def generate_random_password():
    
    length = random.randint(8, 12)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def round_nearest(num):
    
    decimal_part = num - int(num)
    
    if decimal_part >= 0.5: return math.ceil(num)
    else: return math.floor(num)

def mph_to_kmh(mph):
    
    kmh = mph * 1.60934
    return round_nearest(kmh)

def kmh_to_mph(kmh):
    
    mph = kmh / 1.60934
    return round_nearest(mph)

def remove_command(command_name): bot.remove_command(command_name)

# remove_command("")

#------------------------------------------------------------------------#

# Bot events

@bot.event
async def on_ready():

    servers = len(bot.guilds)
    
    print(f"{whi}I am up and running ⠕ Logged in as {bot.user}")
    print(cyan + "\n=====================================================\n")
    print(f"{gre}I'm in {servers} servers! {whi}")

    await bot.change_presence(status = nextcord.Status.idle, activity = nextcord.Activity(type = nextcord.ActivityType.watching, name = "your every move 😈"))

@bot.event
async def on_message(x: nextcord.Interaction):
    
    prefixxx = [dev_prefix]
    prefixxxx = [dev_prefix2]

    for i in range(len(prefixxx)):
	
        if prefixxx[i] in x.content:
					
            for j in range(1):
							
                await x.delete()
								
                await x.channel.send("Deleted the dev command so no one else can see it!")

    for k in range(len(prefixxxx)):
	
        if prefixxxx[k] in x.content:
					
            for l in range(1):
							
                await x.delete()
								
                await x.channel.send("Deleted the other dev command so no one else can see it!")
                
    for rick in ["rick_roll", "rickroll"]:
        
        if rick in x.content.lower().split(): 
            
            await x.channel.send("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713")

            await x.channel.send("Haha! Get rickrolled!")

    await bot.process_commands(x)
    
@bot.event
async def on_reaction_add(x, user):
    
    if x.emoji in emoji_dict:
        
        lang_code = emoji_dict[x.emoji]
        message = x.message
        detected_lang = detect(message.content)
        translated_message = mtranslate.translate(message.content, lang_code)
        translated_to = detect(translated_message)
        
        ambed = nextcord.Embed(title = "Translated Text", description = f"{translated_message}", color = nextcord.Color.gold())
        ambed.add_field(name = "Original Text", value = message.content, inline = False)
        ambed.add_field(name = "Translated from:", value = f'{detected_lang.capitalize()}')
        ambed.add_field(name = "Translated to:", value = f'{translated_to.capitalize()}')
        
        await x.message.reply(embed = ambed)

@bot.event
async def on_command_error(x, error):
    
    if isinstance(error, commands.CommandNotFound): await x.channel.send("Command doesn't exist. Please do `/help` to view all commands.")

    else: print(f"{red}error: {error}")

#------------------------------------------------------------------------#

# Dev commands

@bot.command(name = f"{dev_prefix}_glurp") 
async def glurp(x: nextcord.Interaction): await x.channel.send("glarp")

@bot.command(name = f"{dev_prefix2}_addrole", aliases = [f"{dev_prefix}_addrole"])
async def addrole(x, role: nextcord.Role, user: nextcord.Member):

    await user.add_roles(role)
    await x.channel.send(f"Gave the role, {role}, to {user}.")

@bot.command(name = f"{dev_prefix2}_removerole", aliases = [f"{dev_prefix}_removerole"])
async def removerole(x, role: nextcord.Role, user: nextcord.Member):

    await user.remove_roles(role)
    await x.channel.send(f"Removed the role, {role}, to {user}.")

@bot.command(name = f"{dev_prefix}_restart")
async def restart(x):

    await x.channel.send("restarting")
    s("kill 1")

@bot.command(name = f"{dev_prefix}_guilds")
async def guilds(x):

    guild_names = [guild.name for guild in bot.guilds]
    guild_names_str = "\n".join(guild_names)
    
    await x.channel.send(f"Guilds:\n\n{guild_names_str}")

@bot.slash_command(name = "embed_maker", description = "Title, desc, colour (hex format: 000000, not #000000), footer & image URL. Admin perms command only")
async def embed_maker_2000(x: nextcord.Interaction, title: str, colour: str, description: str = None, footer: str = None, url_link_for_image: str = None):

    if x.user.guild_permissions.administrator:
        
        colour_code = "0x" + colour
        color = int(colour_code, 16)
    
        embed_made = nextcord.Embed(title = title, color = color)
    
        if description: embed_made.description = description
        if url_link_for_image: embed_made.set_image(url = url_link_for_image)
        if footer: embed_made.set_footer(text = footer)
    
        await x.send(embed = embed_made)
    
    else: await x.send("You do not have the necessary permissions to use this command.")

#------------------------------------------------------------------------#

# Help Commands

@bot.slash_command(name = "devpanel", description = "Displays the developer panel")
async def devpanel(x: nextcord.Interaction):
    
    devpanel = nextcord.Embed(title = "Dev Panel", description = None, color = 0xff0000)
            
    devpanel.add_field(name = "", value = """
    ```
[devprefix]_purge - Purges 5 messages
[devprefix]_glurp - Sends: "glarp"
[devprefix2]_addrole - Adds a role e.g. [devprefix2]_addrole <role_name> <member>
[devprefix2]_removerole - Removes role e.g. [devprefix2]_removerole <role_name> <member>
[devprefix]_restart - Restarts the bot
[devprefix]_guilds - View the specific guilds I'm in
```""")
    
    await x.send(embed = devpanel)

def che(pagenum = 0, inline = False):

    pagenum = pagenum % len(list(helpme))
    pagetitle = list(helpme)[pagenum]

    embed = nextcord.Embed(color = nextcord.Color.gold(), title = pagetitle)

    for key, val in helpme[pagetitle].items():

        embed.add_field(name = "/" + key, value = val, inline = inline)
        embed.set_footer(text = f"Page {pagenum + 1} of {len(list(helpme))}")
        
    return embed

@bot.slash_command(name = "help", description = "View all the commands in a more neater way.")
async def hlep(x: nextcord.Interaction):

    try:

        cp = 0
        btn = Button(label = "Next >")
        ntb = Button(label = "< Prev")

        async def ncb(interaction):

            nonlocal cp, msg
            
            cp += 1
            await msg.edit(embed = che(pagenum = cp), view = view)

        async def bcn(interaction):

            nonlocal cp, msg
            
            cp -= 1
            await msg.edit(embed = che(pagenum = cp), view = view)

        btn.callback = ncb
        ntb.callback = bcn

        view = View(timeout = 180)
        view.add_item(ntb)
        view.add_item(btn)
        cha = che()
        msg = await x.send(embed = cha, view = view)
        
    except Exception as e: print(f"{red}error sending help embed: {e}")

#------------------------------------------------------------------------#

# Regular commands
        
@bot.slash_command(name = "greet", description = "Greets you.")
async def greet(x: nextcord.Interaction): await x.channel.send(f"Why, hello there, <@{x.user.id}>!")

@bot.slash_command(name = "ping", description = "Pong!")
async def ping(x: nextcord.Interaction): 

    pingmessage = nextcord.Embed(title = ":ping_pong: Pong!", description = None, color = nextcord.Color.gold())

    before = time.monotonic()
        
    pingmessage.add_field(name = "", value = f"**It takes me about ``{round(bot.latency * 1000)}ms`` to respond ⠕ Your latency: ``{round(time.monotonic() - before) * 1000}ms``**")
        
    await x.send(embed = pingmessage)

@bot.slash_command(name = "kame-hame-ha", description = "KAME-HAME-HA!!!")
async def kame_hame_ha(x: nextcord.Interaction):

    msg = await x.send("Kame...")

    time.sleep(2)

    await msg.edit(content = "Hame...")

    time.sleep(2)

    await msg.edit(content = "HA!!")

@bot.slash_command(name = "invite", description = "View my invite link.")
async def infite(x: nextcord.Interaction): await x.send("Invite URL: https://discord.com/oauth2/authorize?client_id=1096876861511970896&permissions=1505856060534&scope=bot%20applications.commands")

#------------------------------------------------------------------------#

# Word commands

@bot.slash_command(name = "quote", description = "View a randomized quote.")
async def quote(x: nextcord.Interaction):
    
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']

    quotee = nextcord.Embed(title = "Here's a random quote!", description = None, color = nextcord.Color.gold())
    quotee.add_field(name = "", value = f"```\n{quote}\n```")
    
    await x.send(embed = quotee)

@bot.slash_command(name = "upper", description = "Put your input in lowercase to make it uppercase.")
async def upper(x: nextcord.Interaction, input: str):     

    try: await x.send(input.upper())
    except: pass

@bot.slash_command(name = "lower", description = "Put your input in uppercase to make it lowercase.")
async def lower(x: nextcord.Interaction, input: str):    

    try: await x.send(input.lower())
    except: pass

@bot.slash_command(name = "language", description = "Do the command for more instructions.")
async def lang(x: nextcord.Interaction): 
    
    await x.send("React to any message with a flag of a place, and it converts it to the flags' language.")

    kkak = nextcord.Embed(title = "All Languages", description = None, color = nextcord.Color.gold())
    
    kkak.add_field(name = "", value = f"""
🇺🇸: English
🇩🇪: German
🇫🇷: French
🇪🇸: Spanish
🇮🇹: Italian
🇵🇹: Portuguese
🇷🇺: Russian
🇦🇱: Albanian
🇸🇦: Arabic
🇧🇦: Bosnian
🇧🇬: Bulgarian
🇨🇳: Chinese (Simplified)
🇭🇷: Croatian
🇨🇿: Czech
🇩🇰: Danish
🇪🇪: Estonian
🇫🇮: Finnish
🇬🇷: Greek
🇭🇺: Hungarian
🇮🇩: Indonesian
🇮🇳: Hindi
🇮🇪: Irish
🇮🇸: Icelandic
🇮🇱: Hebrew
🇯🇵: Japanese
🇰🇷: Korean
🇱🇻: Latvian
🇱🇹: Lithuanian
🇲🇹: Maltese
🇲🇪: Montenegrin
🇳🇱: Dutch
🇳🇴: Norwegian
🇵🇰: Urdu
🇵🇱: Polish
🇵🇹: Portuguese
🇷🇴: Romanian
🇷🇸: Serbian
🇸🇦: Arabic
🇸🇰: Slovak
🇸🇮: Slovenian
🇸🇬: Swedish
🇹🇭: Thai
🇹🇷: Turkish
🇹🇼: Chinese (Traditional)
🇺🇦: Ukrainian
🇻🇦: Latin""")

    await x.send(embed = kkak)

@bot.slash_command(name = "wikipedia", description = "Search for information on Wikipedia.")
async def wiki(x: nextcord.Interaction, search_query: str):
    
    async with aiohttp.ClientSession() as session:
        
        async with session.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{search_query}") as response:
            
            if response.status == 200:
                
                data = await response.json()
                summary = data["extract"]
                title = data["title"]
                url = data["content_urls"]["desktop"]["page"]

                wikibed = nextcord.Embed(title = title, url = url, description = summary, color = nextcord.Color.gold())
                
                await x.send(embed = wikibed)
                
            else:

                errorbed = nextcord.Embed(title = None, description = ":exclamation: Failed to retrieve summary from Wikipedia.", color = 0xff0000)
                await x.send(embed = errorbed)

#------------------------------------------------------------------------#

# Fun commands

@bot.slash_command(name = "heads_or_tails", description = "Heads or tails?")
async def hot(x: nextcord.Interaction): 

    thingy = ["Heads", "Tails"]

    hota = nextcord.Embed(title = "Heads or Tails", description = None, color = nextcord.Color.gold())
    
    hota.add_field(name = "", value = f"""
**I have a choice**
```
{choice(thingy)}
```
""")

    await x.send(embed = hota)
             
@bot.slash_command(name = "apod", description = "View the Astronomy Picture Of the Day")
async def apod(x: nextcord.Interaction):
    
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + key)
    data = response.json()
    
    try:
        
        desc = data["explanation"]
        type = data["media_type"]
        title = data["title"]
        date = data["date"]
        img = data["url"]
        
    except KeyError as e:

        errorbed = nextcord.Embed(title = None, description = ":exclamation: An error occurred while processing the APOD request.", color = 0xff0000)
        await x.send(embed = errorbed)
        
        return

    await x.send(f"*({date})* (media type: {type}) Image / Video:")

    await x.channel.send(img)

    apod_embed = nextcord.Embed(title = title, description = desc, color = nextcord.Color.gold())

    await x.send(embed = apod_embed)

@bot.slash_command(name = "trivia", description = "Get a random trivia question.")
async def trivia(x: nextcord.Interaction):
    
    endpoint = "http://jservice.io/api/random"
    endpoint2 = "http://jservice.io/api/random"

    try:
        
        response = requests.get(endpoint)
        response2 = requests.get(endpoint2)

        if response.status_code == 200:
            
            data = response.json()
            data2 = response2.json()
            
            if data:
                
                question = data[0].get("question")
                answer = data[0].get("answer")
                category = data[0]["category"].get("title")

                answer2 = data2[0].get("answer")

                triviabed = nextcord.Embed(title = "Trivia Question", description = question, color = nextcord.Color.gold())
                triviabed.add_field(name = "Category", value = category, inline = False)

                class trivia_view(View):
                    
                    def __init__(self): super().__init__()

                    @nextcord.ui.button(label = answer, custom_id = "option_1")
                    async def option_1(self, button: nextcord.Button, interaction: nextcord.Interaction): await self.process_answer(button, interaction)

                    @nextcord.ui.button(label = answer2, custom_id = "option_2")
                    async def option_2(self, button: nextcord.Button, interaction: nextcord.Interaction): await self.process_answer(button, interaction)

                    async def process_answer(self, button: nextcord.Button, interaction: nextcord.Interaction):
                        
                        user_answer = button.label
                        correct_answer = answer

                        if user_answer == correct_answer: response = f"Correct answer!  The answer *was* {correct_answer}!"
                            
                        else: response = f"Oops! The correct answer was {correct_answer}."

                        await interaction.response.send_message(response)

                view = trivia_view()

                await x.send(embed = triviabed, view = view)
                
            else: await x.send("Failed to fetch trivia question. Try again later.")
                
        else: await x.send("Failed to fetch trivia question.")
            
    except requests.exceptions.RequestException as e: await x.send(f"Error occurred during API request: {e}")
        
#------------------------------------------------------------------------#

# Server Commands

@bot.slash_command(name = "profile", description = "Either put in someones username to view their profile or just don't put anything to view yours.")
async def profile(x, user: Member = None):

    if user == None: user = x.user
        
    inline = True
    
    embedbedbedbed = nextcord.Embed(title = user.name, color = 0xff0000)

    userdata = {

        "Mention": user.mention,
        "Nick": user.nick,
        "Created at": user.created_at.strftime("%b %d, %Y, %T"),
        "Joined at": user.joined_at.strftime("%b %d, %Y, %T"),
        "Server": user.guild,
        "Top role": user.top_role
        
    }

    for [fieldname, fieldval] in userdata.items(): embedbedbedbed.add_field(name = fieldname + ":", value = fieldval, inline = inline)

    embedbedbedbed.set_footer(text = f"ID: {user.id}")
    embedbedbedbed.set_thumbnail(user.display_avatar)

    await x.send(embed = embedbedbedbed)

@bot.slash_command(name = "serverinfo", description = "View the server's info.")
async def server(x: nextcord.Interaction):
        
    guild = x.user.guild
    a
    embedbedbedbedbed = nextcord.Embed(title = guild.name, color = 0x0080ff)

    serverdata = {

        "Owner": guild.owner.mention,
        "Channels": len(guild.channels),
        "Created at": guild.created_at.strftime("%b %d, %Y, %T"),
        "Members": guild.member_count,
        "Description": guild.description
        
    }

    for [fieldname, fieldval] in serverdata.items(): embedbedbedbedbed.add_field(name = fieldname + ":", value = fieldval, inline = True)

    embedbedbedbedbed.set_footer(text = f"ID: {guild.id}")
    embedbedbedbedbed.set_thumbnail(guild.icon)

    await x.send(embed = embedbedbedbedbed)

@bot.slash_command(name = "servers", description = "View how many servers I'm in.")
async def servers(x: nextcord.Interaction): 

    servers = len(bot.guilds)
    await x.send(f"I'm in {servers} servers!")

# -----------------------------------------------------------------------#

# Miscellaneous Commands

@bot.slash_command(name = "eat", description = "Put in what you want to eat (in quotes), and you eat it!")
async def eat(x: nextcord.Interaction, food: str):

    try:

        eating = ["Num... Num... Num...", "Yum... Yum... Yum...", "Eating... Eating... Eating...", "Munch... Munch... Munch...", "Crunch... Crunch... Crunch..."]
        await x.send(f"You are eating {food}, and your response to it is: {choice(eating)}")

    except: pass

@bot.slash_command(name = "gif", description = "Put in your query to view a GIF from GIPHY.")
async def gif(x: nextcord.Interaction, query):

    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(giphy_key, query, limit = 5, rating = "pg")

        tsil = list(api_response.data)
        fig = choice(tsil)

        await x.send(f"Here's your '{query}' GIF from GIPHY!")
        await x.channel.send(fig.embed_url)

    except ApiException as e:

        errorbed = nextcord.Embed(title = None, description = ":exclamation: Cannot call GIPHY API.", color = 0xff0000)
                
        await x.send(embed = errorbed)

        print(f"{red}cannot call api")

@bot.slash_command(name = "aboutme", description = "View my about me!")
async def aboutme(x: nextcord.Interaction): await x.send("Hello I am PH4NT0M! My creator is dragonprogrammer. I was made for The Dragon Legion. Check out my commands using `/help`!")

@bot.slash_command(name = "meme", description = "Gets a random meme from Reddit.")
async def meme(x: nextcord.Interaction):
    
    try:
        
        async with aiohttp.ClientSession() as cs:
            
            async with cs.get("https://www.reddit.com/r/cleanmemes/new.json?sort=hot") as r:
                
                res = await r.json()
                
                await x.send(res["data"]["children"][randint(0, 25)]["data"]["url"])
                
    except:

        errorbed = nextcord.Embed(title = None, description = ":exclamation: Error processing the request.", color = 0xff0000)
                
        await x.send(embed = errorbed)

#------------------------------------------------------------------------#

# Animal Commands

@bot.slash_command(name = "dog", description = "View a random dog picture.")
async def dogpic(x: nextcord.Interaction):

    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]

    dog_choices = ["Here's your dog picture!", "Woof, woof!", "bark!", "Awww...", "Cute!!", "EPIC DOGGO LOCATED", "Random dog image"]

    embedbed = nextcord.Embed(title = choice(dog_choices), description = None, color = nextcord.Color.gold())

    embedbed.set_image(url = image_link)
    
    await x.send(embed = embedbed)

@bot.slash_command(name = "cat", description = "View a random cat picture.")
async def catpic(x: nextcord.Interaction):

    headers = {"x-api-key": api_key}
    
    async with aiohttp.ClientSession() as session:
        
        async with session.get("https://api.thecatapi.com/v1/images/search", headers = headers) as response:
            
            data = await response.json()
            image = data[0]

    url = image["url"]

    cat_choices = ["Here's your dog picture!", "Meow, meow!", "MEOW", "Awww...", "Cute!!", "EPIC CATTO LOCATED", "Random cat image"]

    embedbedbed = nextcord.Embed(title = choice(cat_choices), color = nextcord.Color.gold())
    embedbedbed.set_image(url = url)

    await x.send(embed = embedbedbed)

@bot.slash_command(name = "fox", description = "Get a random image of a fox.")
async def random_fox(x: nextcord.Interaction):
    
    response = requests.get("https://randomfox.ca/floof/")
    data = response.json()
    image_url = data["image"]

    fox_choices = ["Here's your fox picture!", "Howl, howl!", "SCREECH", "Awww...", "Cute!!", "EPIC FOX LOCATED", "Random fox image"]
    
    foxbed = nextcord.Embed(title = choice(fox_choices), color = nextcord.Color.gold())
    foxbed.set_image(url = image_url)
    
    await x.send(embed = foxbed)

@bot.slash_command(name = "spider", description = "Get a random image of a spider.")
async def search_spider_image(x: nextcord.Interaction):

    url = "https://www.flickr.com/services/rest/"
    params = {
        'method': 'flickr.photos.search',
        'api_key': flickr_api_key,
        'tags': 'spider',
        'format': 'json',
        'nojsoncallback': 1,
        'per_page': 1
    }

    response = requests.get(url, params = params)
    data = response.json()

    if 'photos' in data and data['photos']['total'] > 0:
        
        photo = data['photos']['photo'][0]
        image_url = f"https://live.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}.jpg"

        spider_choices = ["Here's your spider picture!", "Hiss, hiss!", "*bites you*", "Awww...", "Cute!!", "EPIC SPIDER LOCATED", "Random spider image"]

        spiderbed = nextcord.Embed(title = choice(spider_choices), color = nextcord.Color.gold())
        spiderbed.set_image(url = image_url)

        await x.send(embed = spiderbed)
        
    else:

        errorbed = nextcord.Embed(title = None, description = ":exclamation: No spider images found.", color = 0xff0000)
        await x.send(embed = errorbed)

@bot.slash_command(name = "pokemon", description = "Get information about a Pokémon.")
async def pokemon(x: nextcord.Interaction, pokemon_name: str):

    async with aiohttp.ClientSession() as session:
        
        async with session.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}") as response:
            
            if response.status == 200:
                
                data = await response.json()

                name = data['name'].capitalize()
                description = data['species']['url']
                sprite_url = data['sprites']['front_default']

                async with session.get(description) as description_response:
                    
                    if description_response.status == 200:
                        
                        description_data = await description_response.json()
                        flavor_text_entries = description_data['flavor_text_entries']
                        description_text = ""

                        for entry in flavor_text_entries:
                            
                            if entry['language']['name'] == 'en':
                                
                                description_text = entry['flavor_text']
                                break

                        pokebed = nextcord.Embed(title = name, description = description_text, color = nextcord.Color.gold())
                        pokebed.set_image(url = sprite_url)
                        
                        await x.send(embed = pokebed)
                        
                    else: 
                        
                        errorbed = nextcord.Embed(title = None, description = ":exclamation: Failed to retrieve Pokémon information.", color = 0xff0000)
                
                        await x.send(embed = errorbed)
                        print(description_response.status)
                        
            else: 

                errorbed = nextcord.Embed(title = None, description = ":exclamation: Pokémon not found.", color = 0xff0000)
                
                await x.send(embed = errorbed)
                print(response.status)

#------------------------------------------------------------------------#

# Moderation / Admin Commands

@bot.slash_command(name = "kick", description = "Kicks the given user.")
async def kick_user(x: nextcord.Interaction, user: Member, reason: str = None):

    if x.user.guild_permissions.administrator:

        if reason == "": resin = "No reason given"
        else: resin = reason

        await user.kick()
        
        kickbed = nextcord.Embed(title = None, description = f":white_check_mark: User *{user.name}* has been kicked. Reason: {resin}.", color = nextcord.Color.gold())
        
        await x.send(embed = kickbed, ephemeral = True)

    else: await x.send("You do not have the necessary permissions to use this command.", ephemeral = True)

    if user.guild_permissions.administrator: await x.send("You cannot kick an administrator.", ephemeral = True)

    else: pass

@bot.slash_command(name = "ban", description = "Bans a user from the server.")
async def ban_user(x: nextcord.Interaction, user: Member, reason: str = None):
    
    if x.user.guild_permissions.administrator:

        if reason == "": resin = "No reason given"
        else: resin = reason
        
        await user.ban()

        banbed = nextcord.Embed(title = None, description = f":white_check_mark: User *{user.name}* has been banned. Reason: {resin}.", color = nextcord.Color.gold())
        
        await x.send(embed = banbed, ephemeral = True)
        
    else: await x.send("You do not have the necessary permissions to use this command.", ephemeral = True)

    if user.guild_permissions.administrator: await x.send("You cannot ban an administrator.", ephemeral = True)

    else: pass

@bot.slash_command(name = "purge", description = "Purge the amount between 1 - 100.") 
async def purge(x: nextcord.Interaction, amount: str):

    if x.user.guild_permissions.administrator:
    
        try:
            
            amount = int(amount)
            
            if 1 <= amount <= 100:
                
                await x.channel.purge(limit = amount)
                await x.channel.send(f"Purged {amount} message(s)!")
                
            else: await x.channel.send("Please provide a valid amount between 1 and 100.")
                
        except ValueError: await x.channel.send("Please provide a valid number for the amount.")

    else: await x.channel.send("You do not have the necessary permissions to use this command.")

@bot.slash_command(name = "auditlog", description = f"View the last 10 things from the audit log for the server. I need the {a} permission.")
async def audit_log(x: nextcord.Interaction):
    
    if x.user.guild_permissions.administrator:
        
        server = x.guild

        try:
            
            log_entries = await server.audit_logs(limit = 10).flatten()

            auditlogbed = nextcord.Embed(title = "Audit Log", color = nextcord.Color.gold())
            auditlog_description = ""

            for entry in log_entries:
                
                action = entry.action
                user = entry.user
                target = entry.target

                log_entry = f"Action: {action}\nUser: {user}\nTarget: {target}\n\n"
                
                if log_entry is not None: auditlog_description += log_entry

            if auditlog_description: auditlogbed.description = auditlog_description

            await x.send(embed = auditlogbed, ephemeral = True)

        except nextcord.Forbidden: await x.send("I don't have permission to access the audit log.", ephemeral = True)
            
    else: await x.send("You need to be an administrator to use this command.", ephemeral = True)

@bot.slash_command(name = "warn", description = "Warn a user.")
async def warn(x: nextcord.Interaction, user: nextcord.Member, reason: str):
    
    if x.user.guild_permissions.administrator:
        
        if str(user.id) in db['warns']: db['warns'][str(user.id)].append(reason)
        else: db['warns'][str(user.id)] = [reason]
            
        await x.send(f"User {user.mention} has been warned. Reason: {reason}", ephemeral = True)
        
    else: await x.send("You do not have the necessary permissions to use this command.", ephemeral = True)

@bot.slash_command(name = "view_warnings", description = "View a user's warnings.")
async def view_warnings(x: nextcord.Interaction, user: nextcord.Member):
    
    if x.user.guild_permissions.administrator:
        
        if str(user.id) in db['warns']:
            
            warning_list = "\n".join(db['warns'][str(user.id)])
            await x.send(f"User {user.mention} has the following warnings:\n{warning_list}", ephemeral = True)
            
        else: await x.send(f"User {user.mention} has no warnings.", ephemeral = True)
            
    else: await x.send("You do not have the necessary permissions to use this command.", ephemeral = True)

@bot.slash_command(name = "lock", description = "Lock a channel.")
async def lock_channel(x: nextcord.Interaction, channel: nextcord.TextChannel):
    
    guild = x.guild

    if x.user.guild_permissions.administrator:
        
        if channel in guild.channels:

            lockbed = nextcord.Embed(title = ":lock: This channel has been locked!", description = None, color = nextcord.Color.red())

            await channel.send(embed = lockbed)
            
            selected_channel = guild.get_channel(channel.id)

            await selected_channel.set_permissions(guild.default_role, send_messages = False)
            await x.send(f"Channel {selected_channel.mention} has been locked.", ephemeral = True)
            
        else: await x.send("The specified channel does not exist.", ephemeral = True)
            
    else: await x.send("You do not have the necessary permissions to use this command.", ephemeral = True)

@bot.slash_command(name = "unlock", description = "Unlock a channel.")
async def unlock_channel(x: nextcord.Interaction, channel: nextcord.TextChannel):
    
    guild = x.guild

    if x.user.guild_permissions.administrator:
        
        if channel in guild.channels:
            
            selected_channel = guild.get_channel(channel.id)

            await selected_channel.set_permissions(guild.default_role, send_messages = True)
            
            await x.send(f"Channel {selected_channel.mention} has been unlocked.", ephemeral = True)

            unlockbed = nextcord.Embed(title = ":unlock: This channel has been unlocked!", description = None, color = nextcord.Color.green())

            await channel.send(embed = unlockbed)
            
        else: await x.send("The specified channel does not exist.", ephemeral = True)
            
    else: await x.send("You do not have the necessary permissions to use this command.", ephemeral = True)

#------------------------------------------------------------------------#

# Generation Commands

@bot.slash_command(name = "generate_code", description = "Generates \"Hello, world!\" in any coding language. See all supported languages w/ /all_pos_langs.")
async def generate_code(x: nextcord.Interaction, code_type: str):
    
    code_type = code_type.lower()

    def generate_python_code():

        code = """
def hello_world():
    print("Hello, world!")

hello_world()"""

        return code
    
    def generate_java_code():

        code = """
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}"""

        return code
    
    def generate_cpp_code():

        code = """
#include <iostream>
    
int main() {
    std::cout << "Hello, world!" << std::endl;
    return 0;
}"""

        return code
    
    def generate_ruby_code():

        code = """
puts "Hello, world!"""

        return code
    
    def generate_go_code():

        code = """
package main
    
import "fmt"

func main() {
    fmt.Println("Hello, world!")
}"""

        return code
    
    def generate_csharp_code():

        code = """
using System;
    
class Program {
    static void Main(string[] args) {
        Console.WriteLine("Hello, world!");
    }
}"""

        return code
    
    def generate_basic_code():

        code = """
PRINT "Hello, world!"""

        return code
    
    def generate_rust_code():

        code = """
fn main() {
    println!("Hello, world!");
}"""

        return code
    
    def generate_lolcode_code():

        code = """
HAI 1.2
CAN HAS STDIO?
VISIBLE "Hello, world!"
KTHXBYE"""

        return code
    
    def generate_php_code():

        code = """
<?php
echo "Hello, world!";
?>"""

        return code
    
    def generate_javascript_code():

        code = """
console.log("Hello, world!");"""

        return code
    
    def generate_lua_code():

        code = """
print("Hello, world!")"""

        return code
    
    def generate_swift_code():

        code = """
import Swift
    
print("Hello, world!")"""

        return code
    
    def generate_typescript_code():

        code = """
console.log("Hello, world!");"""

        return code
    
    def generate_kotlin_code():

        code = """
fun main() {
    println("Hello, world!")
}"""

        return code
    
    def generate_scala_code():

        code = """
object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello, world!")
  }
}"""

        return code
    
    def generate_perl_code():

        code = """
print "Hello, world!\n";"""

        return code
    
    def generate_shell_code():

        code = """
echo "Hello, world!"""

        return code
    
    def generate_c_code():

        code = """
#include <stdio.h>
    
int main() {
    printf("Hello, world!\n");
    return 0;
}"""

        return code
    
    def generate_objective_c_code():

        code = """
#import <Foundation/Foundation.h>
    
int main(int argc, char * argv[]) {
    @autoreleasepool {
        NSLog(@"Hello, world!");
    }
    return 0;
}"""

        return code
    
    def generate_haskell_code():

        code = """
main :: IO ()
    main = putStrLn "Hello, world!"""

        return code
    
    def generate_sql_code():

        code = """
SELECT 'Hello, world!';"""

        return code
    
    def generate_coffee_script_code():

        code = """
console.log "Hello, world!"""

        return code
    
    def generate_groovy_code():

        code = """
class HelloWorld {
    static void main(String[] args) {
        println "Hello, world!"
    }
}"""

        return code
    
    def generate_fsharp_code():

        code = """
printfn "Hello, world!"""

        return code
    
    def generate_r_code():

        code = """
print("Hello, world!")"""

        return code
    
    def generate_elixir_code():

        code = """
IO.puts "Hello, world!"""

        return code
    
    def generate_matlab_code():

        code = """
disp('Hello, world!');"""

        return code
    
    def generate_vb_net_code():

        code = """
Module HelloWorld
    Sub Main()
        Console.WriteLine("Hello, world!")
    End Sub
End Module"""

        return code
    
    def generate_lua_code():

        code = """
print("Hello, world!")"""

        return code
    
    def generate_groovy_code():

        code = """
class HelloWorld {
    static void main(String[] args) {
        println "Hello, world!"
    }
}"""

        return code
    
    def generate_fortran_code():

        code = """
program HelloWorld
    print *, "Hello, world!"
end program HelloWorld"""

        return code
    
    def generate_scheme_code():

        code = """
(display "Hello, world!")
(newline)"""

        return code
    
    def generate_lisp_code():

        code = """
(defun hello-world ()
    (format t "Hello, world!"))
    
(hello-world)"""

        return code
    
    def generate_dart_code():

        code = """
void main() {
  print('Hello, world!');
}"""

        return code
    
    def generate_prolog_code():

        code = """
:- initialization(main).
main :-
    write('Hello, world!'),
    nl."""

        return code
    
    def generate_cobol_code():

        code = """
IDENTIFICATION DIVISION.
PROGRAM-ID. HELLOWORLD.
PROCEDURE DIVISION.
    DISPLAY 'Hello, world!'.
    STOP RUN."""

        return code
    
    def generate_pascal_code():

        code = """
program HelloWorld;
begin
  writeln('Hello, world!');
end."""

        return code
    
    def generate_shell_code():

        code = """
echo "Hello, world!"""

        return code
    
    def generate_lua_code():

        code = """
print("Hello, world!")"""

        return code
    
    def generate_vim_script_code():

        code = """
echo "Hello, world!"""

        return code
    
    def generate_abap_code():

        code = """
REPORT HelloWorld.
    
WRITE 'Hello, world!'."""

        return code
    
    def generate_autoit_code():

        code = """
MsgBox(0, "", "Hello, world!")"""

        return code
    
    def generate_powershell_code():

        code = """
Write-Host "Hello, world!"""

        return code
    
    def generate_clojure_code():

        code = """
(println "Hello, world!")"""

        return code
    
    def generate_groovy_code():

        code = """
class HelloWorld {
    static void main(String[] args) {
        println "Hello, world!"
    }
}"""

        return code
    
    def generate_smalltalk_code():

        code = """
Transcript show: 'Hello, world!'."""

        return code
    
    def generate_d_code():

        code = """
import std.stdio;
    
void main() {
    writeln("Hello, world!");
}"""

        return code
    
    def generate_verilog_code():

        code = """
module HelloWorld;
  initial
    begin
      $display("Hello, world!");
      $finish;
    end
endmodule"""

        return code
    
    def generate_ruby_code():

        code = """
puts "Hello, world!"""

        return code
    
    def generate_perl_code():

        code = """
print "Hello, world!\n";"""

        return code
    
    def generate_tcl_code():

        code = """
puts "Hello, world!"""

        return code
    
    def generate_golang_code():

        code = """
package main
    
import "fmt"

func main() {
    fmt.Println("Hello, world!")
}"""

        return code
    
    def generate_ada_code():

        code = """
with Ada.Text_IO;
    
procedure HelloWorld is
begin
   Ada.Text_IO.Put_Line("Hello, world!");
end HelloWorld;"""

        return code
    
    def generate_lisp_code():

        code = """
(defun hello-world ()
  (format t "Hello, world!"))

(hello-world)"""

        return code
    
    def generate_pl_sql_code():

        code = """
BEGIN
   DBMS_OUTPUT.PUT_LINE('Hello, world!');
END;"""

        return code
    
    def generate_vbscript_code():

        code = """
WScript.Echo "Hello, world!"""

        return code
    
    def generate_matlab_code():

        code = """
disp('Hello, world!');"""

        return code
    
    def generate_fsharp_code():

        code = """
printfn "Hello, world!"""

        return code
    
    def generate_html_code():

        code = """
<!DOCTYPE html>
<html>
<body>
  <script>
    document.write("Hello, world!");
  </script>
</body>
</html>"""

        return code
    
    def generate_sql_code():

        code = """
SELECT 'Hello, world!';"""

        return code
    
    def generate_css_code():

        code = """
body::before {
  content: "Hello, world!";
}"""

        return code
    
    def generate_yaml_code():

        code = """
message: Hello, world!"""

        return code
    
    def generate_json_code():

        code = """
{
  "message": "Hello, world!"
}"""

        return code
    
    supported_languages = [
        "python",
        "java",
        "cpp",
        "ruby",
        "go",
        "csharp",
        "basic",
        "rust",
        "lolcode",
        "php",
        "javascript",
        "lua",
        "swift",
        "typescript",
        "kotlin",
        "scala",
        "perl",
        "shell",
        "c",
        "objective-c",
        "haskell",
        "sql",
        "coffeescript",
        "groovy",
        "fsharp",
        "r",
        "elixir",
        "matlab",
        "vb.net",
        "lua",
        "groovy",
        "fortran",
        "scheme",
        "lisp",
        "dart",
        "prolog",
        "cobol",
        "pascal",
        "shell",
        "lua",
        "vim-script",
        "abap",
        "autoit",
        "powershell",
        "clojure",
        "groovy",
        "smalltalk",
        "d",
        "verilog",
        "ruby",
        "perl",
        "tcl",
        "golang",
        "ada",
        "lisp",
        "pl/sql",
        "vbscript",
        "matlab",
        "fsharp",
        "html",
        "sql",
        "css",
        "yaml",
        "json"
    ]

    def generate_code(language):
        
        if language not in supported_languages: return None
        
        if language == "python": return generate_python_code()
        elif language == "java": return generate_java_code()
        elif language == "cpp": return generate_cpp_code()
        elif language == "ruby": return generate_ruby_code()
        elif language == "go": return generate_go_code()
        elif language == "csharp": return generate_csharp_code()
        elif language == "basic": return generate_basic_code()
        elif language == "rust": return generate_rust_code()
        elif language == "lolcode": return generate_lolcode_code()
        elif language == "php": return generate_php_code()
        elif language == "javascript": return generate_javascript_code()
        elif language == "lua": return generate_lua_code()
        elif language == "swift": return generate_swift_code()
        elif language == "typescript": return generate_typescript_code()
        elif language == "kotlin": return generate_kotlin_code()
        elif language == "scala": return generate_scala_code()
        elif language == "perl": return generate_perl_code()
        elif language == "shell": return generate_shell_code()
        elif language == "c": return generate_c_code()
        elif language == "objective-c": return generate_objective_c_code()
        elif language == "haskell": return generate_haskell_code()
        elif language == "sql": return generate_sql_code()
        elif language == "coffeescript": return generate_coffee_script_code()
        elif language == "autoit": return generate_autoit_code()
        elif language == "groovy": return generate_groovy_code()
        elif language == "fsharp": return generate_fsharp_code()
        elif language == "r": return generate_r_code()
        elif language == "d": return generate_d_code()
        elif language == "elixir": return generate_elixir_code()
        elif language == "matlab": return generate_matlab_code()
        elif language == "vb.net": return generate_vb_net_code()
        elif language == "tcl": return generate_tcl_code()
        elif language == "golang": return generate_golang_code()
        elif language == "ada": return generate_ada_code()
        elif language == "lisp": return generate_lisp_code()
        elif language == "pl/sql": return generate_pl_sql_code()
        elif language == "vbscript": return generate_vbscript_code()
        elif language == "html": return generate_html_code()
        elif language == "css": return generate_css_code()
        elif language == "yaml": return generate_yaml_code()
        elif language == "json": return generate_json_code()
    
    code = generate_code(code_type)
    
    if code:

        code_embed = nextcord.Embed(title = f"Generated {code_type.capitalize()} Code", description = f"```{code_type}\n{code}\n```", color = nextcord.Color.gold())

        await x.send(embed = code_embed)
    
    else:

        available_languages = [
            "Python", 
            "Java", 
            "CPP", 
            "Ruby", 
            "Go", 
            "Csharp", 
            "Basic", 
            "Rust", 
            "LOLCODE", 
            "PHP", 
            "JavaScript",
            "Lua", 
            "Swift",
            "TypeScript",
            "Kotlin",
            "Scala",
            "Perl", 
            "Shell",
            "C",
            "Objective-C",
            "Haskell", 
            "SQL",
            "CoffeeScript",
            "Groovy", 
            "Fsharp",
            "R", 
            "Elixir",
            "Matlab",
            "VB.NET",
            "Fortran", 
            "Scheme", 
            "Lisp", 
            "Dart", 
            "Prolog",
            "COBOL",
            "Pascal",
            "Vim-Script", 
            "ABAP", 
            "AutoIt",
            "PowerShell",
            "Clojure", 
            "Smalltalk", 
            "D",
            "Verilog",
            "Tcl",
            "Golang", 
            "Ada", 
            "PL/SQL",
            "VBScript",
            "HTML", 
            "CSS",
            "YAML", 
            "JSON"
        ]
    
        available_languages_str = ", ".join(available_languages)

        ct = f'"{code_type}"'

        errorbed = nextcord.Embed(title = "Invalid Language", description = f":exclamation: The provided language {ct} is not supported. Please choose from the following available languages: {available_languages_str}.", color = 0xff0000)
        
        await x.send(embed = errorbed)

@bot.slash_command(name = "all_pos_langs", description = "View all possible languages for the /generate_code command.")
async def apl(x: nextcord.Interaction):

    available_langs = [
            "Python", 
            "Java", 
            "CPP", 
            "Ruby", 
            "Go", 
            "Csharp", 
            "Basic", 
            "Rust", 
            "LOLCODE", 
            "PHP", 
            "JavaScript",
            "Lua", 
            "Swift",
            "TypeScript",
            "Kotlin",
            "Scala",
            "Perl", 
            "Shell",
            "C",
            "Objective-C",
            "Haskell", 
            "SQL",
            "CoffeeScript",
            "Groovy", 
            "Fsharp",
            "R", 
            "Elixir",
            "Matlab",
            "VB.NET",
            "Fortran", 
            "Scheme", 
            "Lisp", 
            "Dart", 
            "Prolog",
            "COBOL",
            "Pascal",
            "Vim-Script", 
            "ABAP", 
            "AutoIt",
            "PowerShell",
            "Clojure", 
            "Smalltalk", 
            "D",
            "Verilog",
            "Tcl",
            "Golang", 
            "Ada", 
            "PL/SQL",
            "VBScript",
            "HTML", 
            "CSS",
            "YAML", 
            "JSON"
        ]

    langbed = nextcord.Embed(title = "All Supported Languages:", description = None)

    chunk_size = 25

    for i in range(0, len(available_langs), chunk_size):
        
        chunk = available_langs[i : i + chunk_size]
        values = "\n".join(chunk)
        langbed.add_field(name = values, value = "", inline = True)

    await x.send(embed = langbed)

@bot.slash_command(name = "shore", description = "Generate a shore with land and water. Maximum width and height: 10.")
async def generate_shore(x: nextcord.Interaction, width: int = 10, height: int = 10):
    
    if width > 10 or height > 10:

        errorbed = nextcord.Embed(title = "Size too big", description = ":exclamation: Maximum width and height allowed is 10.", color = 0xff0000)
        
        await x.send(embed = errorbed)
        
        return

    land_emoji = "🟩"
    water_emoji = "🟦"

    shore = []
    
    for i in range(height):
        
        row = [land_emoji if random.random() < 0.5 else water_emoji for j in range(width)]
        shore.append(row)

    shore_text = "\n".join("".join(row) for row in shore)
    
    await x.send(f"{shore_text}")

@bot.slash_command(name = "haiku", description = "Generate a haiku.")
async def generate_haiku(x: nextcord.Interaction):
    
    haiku = setup_haiku()
    haiku_text = "\n".join(haiku)
    
    await x.send(f"""Here's a haiku:\n
```fix
{haiku_text}
```""")
    
@bot.slash_command(name = "username", description = "Generate a random username.")
async def generate_username(x: nextcord.Interaction):
    
    username = generate_random_username()
    
    await x.send(f"Here's a random username: {username}")

@bot.slash_command(name = "password", description = "Generate a random password.")
async def generate_password(x: nextcord.Interaction):
    
    password = generate_random_password()
    
    await x.send(f"Here's a random password: ||{password}||")

#------------------------------------------------------------------------#

# Math Commands

@bot.slash_command(name = "calculator", description = "Put the equation.")
async def calc(x: nextcord.Interaction, equation: str):

    def evaluate_expression(expression):
        
        result = eval(expression)
        return result

    calc = nextcord.Embed(title = equation, description = None, color = nextcord.Color.gold())
        
    calc.add_field(name = "", value = f"""
**Answer:**

{evaluate_expression(equation)}

""")
    await x.send(embed = calc)

@bot.slash_command(name = "mph_to_kmh", description = "Convert Miles per Hour to Kilometers per hour.")
async def mphkmh(x: nextcord.Interaction, mph: float):

    result = mph_to_kmh(mph)
    await x.send(result)

@bot.slash_command(name = "kmh_to_mph", description = "Convert Kilometers per Hour to Miles per hour.")
async def kmhmph(x: nextcord.Interaction, kmh: float):

    result = kmh_to_mph(kmh)
    await x.send(result)

#------------------------------------------------------------------------#

bot.run(token)
