import random
import requests
import json
from pprint import pprint

url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=860'
res = requests.get(url)
lottery = res.json()

winner = []
for i in range(1, 7):
    winner.append(lottery[f'drwtNo{i}'])
bonus = lottery['bnusNo']

# 1. 내가 자동으로 산 복권 번호와 당첨 번호 교집합 개수 비교
# 2. 특정 등수가 당첨되면 멈추기
count = 0
while True:
    my_num = random.sample(range(1, 45), 6)
    lotto = len(set(my_num).intersection(winner))

    if lotto == 6:
        rank = 1
    elif lotto == 5:
        if bonus in my_num:
            rank = 2
        else:
            rank = 3
    elif lotto == 4:
        rank = 4
    elif lotto == 3:
        rank = 5
    else:
        rank = 6
    count += 1

    print(f'{count}회 {my_num} 중 {lotto} 개 맞음. {rank}등')

    if (rank == 1):
        break










