from utils.logger import logar
import discord

async def handle_message_edit(before: discord.Message, after: discord.Message, id_monitorado: int):
    if before.author.id == id_monitorado:
        logar(f"{before.author.name} editou uma mensagem: {before.id}")
