## Template Literal

- backtick(`) 문자를 사용하여 문자열을 표현하는 방식
- 문자열을 간단하게 표현할 수 있어 가독성이 높다
- 아래 둘의 출력값은 동일하다

```
console.log("Plus: " + (a + b) " and Twice: " + "2 * (a + b)) + ".");
console.log(`Plus: ${a+b} and Twice: ${2*(a+b)}.`);
```
- 줄바꿈 기호를 사용하지 않고 코드 상에서 줄을 바꾸어도 동일하게 동작한다
```
console.log("New\nLine");
console.log(`New
Line`);
```
