import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask
from threading import Thread

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user.name}')

@bot.command()
async def sussyhelp(ctx):
    help_text = (
        "**🕵️‍♂️ SussyComentor Commands:**\n"
        "`❗!sussyhelp` – Show this help message\n"
        "`❗!comment` – Brutally sarcastic comment on a message\n"
        "`❗!roast` – Ruthless roast of a replied message\n"
        "`❗!memecomment` – Savage meme-style insult\n"
        "`❗!SUSpercentage` – Rate sus level (1–100%)"
    )
    await ctx.send(help_text)

async def generate_ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Error with Gemini:", e)
        return "Oops! My Gemini brain just glitched. Try again later."

@bot.command()
async def comment(ctx):
    if ctx.message.reference:
        replied_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        user = replied_msg.author.mention
        prompt = (
            f"Write a brutally sarcastic, highly rude, and insulting comment about this message: "
            f"\"{replied_msg.content}\". Be extremely disrespectful and savage, like a toxic gamer roasting someone on Discord."
        )
        comment = await generate_ai_response(prompt)
        await ctx.send(f"{user} {comment}")
    else:
        await ctx.send("❗ Please reply to a message with `!comment`.")

@bot.command()
async def roast(ctx):
    if ctx.message.reference:
        replied_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        user = replied_msg.author.mention
        prompt = (
            f"Roast this message with maximum sarcasm, rudeness, and dark humor: "
            f"\"{replied_msg.content}\". Be as brutally honest and funny as possible, like you're humiliating them in front of the entire server."
        )
        roast = await generate_ai_response(prompt)
        await ctx.send(f"{user} {roast}")
    else:
        await ctx.send("❗ Please reply to a message with `!roast`.")

@bot.command()
async def memecomment(ctx):
    if ctx.message.reference:
        replied_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        user = replied_msg.author.mention
        prompt = (
            f"Generate a meme-style, exaggerated, over-the-top, savage and toxic comment for this message: "
            f"\"{replied_msg.content}\". Use Gen Z humor, emoji, all caps, and be hilariously rude. The goal is to make the person look stupid in the funniest way possible."
        )
        meme_reply = await generate_ai_response(prompt)
        await ctx.send(f"{user} {meme_reply}")
    else:
        await ctx.send("❗ Please reply to a message with `!memecomment`.")

@bot.command()
async def SUSpercentage(ctx):
    percent = random.randint(1, 100)
    await ctx.send(f"{percent}% sus 😳")

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Start webserver + bot
keep_alive()
bot.run(DISCORD_TOKEN)
