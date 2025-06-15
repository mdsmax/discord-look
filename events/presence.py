from utils.logger import logar
import discord

async def handle_presence(before: discord.User, after: discord.User, id_monitorado: int):
    if after.id == id_monitorado:
        logar(f"Status alterado: {after.name} — {before.status} > {after.status}")