/*

크기가 작은 부분문자열 : https://school.programmers.co.kr/learn/courses/30/lessons/147355

숫자로 이루어진 문자열 t, p가 주어졌을 때, t에서 p와 길이가 같은 부분문자열 중 p보다 작거나 같은 것이 나오는 횟수를 구하는 문제
- p의 길이는 1 이상 18 이하이다
- t의 길이는 p의 길이 이상 10,000 이하이다
- t와 p는 숫자로만 이루어진 문자열이며, 0으로 시작하지 않는다

Example:
- Input : t="3141592", p="271"
- Output : 2
- 141, 159 두 가지

- Input : t="500220839878", p="7"
- Output : 8

- Input : t="10203", p="15"
- Output : 3

Note:
p의 길이만큼 t의 부분문자열을 구하여 비교
sumOf을 사용하여 반환 타입 추론 문제가 발생하지 않도록 람다 안에서는 Long을 리턴하고, 마지막에 toInt()로 변환

 */

class Solution {
    fun solution(t: String, p: String): Int {
        val size = p.length

        return (0..t.length - size).sumOf { i ->
            if (t.substring(i, i+size) <= p) 1L else 0L
        }.toInt()
    }
}