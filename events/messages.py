from utils.logger import logar

async def handle_message(message, ids_monitorados):
    if message.author.id not in ids_monitorados:
        return

    contexto = f"{message.guild.name} / {message.channel.name}" if message.guild else "DM"
    logar(f"[MSG] {message.author.name} ({message.author.id}) enviou uma mensagem em {contexto}: {message.id}")
