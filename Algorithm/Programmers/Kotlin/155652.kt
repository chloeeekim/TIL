/*

둘만의 암호 : https://school.programmers.co.kr/learn/courses/30/lessons/155652

두 문자열 s와 skip, 자연수 index가 주어졌을 때, 특정 규칙에 따라 문자열을 만드는 문제
- 문자열은 다음과 같은 규칙에 따라 생성한다
    - 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 변경한다
    - index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아간다
    - skip에 있는 알파벳은 제외하고 건너뛴다
- s의 길이는 5 이상 50 이하이며, skip의 길이는 1 이상 10 이하이다
    - s와 skip은 알파벳 소문자로만 이루어져 있다
    - skip에 포함되는 알파벳은 s에 포함되지 않는다
- index는 1 이상 20 이하의 정수이다

Example:
- Input : cards1=["i", "drink", "water"], cards2=["want", "to"], goal=["i", "want", "to", "drink", "water"]
- Output : "Yes"

- Input : cards1=["i", "water", "drink"], cards2=["want", "to"], goal=["i", "want", "to", "drink", "water"]
- Output : "No"

Note:
skip을 제외한 나머지 알파벳들을 모아 alphaList에 저장
현재 인덱스는 indexOf로 구하고, 다음 인덱스는 size를 넘어갈 경우에 대비해 나머지로 구해준다

 */

class Solution {
    fun solution(s: String, skip: String, index: Int): String {
        val alphaList = ('a'..'z').filter { it !in skip }
        val size = alphaList.size

        var answer = StringBuilder()
        for (ch in s) {
            val idx = (alphaList.indexOf(ch) + index) % size
            answer.append(alphaList[idx])
        }

        return answer.toString()
    }
}