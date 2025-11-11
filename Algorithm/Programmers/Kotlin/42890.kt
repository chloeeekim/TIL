/*

후보키 : https://school.programmers.co.kr/learn/courses/30/lessons/42890

릴레이션을 나타내는 2차원 배열이 주어졌을 때, 유일성과 최소성을 만족하는 후보키의 개수를 구하는 문제
- 유일성이란 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 함을 의미한다
- 최소성이란 유일성을 가진 키를 구성하는 속성 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다
- relation은 2차원 문자열 배열이다
    - relation의 컬럼의 길이는 1 이상 8 이하이며, 각각의 컬럼은 릴레이션의 속성을 나타낸다
    - relation의 로우의 길이는 1 이상 20 이하이며, 각각의 로우는 릴레이션의 튜플을 나타낸다
    - relation의 모든 문자열의 길이는 1 이상 8 이하이며, 알파벳 소문자와 숫자로만 이루어져 있다
    - relation의 모든 튜플은 유일하게 식별 가능하다 (중복되는 튜플은 존재하지 않는다)

Example:
- Input : relation=
[
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]
- Output : 2
- 0번 속성, [1번 속성, 2번 속성]이 후보키가 된다

Note:
combinations을 구하여 가능한 모든 조합에 대해서 후보키가 가능한지 확인
해당 조합에 의해 유일성이 보장된다면, 기존 후보키들과 비교하여 subset 여부 확인

 */

class Solution {
    fun solution(relation: Array<Array<String>>): Int {
        val attrSize = relation[0].size
        val rows = relation.size
        val candidate = mutableListOf<List<Int>>()

        for (i in 1 .. attrSize) {
            val combination = combinations(attrSize, i)
            val tempSet = mutableSetOf<List<String>>()

            for (comb in combination) {
                val temp = relation.map { row ->
                    comb.map { row[it] }
                }
                if (temp.toSet().size != rows) continue
                val isCandidate = candidate.none { key ->
                    comb.containsAll(key)
                }
                if (isCandidate) candidate.add(comb)
            }
        }

        return candidate.size
    }

    private fun combinations(maxIdx: Int, size: Int): List<List<Int>> {
        val res = mutableListOf<List<Int>>()
        val temp = mutableListOf<Int>()

        fun backtrack(start: Int) {
            if (temp.size == size) {
                res.add(temp.toList())
                return
            }
            for (i in start until maxIdx) {
                temp.add(i)
                backtrack(i + 1)
                temp.removeLast()
            }
        }

        backtrack(0)
        return res
    }
}