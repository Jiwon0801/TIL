import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
res = requests.get('https://www.melon.com/chart/index.htm', headers=headers).text
soup = BeautifulSoup(res, 'html.parser')
tags = soup.select('#lst50')

with open("melon2.txt", "w", encoding='utf-8') as f:
    for tag in tags:
        ranks = tag.select_one('td:nth-child(2) span.rank').text.strip()
        song = tag.select_one('td:nth-child(6) .ellipsis.rank01 a').text.strip()
        artist = tag.select_one('td:nth-child(6) .ellipsis.rank02 a').text.strip()
        f.write(f'{ranks} / {song} / {artist} \n ')