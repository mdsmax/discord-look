from utils.logger import logar
import discord

async def handle_typing(channel: discord.abc.Messageable, user: discord.User, when, id_monitorado: int):
    if user.id == id_monitorado:
        contexto = f"{channel.guild.name}/{channel.name}" if hasattr(channel, "guild") else "DM"
        logar(f"{user.name} está digitando em {contexto}")
