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

intents = discord.Intents.default()
intents.message_content = True

@bot.event
async def on_ready():
    print(f"{bot.user} está online!")

@bot.event
async def on_message(message):
    # Ignora mensagens de bots
    if message.author.bot:
        return

    # Responde apenas se for mencionada ou escreverem "yelaine"
    if bot.user in message.mentions or "yelaine" in message.content.lower():

        prompt = f"""
{personality}

Mensagem do usuário:
{message.author.display_name}: {message.content}
"""

        try:
            response = model.generate_content(prompt)
            await message.channel.send(response.text)

        except Exception as e:
            print(e)
            await message.channel.send("Desculpe... aconteceu um erro ao pensar. 😔")

    # Mantém os comandos funcionando
    await bot.process_commands(message)


@bot.command()
async def teste(ctx):
    await ctx.send("Olá! Estou funcionando! 🎉")


bot.run(os.getenv("DISCORD_TOKEN"))
