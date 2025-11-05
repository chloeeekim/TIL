/*

k진수에서 소수 개수 구하기 : https://school.programmers.co.kr/learn/courses/30/lessons/92335

양의 정수 n을 k진수로 바꿨을 때, 변환된 수 안에 특정 조건을 만족하는 소수가 몇 개인지 확인하는 문제
- 다음 조건을 만족하는 소수(Prime number)의 개수를 리턴한다
    - 0P0처럼 소수 양쪽에 0이 있는 경우
    - P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
    - 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
    - P처럼 소수 양쪽에 아무것도 없는 경우
    - 단, P는 각 자릿수에 0을 포함하지 않는 소수이다

Example:
- Input : n=437674, k=3
- Output : 3
- 437674를 3진법으로 바꾸면 211020101011 이고, 소수는 211, 2, 11 세 개가 존재한다

- Input : n=110011, k=10
- Output : 2

Note:
n.toString(k)으로 숫자 n을 k진법으로 변경
연속된 0을 기준으로(0+) split 후 비어 있는 요소 제거 (k진법으로 변환한 문자열의 마지막에 0이 오는 경우)
동일한 숫자에 대해서 소수 판별을 여러 번 하지 않기 위해 groupingBy + eachCount 사용
k진법으로 변환한 숫자가 커서 오버플로우가 발생할 수 있으므로 Long 타입으로 변환하여 소수 판별

 */

import kotlin.math.sqrt

class Solution {
    fun solution(n: Int, k: Int): Int {
        val nums = n.toString(k).split("0+".toRegex())
            .filter { it.isNotEmpty() }
            .groupingBy { it }.eachCount()

        return nums.entries.sumOf { (num, count) ->
            if (isPrime(num.toLong())) count else 0
        }
    }

    private fun isPrime(n: Long): Boolean {
        if (n == 1L) return false
        if (n == 2L) return true

        val limit = sqrt(n.toDouble()).toLong() + 1
        for (i in 2 .. limit) {
            if (n % i == 0L) return false
        }
        return true
    }
}