/*

괄호 변환 : https://school.programmers.co.kr/learn/courses/30/lessons/60058

'('와 ')'로만 이루어진 문자열을 올바른 괄호 문자열로 변경하는 문제
- '('와 ')'의 개수가 같다면 균형잡힌 괄호 문자열이라고 부른다
- 균형잡힌 괄호 문자열이 괄호의 짝도 모두 맞을 경우 올바른 괄호 문자열이라고 부른다
- 문자열 w가 균형잡힌 괄호 문자열인 경우, 다음 과정을 통해 올바른 괄호 문자열로 변환할 수 있따
    - 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환한다
    - 2. 문자열 w를 두 균형잡힌 괄호 문자열 u, v로 분리한다. 단, u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있다
    - 3. 문자열 u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계부터 다시 수행한다
    - 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환한다
    - 4. 문자열 u가 올바른 괄호 문자열이 아니라면 다음 과정을 수행한다
    - 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙인다
    - 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다
    - 4-3. ')'를 다시 붙인다
    - 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다
    - 4-5. 생성된 문자열을 반환한다
- p는 '('와 ')'로만 이루어진 문자열이며, 길이는 2 이상 1000 이하인 짝수이다
- p는 균형잡힌 괄호 문자열이다
- 만약 p가 이미 올바른 괄호 문자열이라면 그대로 리턴한다

Example:
- Input : p="(()())()"
- Output : "(()())()"

- Input : p=")("
- Output : "()"

- Input : p="()))((()"
- Output : "()(())()"

Note:
주어진 변환 방법에 맞게 recursive하게 해결
문자열을 u, v로 분리하는 splitUV 함수와 올바른 괄호 문자열인지 확인하는 isValid 함수 생성

 */

class Solution {
    fun solution(p: String): String {
        if (p.isEmpty()) return ""
        if (isValid(p)) return p

        return solve(p)
    }

    private fun solve(str: String): String {
        if (str.isEmpty()) return ""

        var (u, v) = splitUV(str)
        if (isValid(u)) return u + solve(v)

        val res = StringBuilder()
        res.append('(' + solve(v) + ')')
        val reversed = u.drop(1).dropLast(1).map { if (it == ')') '(' else ')' }.joinToString("")
        res.append(reversed)

        return res.toString()
    }

    private fun isValid(str: String): Boolean {
        var count = 0

        for (ch in str) {
            when (ch) {
                '(' -> count++
                ')' -> {
                    if (count == 0) return false
                    else count--
                }
            }
        }

        return count == 0
    }

    private fun splitUV(str: String): Pair<String, String> {
        var opening = 0
        var u = ""
        var v = ""

        for ((idx, ch) in str.withIndex()) {
            when (ch) {
                '(' -> opening++
                ')' -> opening--
            }
            if (opening == 0) {
                u = str.substring(0, idx + 1)
                v = str.substring(idx + 1)
                break
            }
        }

        return u to v
    }
}