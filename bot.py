import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import google.generativeai as genai
import asyncio

load_dotenv()

with open("personality.txt", "r", encoding="utf-8") as f:
    personality = f.read()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} está online!")

@bot.event
async def on_message(message):
    # Ignora mensagens de bots
    if message.author.bot:
        return

    await bot.process_commands(message)
    
    # Responde apenas se for mencionada ou escreverem "yelaine"
    if bot.user in message.mentions or "yelaine" in message.content.lower():

        prompt = f"""
{personality}

Mensagem do usuário:
{message.author.display_name}: {message.content}
"""

        try:
            response = chat.send_message(prompt)
            await message.channel.send(response.text)

        except Exception as e:
            print(e)
            await message.channel.send("Desculpe... aconteceu um erro ao pensar. 😔")

@bot.command()
async def teste(ctx):
    await ctx.send("Olá! Estou funcionando! 🎉")

bot.run(os.getenv("DISCORD_TOKEN"))
