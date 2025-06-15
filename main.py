import discord
import json
import os
import asyncio

from utils.validator import validar_token, pode_monitorar
from events.on_ready import handle_ready
from events.presence import handle_presence
from events.messages import handle_message
from events.user_update import handle_user_update
from events.relationship import handle_relationship_add, handle_relationship_remove
from events.typing import handle_typing
from events.message_edit import handle_message_edit
from events.message_delete import handle_message_delete

with open("config.json") as f:
    config = json.load(f)
    TOKEN = config["token"]

    try:
        IDS_MONITORADOS = [int(i) for i in config["ids_alvo"]]
    except:
        print("IDs de monitoramento inválidos.")
        exit()

    if not TOKEN or not IDS_MONITORADOS:
        print("Configure o 'config.json' com token e ids_alvo antes de usar.")
        exit()

client = discord.Client()

# Eventos
@client.event
async def on_ready():
    await handle_ready(client, IDS_MONITORADOS)

@client.event
async def on_presence_update(before, after):
    await handle_presence(before, after, IDS_MONITORADOS)

@client.event
async def on_message(message):
    await handle_message(message, IDS_MONITORADOS)

@client.event
async def on_user_update(before, after):
    await handle_user_update(before, after, IDS_MONITORADOS)

@client.event
async def on_relationship_add(relationship):
    await handle_relationship_add(relationship, IDS_MONITORADOS)

@client.event
async def on_relationship_remove(relationship):
    await handle_relationship_remove(relationship, IDS_MONITORADOS)

@client.event
async def on_typing(channel, user, when):
    await handle_typing(channel, user, when, IDS_MONITORADOS)

@client.event
async def on_message_edit(before, after):
    await handle_message_edit(before, after, IDS_MONITORADOS)

@client.event
async def on_message_delete(message):
    await handle_message_delete(message, IDS_MONITORADOS)



async def main():
    if not await validar_token(client, TOKEN):
        return

    for id_alvo in IDS_MONITORADOS:
        if not await pode_monitorar(client, id_alvo):
            print(f"⚠️ Não foi possível monitorar o ID {id_alvo}")

    await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
