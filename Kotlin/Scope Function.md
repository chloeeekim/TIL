## Kotlin Scope Function

| 함수명     | 객체 참조 | 반환 값           | 확장함수 여부                           |
|---------|-------|----------------|-----------------------------------|
| `let`   | `it`  | lambda 결과값     | Yes                               |
| `run`   | `this` | lambda 결과값     | Yes                               |
| `run`   | -     | lambda 결과값     | No (context object 없이 호출)         |
| `with`  | `this` | lambda 결과값     | No (context object를 argument로 받음) |
| `apply` | `this` | context object | Yes                               |
| `also`  | `it`  | context object | Yes                               |

### let

- 객체 참조: `it`
- 반환 값: 마지막 표현식 (lambda 결과값)
- 다음과 같이 안전 호출 연산자(`?.`)와 같이 사용하여 null-safe 호출에 사용되는 경우가 많다

```kotlin
val length = person?.let { it.name.length }
```

- 객체 접근 식별자를 다음과 같이 변경할 수 있다
```kotlin
val length = person?.let { p -> p.name.length }
```

### run

- 객체 참조: `this` (수정 불가/생략 가능)
- 반환 값: 마지막 표현식 (lambda 결과값)
- 다음과 같이 `this`를 생략하고 사용하는 경우가 많다

```kotlin
val length = person.run { name.length }
```

- 다음과 같이 확장 함수가 아닌 `run`을 단독 사용할 수도 있다
- 이 경우는 관련 코드들을 한 블럭에 묶어 가독성을 높이는 역할을 수행

```kotlin
val length = run {
    println(name)
    name.length
}
```

### with

- 객체 참조: `this` (수정 불가/생략 가능)
- 반환 값: 마지막 표현식 (lambda 결과값)
- 확장 함수가 아닌 일반 함수이므로, 안전 호출 연산자를 사용한 null check가 불가능
- 다음과 같이 non-null인 객체에 대한 코드를 하나의 블록으로 묶어 가독성을 높이는 역할을 수행

```kotlin
val person = Person("Alice", 30)
val length = with(person) {
    name.length
}
```

### apply

- 객체 참조: `this`
- 반환 값: 원본 객체 (context object)
- 다음과 같이 객체 초기화에 주로 사용

```kotlin
val person = Person().apply {
    name = "Alice"
    age = 30
}
```

### also

- 객체 참조: `it`
- 반환 값: 원본 객체 (context object)
- 다음과 같이 로깅이나 디버깅 등의 부가 작업 등에 많이 사용

```kotlin
val numbers = mutableListOf("one", "two", "three")
numbers.also { println("initial list: $it") }
```

- `let`처럼 객체 접근 식별자를 다음과 같이 변경할 수 있다

```kotlin
numbers.also { n -> println("initial list: $n") }
```

### `it` 키워드

- 다음과 같이 상위 스코프에 동일한 이름의 변수가 존재하는 경우, `apply`나 `run`을 사용하였을 때 문제가 발생할 수 있다

```kotlin
val name = "Alice"
val person = Person("Bob", 30)
person.run {
    println("length: ${name.length}") // 5
}
```

- 위 경우, person 인스턴스의 name이 아닌 상위 스코프의 name을 참조하게 된다
- 다음과 같이 `it` 키워드를 사용하면 원하는 결과를 얻을 수 있다

```kotlin
val name = "Alice"
val person = Person("Bob", 30)
person.let {
    println("length: ${it.name.length}") // 3
}
```
