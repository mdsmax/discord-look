# Discord Presence Monitor

Ferramenta em Python para monitorar a presença, status e atividade de um usuário específico no Discord, usando uma conta de usuário (token selfbot).

---

## 🚨 Aviso de Responsabilidade

**IMPORTANTE:**  
Esta ferramenta é desenvolvida **apenas para fins educacionais e testes pessoais**. O uso para monitorar terceiros sem consentimento é **estritamente proibido** e pode violar os Termos de Serviço do Discord, além de leis locais de privacidade.  

Você é o único responsável pelo uso deste software.  
Por favor, utilize com ética e respeito à privacidade das pessoas.

---

## ⚙️ Funcionalidades

- Monitoramento de status online/offline do usuário alvo  
- Detecção de alterações no nome, avatar e banner do usuário monitorado  
- Notificação de mensagens enviadas, editadas e deletadas pelo usuário  
- Aviso quando o usuário começa a digitar em canais  
- Detecção de adição ou remoção de amizade  
- Logs organizados e separados por evento  
- Modularidade com código dividido em arquivos para fácil manutenção  

---

## 🛠️ Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seuusuario/discord-presence-monitor.git
cd discord-presence-monitor
```

2. Crie um ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ⚡ Como usar

1. Abra o arquivo `config.json` e preencha com seu token de usuário e o ID do usuário que deseja monitorar.

2. Execute o script principal:

```bash
python main.py
```

3. Acompanhe os logs no terminal e em arquivos (se configurado).

---

## 📁 Estrutura do Projeto

- `main.py` — arquivo principal que inicia o bot  
- `events/` — módulos com handlers para eventos do Discord  
- `utils/` — funções utilitárias, como validação de token e logging  
- `config.json` — configurações do usuário e do alvo  

---

## ⚠️ Avisos Legais

- Este projeto usa a API Discord de forma não oficial (selfbot) e pode resultar em banimento da conta usada para login.  
- Use com cautela e apenas com contas de teste ou sob total controle.  
- O autor não se responsabiliza por mau uso ou consequências legais.

---

## 📬 Contato

Se precisar de ajuda ou quiser colaborar, abra uma issue ou me envie uma mensagem.

---

**Obrigado por usar o Discord Presence Monitor!**
