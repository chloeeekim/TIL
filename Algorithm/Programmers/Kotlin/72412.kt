/*

순위 검색 : https://school.programmers.co.kr/learn/courses/30/lessons/72412

지원자들의 정보가 주어졌을 때, 특정 조건에 해당하는 지원자가 몇 명인지 구하는 문제
- [조건]을 만족하는 사람 중 테스트 점수를 X점 이상 받은 사람을 구한다
- info의 원소는 "개발언어 직군 경력 소울푸드 점수" 형태이며, 각 단어는 공백 문자 하나로 구분된다
    - 개발언어는 cpp, java, python 중 하나이다
    - 직군은 backend, frontend 중 하나이다
    - 경력은 junior, senior 중 하나이다
    - 소울푸드는 chicken, pizza 중 하나이다
    - 점수는 코딩테스트 점수를 의미하며, 1 이상 100,000 이하인 자연수이다
- query의 원소는 "[조건] X" 형태이며, 각 단어는 공백 문자 하나로 구분된다
    - [조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 형태의 문자열이다
    - 언어, 직군, 경력, 소울푸드는 - 표시가 가능하며, - 표시된 조건은 고려하지 않는다

Example:
- Input : info=
[
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
], query=
[
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
]
- Output : [1,1,1,1,2,4]

Note:
각 지원자들의 조건과 -의 조합을 생성하는 makeConditions 작성
생성된 조합을 합친 문자열을 key로 사용하여 hash 하는 방식
효율성 테스트가 있기 때문에 성능을 위해 검색 시에 binary search 사용
kotlin의 List.binarySearch의 경우 중복된 값이 있을 때 중복된 값 중 하나의 인덱스를 반환하기 때문에
target과 같거나 큰 값이 처음 나오는 위치를 찾는 lowerBound 메서드를 작성하여 해결

 */

class Solution {
    data class Elem(val infos: Array<String>, val idx: Int)

    fun solution(info: Array<String>, query: Array<String>): IntArray {
        val infoMap = mutableMapOf<String, MutableList<Int>>()

        for (i in info) {
            val (lang, part, career, soulfood, score) = i.split(" ")
            val scoreInt = score.toInt()
            val conditions = makeConditions(lang, part, career, soulfood)

            for (cond in conditions) {
                infoMap.getOrPut(cond) { mutableListOf() }.add(scoreInt)
            }
        }

        infoMap.values.forEach { it.sort() }

        return query.map { q ->
            val cond = q.substringBeforeLast(" ")
            val target = q.substringAfterLast(" ").toInt()

            val scores = infoMap[cond] ?: return@map 0
            val size = scores.size
            val lower = lowerBound(scores, target)
            size - lower
        }.toIntArray()
    }

    private fun lowerBound(list: List<Int>, target: Int): Int {
        var left = 0
        var right = list.size
        while (left < right) {
            val mid = (left + right) / 2
            if (list[mid] < target) left = mid + 1
            else right = mid
        }

        return left
    }

    private fun makeConditions(lang: String, part: String, career: String, soulfood: String): List<String> {
        val conditions = mutableSetOf<String>()
        val size = 4
        val queue = ArrayDeque<Elem>().apply { addLast(Elem(arrayOf(lang, part, career, soulfood), 0)) }

        while (queue.isNotEmpty()) {
            val (infos, idx) = queue.removeFirst()

            if (idx == size) {
                conditions.add(infos.joinToString(" and "))
                continue
            }

            queue.addLast(Elem(infos.copyOf(), idx + 1))
            infos[idx] = "-"
            queue.addLast(Elem(infos.copyOf(), idx + 1))
        }

        return conditions.toList()
    }
}