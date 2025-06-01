import discord
from discord.ext import commands
import openai
import os
import random
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Set up intents and bot
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
        "`❗!comment` – Funny comment on a message\n"
        "`❗!roast` – Roast of replied message \n"
        "`❗!memecomment` – Meme-style over-the-top AI response\n"
        "`❗!SUSpercentage` – Rate sus level (1–100%)"
    )
    await ctx.send(help_text)

async def generate_ai_response(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You're a funny and sarcastic Discord bot who comments like a meme lord."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=80,
            temperature=0.95
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Error with OpenAI:", e)
        return "Oops! My AI brain tripped. Try again later."

@bot.command()
async def comment(ctx):
    if ctx.message.reference:
        replied_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        user = replied_msg.author.mention
        prompt = f"Write a witty and sarcastic comment about this message: \"{replied_msg.content}\""
        comment = await generate_ai_response(prompt)
        await ctx.send(f"{user} {comment}")
    else:
        await ctx.send("❗ Please reply to a message with `!comment`.")

@bot.command()
async def roast(ctx):
    if ctx.message.reference:
        replied_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        user = replied_msg.author.mention
        prompt = f"Roast this message in a sarcastic and humorous way: \"{replied_msg.content}\""
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
            f"Generate a meme-style, exaggerated, over-the-top humorous comment for this message: "
            f"\"{replied_msg.content}\". Use Gen Z humor, emoji, caps if needed."
        )
        meme_reply = await generate_ai_response(prompt)
        await ctx.send(f"{user} {meme_reply}")
    else:
        await ctx.send("❗ Please reply to a message with `!memecomment`.")

@bot.command()
async def SUSpercentage(ctx):
    percent = random.randint(1, 100)
    await ctx.send(f"{percent}% sus 😳")

bot.run(DISCORD_TOKEN)
