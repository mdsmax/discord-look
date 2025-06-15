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
        ID_MONITORADO = int(config["id_alvo"])
    except: print("O ID para ser monitorado fornecido não é válido."); exit()
    if TOKEN == "" or ID_MONITORADO == "":
        print("É necessário configurar o 'config.json' antes de usar a tool.")

client = discord.Client()

###############################################################################################
#  _______                     __               
# |    ___|.--.--.-----.-----.|  |_.-----.-----.
# |    ___||  |  |  -__|     ||   _|  _  |__ --|
# |_______| \___/|_____|__|__||____|_____|_____|


@client.event
async def on_ready():
    await handle_ready(client, ID_MONITORADO)

@client.event
async def on_presence_update(before, after):
    await handle_presence(before, after, ID_MONITORADO)

@client.event
async def on_message(message):
    await handle_message(message, ID_MONITORADO)

@client.event
async def on_user_update(before, after):
    await handle_user_update(before, after, ID_MONITORADO)

@client.event
async def on_relationship_add(relationship):
    await handle_relationship_add(relationship, ID_MONITORADO)

@client.event
async def on_relationship_remove(relationship):
    await handle_relationship_remove(relationship, ID_MONITORADO)

@client.event
async def on_typing(channel, user, when):
    await handle_typing(channel, user, when, ID_MONITORADO)

@client.event
async def on_message_edit(before, after):
    await handle_message_edit(before, after, ID_MONITORADO)

@client.event
async def on_message_delete(message):
    await handle_message_delete(message, ID_MONITORADO)


###############################################################################################

async def main():
    if not await validar_token(client, TOKEN):
        return

    if not await pode_monitorar(client, ID_MONITORADO):
        return

    await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())