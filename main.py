import os
import discord
from discord.ext import commands

# Channel-IDs definieren
CHANNEL_ID = 1337092534152728667
MUSIK_CHANNEL_ID = 1334629595642593311
ALLGEMEIN_CHANNEL_ID = 1334619772536492083

# Erstelle eine Instanz des Bots
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Erforderlich für das Lesen von Nachrichten
bot = commands.Bot(command_prefix="~", intents=intents)

rules = """
**§1 Respekt & Freundlichkeit**  
Behandle alle Mitglieder mit **Respekt**. Beleidigungen, Diskriminierung oder Mobbing sind **strengstens verboten**.  

**§2 Keine Hassrede & Belästigung**  
Jegliche Form von **Rassismus, Sexismus, Homophobie oder andere diskriminierende Äußerungen** werden nicht toleriert.  

**§3 Kein Spam & Werbung**  
Das Spammen von Nachrichten, Emojis oder Links ist **nicht erlaubt**. Werbung für andere Server oder Produkte nur mit Erlaubnis des Teams.  

**§4 Keine NSFW-Inhalte**  
Pornografische, gewalttätige oder anderweitig unangemessene Inhalte sind **streng untersagt**.  

**§5 Keine illegalen Aktivitäten**  
Teile oder fördere keine illegalen Inhalte, Hacks oder Betrugsversuche.  

**§6 Richtige Kanäle nutzen**  
Poste deine Nachrichten **im richtigen Kanal** und halte dich an die jeweiligen Kanalregeln.  

**§7 Anweisungen des Teams befolgen**  
Admins und Moderatoren haben das letzte Wort. **Folge ihren Anweisungen**, um den Server fair und sicher zu halten.  

**§8 Datenschutz & Sicherheit**  
Teile **keine privaten Informationen** wie Adressen, Telefonnummern oder Passwörter.  

**§9 Sprache & Verhalten**  
Halte dich an die **Hauptsprache des Servers** und vermeide unnötige Provokationen oder Streitigkeiten.  

**§10 Melde Verstöße**  
Wenn du siehst, dass jemand gegen die Regeln verstößt, melde es einem **Moderator oder Admin**.  

💡 *Mit dem Beitritt zu diesem Server erklärst du dich mit diesen Regeln einverstanden!*
"""

@bot.event
async def on_ready():
    print(f'Bot ist eingeloggt als {bot.user}')

@bot.command()
async def update(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.purge()
        await channel.send("\u2696\ufe0f **Serverregeln** \n\n" + rules)

@bot.command()
async def musik(ctx):
    channel = bot.get_channel(MUSIK_CHANNEL_ID)
    if channel:
        await channel.purge()
        
@bot.command()
async def allgemein(ctx):
    channel = bot.get_channel(ALLGEMEIN_CHANNEL_ID)
    if channel:
        await channel.purge()

# Wichtiger Health-Check Webserver
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "OK", 200

def run_webserver():
    app.run(host="0.0.0.0", port=8000)

threading.Thread(target=run_webserver, daemon=True).start()

bot.run(os.getenv("DISCORD_TOKEN"))
