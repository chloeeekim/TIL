/*

가장 긴 팰린드롬 : https://school.programmers.co.kr/learn/courses/30/lessons/12904

문자열 s가 주어졌을 때, s의 부분문자열(substring) 중 가장 긴 팰린드롬의 길이를 구하는 문제
- 팰린드롬(palindrome)이란 앞뒤를 뒤집어도 똑같은 문자열을 의미한다
- 문자열 s의 길이는 2,500 이하의 자연수이다
    - 문자열 s는 알파벳 소문자로만 구성된다

Example:
- Input : s="abcdcba"
- Output : 7

- Input : s="abacde"
- Output : 3

Note:
이중 반복문을 통해 모든 부분문자열을 검사하는 방법도 가능하지만, 시간이 조금 더 걸리는 편
투 포인터 방식으로 idx에 대해 palindrome의 길이가 홀수인 경우와 짝수인 경우 두 가지로 구분하여 확인
코드 중복을 줄이기 위해 solve 함수를 생성

 */

class Solution {
    fun solution(s: String): Int {
        val length = s.length
        if (s == s.reversed()) return length

        fun solve(left: Int, right: Int): Int {
            var len = 0
            var l = left
            var r = right
            while (l >= 0 && r < length) {
                if (s[l] == s[r]) {
                    l--
                    r++
                    len += 2
                }
                else {
                    break
                }
            }

            return len
        }

        var answer = 0
        for (idx in 0 until length) {
            val lenOdd = solve(idx - 1, idx + 1) + 1
            val lenEven = solve(idx, idx + 1)

            answer = listOf(answer, lenOdd, lenEven).maxOrNull() ?: 0
        }

        return answer
    }
}