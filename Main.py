import discord # type: ignore
from discord.ext import commands # type: ignore
import aiohttp
import json
############## Animals #################
import bin.FunnyPets as FunnyPets
from bin.FunnyPets import CatAPI1
from bin.FunnyPets import DogAPI1
############## Memes ###################
import bin.SingSongs as SingSongs
from bin.SingSongs import Sing
############# Dolar API ################
import bin.DolarAPI
from bin.DolarAPI import Money

sing = SingSongs.Sing()
Cat1 = CatAPI1()
Dog1 = DogAPI1()
Money1 = Money()
# Definindo o token do seu bot (substitua pelo seu próprio token)
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

#------------------------------------------------------------------------------------------------------------------------------------
#                                    EVENTOS DE TEXTO
#------------------------------------------------------------------------------------------------------------------------------------
#------- Sing event

@bot.event
async def on_message(message):
    print(message)
    if message.author == bot.user:
        return  # Evita que o bot responda a si mesmo
    #------------------ Memes
    if 'never gonna give you up' in message.content.lower(): 
        await sing.NeverGonnaGiveYouUp(message)
    #------------------ Dogs
    if 'quero um gato' in message.content.lower():
        await Cat1.catGet1(message)
    if 'quero muitos gatos' in message.content.lower():
        await Cat1.catGet10(message)
    if 'quero um cachorro' in message.content.lower():
        await Dog1.DogGet1(message)
    if 'quero muitos cachorros' in message.content.lower():
        await Dog1.DogGet10(message)
    #---------------- Dolar
    if 'cotação de hoje' or 'cotação hoje' or 'dolar hoje'in message.content.lower():
        await Money1.Cotacao(message)

    await bot.process_commands(message)  # Garante que os comandos sejam processados corretaments
    
# Rodando o bot com o token fornecido
bot.run(TOKEN) # type: ignore
