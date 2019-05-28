# CSS

#### nth

nth-child()는 자식 중에 2번째

nth-of-type()은 같은 타입 형제 중에 2번째



#### box model

###### margin

```
 /* 왼쪽위, 오른쪽 아래: 상하
    왼쪽 아래, 오른쪽 위: 좌우 */
border-radius: 15px 75px
```



```
/* 4개 순서: top, right, left, bottom */
margin: 25px 25px 25px;

/* 3개 순서: top, right & left, bottom */
 margin: 25px 25px 25px;

/* 2개 순서: top & bottom, right & left */
margin: 10px 5px;
```



#### dispaly

```
html
<h2 class = "none">

css
.none {
    display: none;
}

```

```
html
<h2 class = "hidden">

css
.hidden {
    visibility: hidden
}
```



### position

#### relative

- 현재 위치 기준
- position 적용 전 (static일 때) 기준으로 움직임. 움직인 후 원래 공간 유지

#### absolute

- 기본 레이어 관계에서 벗어남. 즉 다른 도형들도 새로운 자리로 움직이게 됨
- 움직인 후 원래 공간이 없어짐
- position이 stastic이 아닌 부모를 찾아서 그 부모를 기준점으로 삼는다.

