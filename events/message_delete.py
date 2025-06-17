from utils.logger import logar

async def handle_message_delete(message, ids_monitorados):
    if message.author.id not in ids_monitorados:
        return

    logar(f"[DELETE] {message.author.name} ({message.author.id}) deletou mensagem ({message.id}) em {message.channel}: {message.content}")
