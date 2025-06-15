import discord
from utils.logger import logar

async def validar_token(client, token: str) -> bool:
    try:
        await client.login(token)  # sem bot=False
        return True
    except Exception as e:
        print(f"Erro no login: {e}")
        return False

async def pode_monitorar(client: discord.Client, id_alvo: int) -> bool:
    user = client.get_user(id_alvo)
    if user:
        return True
    try:
        await client.fetch_user(id_alvo)
        return True
    except:
        logar("Não foi possível localizar o usuário. Verifique se ele é amigo ou está em algum servidor em comum.")
        return False
