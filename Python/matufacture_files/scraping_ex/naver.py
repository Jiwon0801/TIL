
import requests
from bs4 import BeautifulSoup


req = requests.get('http://naver.com').text


#print(req)
soup = BeautifulSoup(req, 'html.parser')
tags = soup.select('PM_CL_realtimeKeyword_rolling .ah_item .ah_k')
print(tags)
