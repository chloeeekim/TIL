/*

괄호 회전하기 : https://school.programmers.co.kr/learn/courses/30/lessons/76502

괄호 문자열이 주어졌을 때, 문자열을 x만큼 회전시켰을 때 올바른 괄호 문자열이 되도록 하는 x의 개수를 구하는 문제
- 올바른 괄호 문자열은 다음과 같다
    - (), [], {}는 모두 올바른 괄호 문자열이다
    - 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A}도 올바른 괄호 문자열이다
    - 만약 A, B가 올바른 괄호 문자열이라면 AB도 올바른 괄호 문자열이다
- 괄호 문자열 s는 대괄호, 중괄호, 소괄호로 이루어져 있다
    - s의 길이는 1 이상 1,000 이하이다

Example:
- Input : s="[](){}"
- Output : 3

- Input : s="}]()[{"
- Output : 2

- Input : s="[)(]"
- Output : 0

- Input : s="}}}"
- Output : 0

Note:
s의 길이가 홀수라면 올바른 괄호 문자열이 될 수 없으므로 0을 리턴
stack을 사용하여 올바른 괄호 문자열인지를 판단
모든 경우의 수에 대해서 확인

 */

class Solution {
    val pair = mapOf(']' to '[', '}' to '{', ')' to '(')

    fun solution(s: String): Int {
        val len = s.length
        if (len % 2 == 1) return 0

        return (0 until len).count { i ->
            isValid(s.drop(i) + s.take(i))
        }
    }

    private fun isValid(s: String): Boolean {
        val stack = ArrayDeque<Char>()

        for (ch in s) {
            when (ch) {
                '[', '(', '{' -> stack.addLast(ch)
                ']', ')', '}' -> {
                    if (stack.removeLastOrNull() != pair[ch]) {
                        return false
                    }
                }
            }
        }

        return stack.isEmpty()
    }
}