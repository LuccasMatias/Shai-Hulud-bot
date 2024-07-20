import json
import aiohttp


class CatAPI1:
    async def catGet1(self, message):
        linkAPI = 'https://api.thecatapi.com/v1/images/search'
        
        async with aiohttp.ClientSession() as session:
            async with session.get(linkAPI) as response:
                if response.status == 200:
                    data = await response.json()
                    with open('cache/dataCatAPI.json', 'w') as f:
                        json.dump(data, f, indent=2)

                    with open('cache/dataCatAPI.json', 'r') as f:
                        data = json.load(f)
                        await message.channel.send('Aqui está um gatinho para você :heart_eyes_cat: ')
                        for i in data:
                            await message.channel.send(f"{i['url']}")
                else:
                    print(f"Erro na requisição: {response.status}")


    async def catGet10(self, message):
        linkAPI = 'https://api.thecatapi.com/v1/images/search?limit=10'
        
        async with aiohttp.ClientSession() as session:
            async with session.get(linkAPI) as response:
                if response.status == 200:
                    data = await response.json()
                    with open('cache/dataCatAPI.json', 'w') as f:
                        json.dump(data, f, indent=2)

                    with open('cache/dataCatAPI.json', 'r') as f:
                        data = json.load(f)
                        await message.channel.send('então RECEBA !!! METEORO DE FOFURA !!!! :heart_eyes_cat: ')
                        for i in data:
                            await message.channel.send(f"{i['url']}")
                else:
                    print(f"Erro na requisição: {response.status}")

