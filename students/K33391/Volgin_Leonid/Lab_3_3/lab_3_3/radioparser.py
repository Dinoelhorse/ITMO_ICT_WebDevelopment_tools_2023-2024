import aiohttp
from radio_models import *
from bs4 import BeautifulSoup

async def save_song(title, song, sion):
    author = song.find('span', class_='artist').get_text()
    name = song.find('span', class_='song').get_text()
    # print(author,': ', name)
    pesnya = Song(name=name, author=author, title=title)
    sion.add(pesnya)
    sion.commit()

async def parse_and_save(url, sion):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.get(url) as response:
                r = await response.text()
                soup = BeautifulSoup(r, 'html.parser')
                print("Listening music from: ",soup.find('title').text)
                title = soup.find('title').text
                songs = soup.find_all('div', class_="name_track")
                for song in songs:
                    try:
                        await save_song(title, song, sion)
                    except Exception as e:
                        pass
    except Exception as ex:
        pass

