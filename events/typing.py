from utils.logger import logar

async def handle_typing(channel, user, when, ids_monitorados):
    if user.id not in ids_monitorados:
        return

    logar(f"[DIGITANDO] {user.name} ({user.id}) está digitando em {channel}.")
