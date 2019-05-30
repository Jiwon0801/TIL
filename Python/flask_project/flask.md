## flask

####  app.py

- export FLASK_APP = hello.py 

- flask run

- flask.py  는 작동 안함

  

#### ___ _name _ ___

- __현재 스크립트 파일이 시작점인지 아니면 모듈인지 판단__
- 모듈의 이름이 저장되는 변수
- import로 가져오면 이 값은 모듈의 이름이 된다. app.py라면 app이 된다.
- __하지만 직접 실행 됐을 때는 모듈의 이름이 아니라 '_ _ main _ _'값으로 할당 된다.__
- 직접 실행이 되지 않을 경우에는 모듈 이름이 출력
- test.py

``` python
test.py

def add(a, b):
    return a+b

def mul(a, b):
    return a*b


# 직접 실행 됐을 때
if __name__ == "__main__":
    print(add(10, 20))
    print(mul(10, 20))
```

``` python 
import test

test.add(1,2)
```



- A.py, B.py

```python
A.py

from flask import Flask
app = Flask(__name__)

def fun():
    print('function A.py')

print('top-level A.py')

if (__name__ == "__main__"):
    print('A.py가 직접 실행')
else:
    print('A.py가 import 되어 사용됨')
```



```python
B.py

from flask import Flask
import A #자동으로 먼저 실행됨
app = Flask(__name__)

print('top-level B.py')
A.fun()

if (__name__ == "__main__"):
    print('B.py가 직접 실행')
else:
    print('B.py가 import 되어 사용됨')
```



- B가 실행될 경우 

  ```python
  top-level A.py
  A.py가 import 되어 사용됨
  top-level B.py
  function A.py
  B.py가 직접 실행
  ```



#### dict.keys()

- dict.keys(['1','2','3']) == 반복 가능한 객체 == iterable 객체
- 동적 할당을 위해
- 메모리 효율성



#### request.args

```python
request.args == ImmutableMultiDict([('name', '퐁퐁퐁')]
```





#### get() 방식

```python
user_name = request.args.get('name')
```



#### post() 방식

```python
user_name = request.form.get('name')
```



#### requests

```python
#외부 모듈이기 때문에 새로운 프로젝트 생성 시 설치 필요
pip install requests
```



#### list comprehension

```python
winner = []
for i in range(1,7):
	winner.append(lotto[f'drwNo{i}'])

# list comprehension
winner = [lotto[f'drwtNo{i}'] for i in range(1, 7)]

```