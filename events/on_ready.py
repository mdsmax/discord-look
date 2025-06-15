import os
import discord
from utils.logger import logar

banner = r"""
     _     __  
    ( \   /  \  developed by guilherme
     ) )_(_/\_) https://mdsmax.dev
    (_/(_)     
"""

async def handle_ready(client: discord.Client, ids_monitorados):
    os.system('cls' if os.name == "nt" else 'clear')
    print()
    print(banner)
    print()

    # informações da conta principal
    logar(f"Conectado como {client.user} (ID: {client.user.id})")

    # informações da conta monitorada
    for uid in ids_monitorados:
        user = await client.fetch_user(uid)
        logar(f"Monitorando {user.name} (ID: {uid})")