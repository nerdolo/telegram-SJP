'''
class for taking words' definitions from sjp.pwn.pl
'''
import aiohttp
from bs4 import BeautifulSoup
import json
import urllib.parse



class SJP:
    def __init__(self):
        self.sess = aiohttp.ClientSession()

    async def close(self):
        await self.sess.close()

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def get_autocomplete(self, query):
        async with self.sess.get('https://sjp.pwn.pl/complete.php?source=autocomplete-sjp&query=' + urllib.parse.quote_plus(query)) as r:
            txt = await r.text()
            js = json.loads(txt)
            return [i['value'] for i in js]

    async def get_definition(self, word):
        async with self.sess.get('https://sjp.pwn.pl/szukaj/' + urllib.parse.quote_plus(word) + '.html') as r:
            soup = BeautifulSoup(await r.text(), 'html.parser')
            sjp_results = soup.find("div", attrs={"class": "sjp-wyniki"})
            return sjp_results.find(attrs={"class": "entry-body"}).get_text().strip().replace('\xa0', ' ') if sjp_results is not None else None
