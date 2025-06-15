from utils.logger import logar
import discord

async def handle_message_delete(message: discord.Message, id_monitorado: int):
    if message.author.id == id_monitorado:
        logar(f"{message.author.name} deletou uma mensagem: {message.content[:100]} - {message.id}")
