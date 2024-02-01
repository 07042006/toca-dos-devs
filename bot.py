import discord
import asyncio
import requests
from bs4 import BeautifulSoup

TOKEN = 'DIGITE_SEU_TOKEN_AQUI'
canal_id = 0000000000000000000  # substitua pelo ID do seu canal

# Configurações de tempo
intervalo = 8 * 60 * 60  # Intervalo em segundos (8 horas)

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print('Bot conectado como {0.user}'.format(client))
    canal = client.get_channel(canal_id)  # Obtém o canal pelo ID
    if canal:
        await enviar_mensagem_periodicamente(canal)  # Envia a mensagem no canal periodicamente

# Função para enviar a mensagem periodicamente
async def enviar_mensagem_periodicamente(canal):

    counter07042006 = ''

    # URLs
    url07042006 = "https://github.com/07042006?tab=overview&from=2024-02-01&to=2024-02-01"

    while True:

        response = requests.get(url07042006)
        # Verifica se a solicitação foi bem sucedida
        if response.status_code == 200:
            # Analisa o conteúdo HTML
            soup = BeautifulSoup(response.text, "html.parser")
            # Encontra o elemento com a classe específica
            contribution_element = soup.find("h2", class_="f4 text-normal mb-2")
            # Extrai o texto do elemento
            contributions_text = contribution_element.text.strip()
            # Extrai o número de contribuições
            contributions_number = contributions_text.split()[0]
            counter07042006 = contributions_number;
            print("07042006:", counter07042006)
        else:
            print("Falha ao acessar a página:", response.status_code)

        texto_contribuicoes = f"""
        ![Hora do Café](https://i.pinimg.com/originals/1a/56/ea/1a56eaaaf78869d7c6e0e620b2b98394.gif)

        :coffee:  **Coffee Time - GitHub Members Contributions**

        **:white_check_mark:  Bruno Nascimento - 07042006 | @brunofox_**
        **Total {counter07042006} contributions in 2024**
        
        By **Bruno** - próximo updade em 8 horas
        """

        await canal.send(texto_contribuicoes) # Envia a mensagem no canal
        await asyncio.sleep(intervalo)  # Espera o intervalo especificado

# Inicia o bot
async def main():
    await client.start(TOKEN)  # Inicializa o cliente com o token

# Roda o bot
asyncio.run(main())