import datetime
import os

LOG_PATH = "logs/eventos.log"
os.makedirs("logs", exist_ok=True)

def logar(mensagem: str):
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{agora}] {mensagem}"
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(linha + "\n")
    print(f"    {linha}")
