# Bootstrap



## spacing

- .m-0: margin: 0px
- .mt-3: margin-top: 3px
- .mx-0: margin-right: 0px / margin-left: 0px
- .py-0 : padding-top: 0!  /  paddint-bottom: 0!
- mt-1: 0.25rm
- mt-2 : 0.5rm
- mt-3 : 1rm
- .mx-auto: 가운데 정렬
- mr-auto: 오른쪽 정렬
- ml-auto: 왼쪽 정렬



## color

- .bg-primary
- .text-primary
- .btn-primary



## border

- .border-primary
- radius: rounded-top, rounded-pill, roudned-circle



## display

- .d-block
- .d-inline
- .d-block
- 반응형:  d-sm-none cv



## position

- .position-static
- .position-top
- .d-block



## grid

- 12를 기준으로 : 약수가 제일 많기 때문에
- `<div class="square col-2 ofset-5 "></div>`



## flex

#### flex

``` 
flex-direction: row; // default: 오른쪽 정렬
flex-direction: row-reverse;
flex-direction: column;
```



#### flex-wrap

- nowrap: 모든 요소들을 한 줄에 정렬합니다.
- wrap:요소들을 여러 줄에 걸쳐 정렬합니다.
- wrap-reverse : 요소들을 여러 줄에 걸쳐 반대로 정렬합니다.



#### justify-content (x축 기준. 부모)

```html
/* 왼쪽 정렬 default */
justify-content: flex-start;
/* 오른쪽 정렬 */
justify-content: flex-end;
/* 가운데 정렬 */
justify-content: center;
 /* 좌우 정렬 */
justify-content: space-between;
/* 균등 좌우 정렬 : 안쪽 여백은 외곽 여백의 2배 */
justify-content: space-around;
```



```html
<!-- justify-content-center: 부모 -->
    <div class="row justify-content-center">
      <div class="col-2">1</div>
      <div class="col-2">2</div>
      <div class="col-2">3</div>
    </div>
    <br>
    <!-- justify-content-start -->
    <div class="row justify-content-start">
      <div class="col-2">1</div>
      <div class="col-2">2</div>
      <div class="col-2">3</div>
    </div>
    <br>
    <!-- justify-content-end -->
    <div class="row justify-content-end">
      <div class="col-2">1</div>
      <div class="col-2">2</div>
      <div class="col-2">3</div>
    </div>
    <br>
    <!-- justify-content-between -->
    <div class="row justify-content-between">
      <div class="col-2">1</div>
      <div class="col-2">2</div>
      <div class="col-2">3</div>
    </div>
    <br>
    <!-- justify-content-around -->
    <div class="row justify-content-around">
      <div class="col-2">1</div>
      <div class="col-2">2</div>
      <div class="col-2">3</div>
    </div>
```



#### align-items (y축 기준. 부모)

```html
/* 상단 정렬 */
align-items: flex-start;
/* 하단 정렬 */
align-items: flex-end;
/* 가운데 정렬 */
align-items: center;
/* 상하단 꽉 차게 default */
align-items: stretch;
/* 폰트의 하단 라인에 맞춰서 정렬 */
align-items: baseline;
```

```html
<!-- align-items-center -->
    <div class="row row-vh align-items-center">
      <div class="col">1</div>
      <div class="col">2</div>
      <div class="col">3</div>
    </div>
    <br>
    <div class="row row-vh align-items-start">
      <div class="col">1</div>
      <div class="col">2</div>
      <div class="col">3</div>
    </div>
    <br>
    <div class="row row-vh align-items-end">
      <div class="col">1</div>
      <div class="col">2</div>
      <div class="col">3</div>
    </div>
```





#### align-self (개별 단위. 자식)

```
.item8 {
	align-self: flex-start;           
}

.item4 {
	align-self: flex-end;    
}
.item5 {
	align-self: center;
}

```

```html
<div class="row align-items-center row-vh">
      <div class="col align-self-start">1</div>
      <div class="col align-self-center">2</div>
      <div class="col align-self-end">3</div>
</div>
```





#### order 

```html
.item1 {
    /* default가 0 */
    order: 0;
}

.item2 {
	/* 나머지가 default 0이므로 item2는 제일 마지막 순번이 됨 */
    order: 1;
}

.item4 {
	/* 숫자가 작을수록 앞 번호 */
    order: -1;
}

.item5 {
    order: -2;
}
```

