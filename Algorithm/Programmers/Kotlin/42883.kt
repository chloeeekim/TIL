/*

큰 수 만들기 : https://school.programmers.co.kr/learn/courses/30/lessons/42883

어떤 숫자에서 k개의 수를 제거했을 때, 얻을 수 있는 가장 큰 수를 구하는 문제
- 숫자 number는 문자열 형식으로 주어진다
    - number는 2자리 이상, 1,000,000자리 이하인 숫자이다
- 제거할 수의 개수 k는 1 이상 number의 자릿수 미만인 자연수이다

Example:
- Input : number="1924", k=2
- Output : "94"

- Input : number="1231234", k=3
- Output : "3234"

- Input : number="4177252841", k=4
- Output : "775841"

Note:
stack을 사용하여 greedy 하게 해결
앞자리 숫자가 현재 숫자보다 작은 경우, 앞자리 숫자를 제거하는 것이 이득
"9876"과 같이 위 기준에 의해 제거할 숫자가 없는 경우, 뒷자리에서 k개만큼 제거하는 것이 이득

 */

class Solution {
    fun solution(number: String, k: Int): String {
        val stack = ArrayDeque<Char>()
        var removed = 0

        for (ch in number) {
            while (removed < k && stack.isNotEmpty() && stack.last() < ch) {
                stack.removeLast()
                removed++
            }
            stack.addLast(ch)
        }

        val maxLen = number.length - k
        return stack.slice(0 until maxLen).joinToString("")
    }
}