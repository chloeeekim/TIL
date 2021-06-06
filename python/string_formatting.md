## 문자열 포맷팅 방법

### % operator

- C 스타일
- 포맷팅하고자 하는 문자열(혹은 number 등)의 데이터 타입이 동일해야 한다는 단점
```
str = "Hello %s" % "World!"
print(str)
-> Hello World!
```

### str.format()

- python3 이후 지원
- % operator보다 가독성이 좋으며, 데이터 타입에 신경쓰지 않아도 된다는 장점
```
str = "Hello {}".format("World!")
print(str)
-> Hello World!
```
- 다음와 같이 다양한 형태로 지원
- 긴 문자열과 매개변수가 많은 경우 여전히 가독성이 떨어진다는 단점
```
str = "Name: {name}, Age: {age}"
str.format(name="Chloe", age=29)
print(str)
-> Name: Chloe, Age: 29

str = "Name: {1}, Age: {0}"
str.format(29, Chloe)
print(str)
-> Name: Chloe, Age: 29
```

### f-string

- python 3.6 이상에서만 지원하는 문법
- 문자열이 긴 경우에도 가독성이 좋다
```
name = "World!"
str = f"Hello {name}"
print(str)
-> Hello World!
```
- 다음과 같이 산술 연산 또한 지원 (str.format()은 지원하지 않음)
```
a = 20
b = 9
str = f"age: {a+b}"
print(str)
-> age: 29
```
- f-string을 먼저 선언하고, 변수를 나중에 선언하는 방식 또한 가능
```
str = f"Name: {name}, Age: {age}"
name = "Chloe"
age = 29
print(str)
-> Name: Chloe, age = 29
```
