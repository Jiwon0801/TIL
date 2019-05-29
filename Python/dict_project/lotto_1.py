import random
import requests
from bs4 import BeautifulSoup
from pprint import pprint

numbers = random.sample(range(800, 861), 5)
for num in numbers:
    count = 0
    url = f'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}'
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')

    lottery = soup.select('.ball_645')
    print(f'{num} 회차 당첨 번호')
    for lotto in lottery:
        print(lotto.text, end=' ')
        count += 1
        if count == 6:
            print('+', end=' ')
    print('\n')
