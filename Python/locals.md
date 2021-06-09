## locals()

- 현재의 local variables을 dict 타입으로 반환하는 내장 함수
- 값의 수정 불가
- 아래처럼 변수의 존재 유무를 확인하는 용도로 사용할 수 있다.
```
if money > 0 :
    chicken = money / 20000
if not 'chicken' in locals() : 
    chicken = 0
```
