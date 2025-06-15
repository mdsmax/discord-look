import os
import discord
from utils.logger import logar

banner = r"""
     _     __  
    ( \   /  \  developed by guilherme
     ) )_(_/\_) https://mdsmax.dev
    (_/(_)     
"""

async def handle_ready(client: discord.Client, ID_MONITORADO: int):
    os.system('cls' if os.name == "nt" else 'clear')
    print()
    print(banner)
    print()

    # informações da conta principal
    logar(f"Conectado como {client.user} (ID: {client.user.id})")

    # informações da conta monitorada
    usuario = client.get_user(ID_MONITORADO)
    if not usuario:
        try:
            usuario = await client.fetch_user(ID_MONITORADO)
        except:
            usuario = None

    nome_monitorado = usuario.name if usuario else "Desconhecido"
    logar(f"Monitorando o usuário {nome_monitorado} (ID: {ID_MONITORADO})")