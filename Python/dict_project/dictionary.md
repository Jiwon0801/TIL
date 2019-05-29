# Python

## Dictionary

##### dictionary 선언

``` python
# 딕셔너리 선언
dic = {'Name':'James', 'Job':'Student'}

score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}
```

##### dictionary key, value 리스트로 가져오기 : keys(), values()

```python
# 딕셔너리 키 리스트로 가져오기
print dic.keys()
 
# 딕셔너리 값 리스트로 가져오기
print dic.values()

```

##### dictionary key, value 튜플로 가져오기: items()

```python
# 딕셔너리 키, 값 쌍 튜플로 가져오기
print dic.items()
```



##### dictionary에 해당 키 있는지 검사: in

```python
# 딕셔너리에 해당 키가 있는지 검사하기
print 'Job' in dic
print 'Age' in dic
```



##### dictionary depth

```python
# 딕셔너리 안에 여러 키와 값이 중첩으로 있을 경우
if "requests" in mulcam["language"]["python"]["python standard ibrary"]:
    print("True")
else:
    print("False")
```