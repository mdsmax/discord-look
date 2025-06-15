from utils.logger import logar

async def handle_relationship_add(relationship, id_monitorado: int):
    if relationship.user.id == id_monitorado:
        logar(f"O usuário {relationship.user} te adicionou ou foi aceito como amigo.")

async def handle_relationship_remove(relationship, id_monitorado: int):
    if relationship.user.id == id_monitorado:
        logar(f"O usuário {relationship.user} foi removido ou te removeu da lista de amigos.")
