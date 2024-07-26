import json
import aiohttp

class Money:
    async def Cotacao(self, message):
        
        LinkAPI = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

        async with aiohttp.ClientSession() as session:
            async with session.get(linkAPI) as response:
                if response.status == 200:
                    data = await response.json()
                    with open('cache/dataDolarAPI.json', 'w') as f:
                        json.dump(data, f, indent=2)

                    with open('cache/DolarAPI.json', 'r') as f:
                        data = json.load(f)
                        await message.channel.send('*Cotaç: *')
                        for i in data:
                            await message.channel.send(f"{i['url']}")
                else:
                    print(f"Erro na requisição: {response.status}")
