from flask import Flask, render_template, request
import requests
import random
import json
app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    response = requests.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}')
    lotto = response.json()

    #list comprehension
    winner = [lotto[f'drwtNo{i}'] for i in range(1, 7)]

    # 내 번호 리스트 만들기
    my_num = random.sample(range(1, 46), 7)

    # 당첨 번호와의 교집합
    lottery = len(set(my_num).intersection(winner))
    #set : 중복 제한

    bonus = lotto["bnusNo"]

    # 조건에 따라 1등부터 꽝까지 결과값 lotto_result로 보내준다.
    if lottery == 6:
        rank = 1
    elif lottery == 5:
        if bonus in my_num:
            rank = 2
        else:
            rank = 3
    elif lottery == 4:
        rank = 4
    elif lottery == 3:
        rank = 5
    else:
        rank = "꽝"


    return render_template('lotto_result.html', lotto_round = lotto_round, winner=f'{winner}+ {lotto["bnusNo"]}',my_num = my_num, rank = rank)

if __name__ == "__main__":
    app.run(debug=True)