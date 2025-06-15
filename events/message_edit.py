from utils.logger import logar

async def handle_message_edit(before, after, ids_monitorados):
    if before.author.id not in ids_monitorados:
        return

    contexto = f"{before.guild.name} / {before.channel.name}" if before.guild else "DM"
    logar(f"[EDIT] {before.author.name} ({before.author.id}) editou mensagem ({before.id}) em {contexto}\n- Antes: {before.content}\n- Depois: {after.content}")
