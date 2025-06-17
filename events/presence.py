from utils.logger import logar

async def handle_presence(before, after, ids_monitorados):
    if after.id not in ids_monitorados:
        return

    if before.status != after.status:
        logar(f"[STATUS] {after.name} ({after.id}) mudou o status: {before.status} > {after.status}")
