import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import google.generativeai as genai
import asyncio

load_dotenv()

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
    print(f"Mensagem recebida: {message.content}")
    await bot.process_commands(message)

@bot.command()
async def teste(ctx):
    await ctx.send("Olá! Estou funcionando! 🎉")

with open("personality.txt", "r", encoding="utf-8") as f:
    personality = f.read()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

bot.run(os.getenv("DISCORD_TOKEN") 
