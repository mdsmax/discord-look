from utils.logger import logar
import discord

async def handle_user_update(before: discord.User, after: discord.User, id_monitorado: int):
    if after.id != id_monitorado:
        return

    if before.avatar != after.avatar:
        logar(f"{after.name} mudou o avatar.")

    if before.banner != after.banner:
        logar(f"{after.name} mudou o banner.")

    if before.name != after.name:
        logar(f"Nome alterado: {before.name} > {after.name}")

    if before.discriminator != after.discriminator:
        logar(f"{after.name} mudou o discriminator: {before.discriminator} > {after.discriminator}")