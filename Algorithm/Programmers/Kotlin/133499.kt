/*

옹알이 (2) : https://school.programmers.co.kr/learn/courses/30/lessons/133499

문자열 배열이 주어질 때, 조카가 발음할 수 있는 단어의 개수를 구하는 문제
- 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못한다
    - 또, 연속해서 같은 발음을 하는 것을 어려워한다
- 문자열 배열 babbling의 길이는 1 이상 100 이하이다
    - babbling의 원소의 길이는 1 이상 30 이하이다
    - 문자열은 알파벳 소문자로만 이루어져 있다

Example:
- Input : babbling=["aya", "yee", "u", "maa"]
- Output : 1
- "aya"만 발음할 수 있다

- Input : babbling=["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
- Output : 2
- "ayaye"와 "yemawoo"만 발음할 수 있다 ("yeye"의 경우 동일한 발음이 연속되기 때문에 발음할 수 없다)

Note:
canSpeak 함수를 생성하여 해당 발음이 가능한지 확인
발음할 수 있는 네 가지 중에서 하나가 문자열 시작과 동일하다면, 해당 발음의 인덱스를 before에 저장하고, 문자열에서 해당 발음을 제거하고 다시 반복
만약 before와 동일한 발음이 나온다면 연속된 발음이므로 불가능

 */

class Solution {
    fun solution(babbling: Array<String>): Int {
        return babbling.count { canSpeak(it) }
    }

    private fun canSpeak(word: String): Boolean {
        val speak = listOf("aya", "ye", "woo", "ma")
        var idx = 0
        var before: String? = null

        while (idx < word.length) {
            val match = speak.firstOrNull { can ->
                word.startsWith(can, startIndex=idx) && can != before
            } ?: return false

            before = match
            idx += match.length
        }

        return true
    }
}