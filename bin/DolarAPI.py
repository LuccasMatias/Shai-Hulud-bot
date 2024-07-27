import json
import aiohttp

class Money:
    async def Cotacao(self, message):
        
        linkAPI = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

        async with aiohttp.ClientSession() as session:
            async with session.get(linkAPI) as response: #type:ignore
                if response.status == 200:
                    data = await response.json()
                    with open('cache/dataDolarAPI.json', 'w') as f:
                        json.dump(data, f, indent=2)

                    with open('cache/dataDolarAPI.json', 'r') as f:
                        data = json.load(f)
                        dolar_bid = format(float(data['USDBRL']['bid']), '.2f')
                        euro_bid = format(float(data['EURBRL']['bid']), '.2f')
                        bitcoin_bid = format(float(data['BTCBRL']['bid']), '.2f')

                        await message.channel.send(f'> **Cotação Dolar-Real** R$:{dolar_bid}')
                        await message.channel.send(f'> **Cotação Euro-Real** R$:{euro_bid}')
                        await message.channel.send(f'> **Cotação Bitcoin-Real** R$:{bitcoin_bid}')
                        #await message.channel.send(f"{i['url']}")
                else:
                    print(f"Erro na requisição: {response.status}")
