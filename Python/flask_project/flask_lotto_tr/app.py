from flask import Flask, render_template, request
import requests
import random
app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    response = requests.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}')
    lotto = response.json()
    # winner = []
    # for i in range(1, 7):
    #     winner.append(lotto[f'drwtNo{i}'])

    # 당첨번호 6개 (list comprehension)
    winner = [lotto[f'drwtNo{i}'] for i in range(1, 7)]

    # 내 번호 리스트 만드는 2가지 방법
    # 1. 랜덤으로 만들기
    my_numbers = sorted(random.sample(range(1, 46), 6))

    # 2. 입력받은 값으로 만들기
    my_numbers = []
    for i in range(1, 7):
        lotto_ball = request.args.get(f'ball_{i}')
        my_numbers.append(int(lotto_ball))
        my_numbers = sorted(my_numbers)

    # 2-1 list comprehension
    my_numbers = sorted([int(request.args.get(f'ball_{i}')) for i in range(1, 7)])

    # 번호 교집합 찾기
    matched = len(set(winner) & set(my_numbers))

    if len(set(my_numbers)) == 6:
        if matched == 6:
            result = "1등입니다!!!"
        elif matched == 5 and lotto["bnusNo"] in my_numbers:
            result = "2등입니다!!"
        elif matched == 5:
            result = "3등입니다!"
        elif matched == 4:
            result = "4등입니다."
        elif matched == 3:
            result = "5등입니다.."
        else:
            result = "꽝입니다..."
    else:
        result = '중복된 번호가 있는 것 같아요!'

    return render_template('lotto_result.html',
                           lotto_round=lotto_round,
                           winner=f'{winner} + {lotto["bnusNo"]}',
                           my_numbers=my_numbers,
                           result=result)

if __name__ == '__main__':
    app.run(debug=True)