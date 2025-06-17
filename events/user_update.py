from utils.logger import logar

async def handle_user_update(before, after, ids_monitorados):
    if before.id not in ids_monitorados:
        return

    if before.avatar != after.avatar:
        logar(f"[AVATAR] {after.name} ({after.id}) trocou o avatar.")

    if before.banner != after.banner:
        logar(f"[BANNER] {after.name} ({after.id}) trocou o banner.")

    if before.name != after.name:
        logar(f"[NOME] Alteração de nome: {before.name} → {after.name} (ID: {before.id})")
