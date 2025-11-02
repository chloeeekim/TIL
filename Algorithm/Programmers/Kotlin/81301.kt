/*

숫자 문자열과 영단어 : https://school.programmers.co.kr/learn/courses/30/lessons/81301

숫자의 일부 자릿수가 영단어로 바뀐 문자열이 주어졌을 때, 원래 숫자를 구하는 문제
- 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 주어진다
- s의 길이는 1 이상 50 이하이며, s가 "zero" 혹은 "0"으로 시작하는 경우는 주어지지 않는다
- return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 주어진다

Example:
- Input : s="one4seveneight"
- Output : 1478

- Input : s="23four5six7"
- Output : 234567

- Input : s="2three45sixseven"
- Output : 234567

- Input : s="123"
- Output : 123

Note:
map을 사용하여 영어 단어에 해당하는 숫자를 매핑
replace를 사용하여 영어 단어를 숫자로 변경
fold를 사용하여 문자열 변환을 누적 방식으로 처리

 */

class Solution {
    fun solution(s: String): Int {
        val number = mapOf("zero" to "0", "one" to "1", "two" to "2", "three" to "3", "four" to "4", "five" to "5", "six" to "6", "seven" to "7", "eight" to "8", "nine" to "9")

        val answer = number.entries.fold(s) { acc, (str, num) ->
            acc.replace(str, num)
        }

        return answer.toInt()
    }
}