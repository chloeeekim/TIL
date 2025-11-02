/*

성격 유형 검사하기 : https://school.programmers.co.kr/learn/courses/30/lessons/118666

4가지의 지표와 n개의 질문에 대한 답변이 있을 때, 성격 유형 검사 결과를 구하는 문제
- 1번 지표: 라이언형(R), 튜브형(T) / 2번 지표: 콘형(C), 프로도형(F) / 3번 지표: 제이지형(J), 무지형(M) / 4번 지표:어피치형(A), 네오형(N)
- 질문에 대한 선택지는 7가지가 있으며, 매우 동의 혹은 매우 비동의인 경우 3점, 동의나 비동의인 경우 2점, 약간 동의나 약간 비동의인 경우 1점, 모르겠음인 경우 0점을 획득
- 하나의 지표에서 각 성격 유형 점수가 같다면, 두 성격 유형 중 사전 순으로 빠른 성격 유형을 선택한다
- survey의 원소는 "RT"와 같이 각 지표의 성격 유형 값이며, 첫 번째 문자는 비동의 관련 선택지를 선택했을 때 받는 성격 유형이며, 두 번째 문자는 동의 관련 선택지를 선택했을 때 받는 성격 유형이다
- choices의 원소는 1: 매우 비동의, 2: 비동의, ... , 6: 동의, 7: 매우 동의를 의미한다

Example:
- Input : survey=["AN", "CF", "MJ", "RT", "NA"], choices=[5, 3, 2, 7, 5]
- Output : "TCMA"

- Input : survey=["TR", "RT", "TR"], choices=[7, 1, 3]
- Output : "RCJA"
- 2, 3, 4번 지표는 모두 0점이므로 사전 순으로 빠른 C, J, A를 선택

Note:
MutableMap을 사용하여 각 성격 유형에 따른 점수를 저장
choiceList에 choice 값에 따른 점수를 저장

 */

class Solution {
    fun solution(survey: Array<String>, choices: IntArray): String {
        val choiceList = listOf(3 to 0, 2 to 0, 1 to 0, 0 to 0, 0 to 1, 0 to 2, 0 to 3)
        val keys = listOf('R', 'T', 'C', 'F', 'J', 'M', 'A', 'N')
        val typeMap = keys.associateWith { 0 }.toMutableMap()

        survey.zip(choices.toTypedArray()).forEach { (s, c) ->
            val (first, second) = choiceList[c - 1]
            typeMap[s[0]] = typeMap[s[0]]!! + first
            typeMap[s[1]] = typeMap[s[1]]!! + second
        }

        val resultPairs = listOf('R' to 'T', 'C' to 'F', 'J' to 'M', 'A' to 'N')
        return buildString {
            for ((a, b) in resultPairs) {
                append(if (typeMap[a]!! >= typeMap[b]!!) a else b)
            }
        }
    }
}