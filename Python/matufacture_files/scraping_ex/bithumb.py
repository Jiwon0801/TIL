import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bithumb.com/').text
soup = BeautifulSoup(req, 'html.parser')
# coin_tags = soup.select('#tableAsset > tbody > tr > td:nth-child(1) > p > a > strong:not(i)')
# cost_tags = soup.select('#tableAsset > tbody > tr > td:nth-child(2) > strong')
#
# # for tag in coin_tags:
# #    print(tag.text.strip())
# #
# # for tag in cost_tags:
# #    print(tag.text.strip())
# leng = len(cost_tags)
# with open("bithumb.txt", "w", encoding = 'utf-8') as f:
#     for i in range(0, leng):
#         f.write(coin_tags[i].text.strip() + '/' + cost_tags[i].text.strip() +'\n')

tags = soup.select('.coin_list tr')
with open("bithumb.txt", "w", encoding='utf-8') as f:
    for tag in tags:
        name = tag.select_one('td:nth-of-type(1) a strong').text.replace(' NEW', '').strip()
        price = tag.select_one('td:nth-of-type(2) strong').text.strip()
        f.write(f'{name} / {price}\n ')

