import os
import discord
from discord.ext import commands

CHANNEL_ID = 1337092534152728667

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

**§6 Anweisungen des Teams befolgen**  
Admins und Moderatoren haben das letzte Wort. **Folge ihren Anweisungen**, um den Server fair und sicher zu halten.  

**§9 Datenschutz & Sicherheit**  
Teile **keine privaten Informationen** wie Adressen, Telefonnummern oder Passwörter.  

**§10 Sprache & Verhalten**  
Halte dich an die **Hauptsprache des Servers** und vermeide unnötige Provokationen oder Streitigkeiten.  

**§11 Melde Verstöße**  
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
        # Löscht alle Nachrichten im Channel
        await channel.purge()

        # Sendet die neue Nachricht mit Regeln
        await channel.send("⚖️ **Serverregeln** \n\n" + rules)

#twichtig für alles
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "OK", 200  # Antwort für den Health-Check

def run_webserver():
    app.run(host="0.0.0.0", port=8000)

# Starte den Webserver in einem eigenen Thread
threading.Thread(target=run_webserver, daemon=True).start()

bot.run(os.getenv("DISCORD_TOKEN"))
