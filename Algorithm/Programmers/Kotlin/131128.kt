/*

숫자 짝꿍 : https://school.programmers.co.kr/learn/courses/30/lessons/131128

두 정수 X, Y가 주어졌을 때, 두 수의 짝꿍을 구하는 문제
- 숫자 짝꿍이란 두 정수의 임의의 자리에서 공통으로 나타나는 정수들을 이용하여 만들 수 있는 가장 큰 정수를 의미한다
    - 짝꿍이 존재하지 않는 경우, 짝꿍은 -1이다
    - 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0이다
- 두 정수 X, Y의 길이(자릿수)는 각각 3 이상 3,000,000 이하이다
    - X, Y는 0으로 시작하지 않는다
- X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환한다

Example:
- Input : X="100", Y="2345"
- Output : "-1"

- Input : X="100", Y="203045"
- Output : "0"

- Input : X="100", Y="123450"
- Output : "10"

- Input : X="12321", Y="42531"
- Output : "321"

- Input : X="5525", Y="1255"
- Output : "552"

Note:
groupingBy와 eachCount를 사용하여 각 정수별 나타나는 개수를 카운트
가장 큰 정수를 만들기 위해서는 큰 수가 앞에 나타나야 하므로, 9부터 0까지 확인하며 공통으로 나타나는 횟수(min)만큼 문자열에 더한다
결과 문자열이 비어있다면 짝꿍이 존재하지 않으므로 "-1"을, 결과 문자열의 가장 앞 문자가 '0'이라면 0으로만 이루어진 문자열이므로 "0"을 리턴한다

 */

class Solution {
    fun solution(X: String, Y: String): String {
        val Xcount = X.groupingBy { it }.eachCount()
        val Ycount = Y.groupingBy { it }.eachCount()

        val answer = buildString {
            ('9' downTo '0').forEach { num ->
                val r = minOf(Xcount[num] ?: 0, Ycount[num] ?: 0)
                repeat(r) { append(num) }
            }
        }

        return if (answer.isEmpty()) "-1" else if (answer[0] == '0') "0" else answer
    }
}