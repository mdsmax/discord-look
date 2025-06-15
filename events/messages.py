from utils.logger import logar
import discord

async def handle_message(message: discord.Message, id_monitorado: int):
    if message.author.id == id_monitorado:
        contexto = f"{message.guild.name} / {message.channel.name}" if message.guild else "DM"
        logar(f"{message.author.name} enviou mensagem em {contexto}: {message.id}")
