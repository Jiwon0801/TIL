# python



## file

`os.chdir('폴더주소'): 작업하고 있는 위치 변경`

`os.listdir('폴더주소'): 저장된 디렉토리 전체 파일 목록을 얻기`

`os.rename('현재파일명', '바꿀파일명')`

`os.path.splitext(filename)`

`(c:/tempython/data.txt')`

`(c:/tempython/data', '.txt')`

`with open('파일명', '파일모드') as f:`

`파일모드`

`'w': 쓰기`

`'r': 읽기`

`'a': 이어쓰기`

`파일 쓰기`

`f.write('새로 쓸 내용')`

`파일 읽기`

`f.read(): 파일 전체 읽기`

`f.readlines(): 파일 한줄 씩 읽기`



## list

`reverse(): 순서를 역순`

`[-1]: 마지막 값 참조`



## string

`lower(): 소문자로`

`upper(): 대문자로`

`'구분자'.join('리스트'): 리스트를 구분자를 기준으로 문자열로 생성`

## csv

`Ex csv.writer` 

```
import csv
with open('lunch.csv', 'w', encoding = 'utf-8') as f:
    csv.writer = csv.writer(f)
    for item in lunch.items():
        csv.writer.writerow(item)
```

`Ex csv.reader`

```
import csv
with open('lunch.csv', 'r', encoding = 'utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)
```

## Scraping

`설치: pip intall beautifulsoup4`

`추가:`

`import requests`

`from bs4 import BeautifulSoup`

`req = requests.get('사이트 URL'): 요청 후 응답 저장`

`soup = BeautifulSoup(req, 'html'): 조작하기 편하게 html 변환`

`tags = soup.select('선택자'): 선택자의 조건에 해당하는 리스트 얻기`

`ctrl + shift + i: 개발자 도구 `

`.text: text내용만`

`.strip: 좌우 공백 제거`

