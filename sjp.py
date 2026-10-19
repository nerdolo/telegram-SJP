'''
class for taking words' definitions from sjp.pwn.pl
'''
import aiohttp
from bs4 import BeautifulSoup
import urllib.parse


class SJP:
    def __init__(self, sess: aiohttp.ClientSession):
        self.sess = sess

    async def close(self):
        await self.sess.close()

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def get_autocomplete(self, query):
        async with self.sess.get('https://sjp.pwn.pl/api/autocomplete', params={'query': query}) as resp:
            completions = (await resp.json())['hits']['hits']
            return [item['_source']['title'] for item in completions]

    async def get_definition(self, word):
        url = f"https://sjp.pwn.pl/slowniki/{urllib.parse.quote_plus(word)}.html"

        async with self.sess.get(url) as resp:
            resp.raise_for_status()
            html = await resp.text()

        soup = BeautifulSoup(html, "html.parser")
        lines = []

        title_elem = soup.select_one("span.tytul a")
        if title_elem:
            lines.append(title_elem.get_text(strip=True))

        znacz_elements = soup.select("div.znacz")

        if znacz_elements:
            for znacz in znacz_elements:
                lines.append(znacz.get_text())
        else:
            article = soup.select_one("li.pwn-article")
            if article:
                for br in article.find_all("br"):
                    br.replace_with("\n")
                text = article.get_text().strip()
                if text:
                    lines.append(text)

        return "\n".join(lines) if lines else None
