import discord # type: ignore
import SingSongs
from SingSongs import Sing
from discord.ext import commands # type: ignore

sing = SingSongs.Sing()

# Definindo o token do seu bot (substitua pelo seu próprio token)
TOKEN = ''

# Definindo os intents que seu bot usará
intents = discord.Intents.default()
intents.messages = True  # Para receber eventos de mensagens
intents.guilds = True    # Para receber eventos relacionados a servidores (guilds)
intents.message_content = True

# Criando uma instância do bot com os intents especificados
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento que indica que o bot está pronto e conectado ao Discord
@bot.event
async def on_ready():
    print(f'Bot está pronto como {bot.user.name}')
    print(f'ID do Bot: {bot.user.id}')

# Evento para responder com "Pong!" ao receber "ping" em qualquer mensagem de texto
@bot.event
async def on_message(message):
    print(message)
    if message.author == bot.user:
        return  # Evita que o bot responda a si mesmo

    if 'never gonna give you up' in message.content.lower():
        await sing.NeverGonnaGiveYouUp(message)

    await bot.process_commands(message)  # Garante que os comandos sejam processados corretamente

# Rodando o bot com o token fornecido
bot.run(TOKEN)
