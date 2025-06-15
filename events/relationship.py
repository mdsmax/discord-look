from utils.logger import logar

async def handle_relationship_add(relationship, ids_monitorados):
    if relationship.user.id in ids_monitorados:
        logar(f"[AMIZADE] {relationship.user.name} ({relationship.user.id}) virou seu amigo.")

async def handle_relationship_remove(relationship, ids_monitorados):
    if relationship.user.id in ids_monitorados:
        logar(f"[AMIZADE] {relationship.user.name} ({relationship.user.id}) removeu a amizade.")
