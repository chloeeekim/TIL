/*

모의고사 : https://school.programmers.co.kr/learn/courses/30/lessons/42840

문제의 정답이 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 구하는 문제
- 수포자는 1번부터 마지막 문제까지 다음과 같이 찍는다
    - 1번 수포자: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    - 2번 수포자: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    - 3번 수포자: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
- 1번부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers의 길이는 최대 10,000 이다
    - 문제의 정답은 1, 2, 3, 4, 5 중 하나이다
- 가장 높은 점수를 받은 사람이 여러 명일 경우, 오름차순으로 정렬하여 리턴한다

Example:
- Input : answers=[1, 2, 3, 4, 5]
- Output : [1]

- Input : answers=[1, 3, 2, 4, 2]
- Output : [1, 2, 3]

Note:
각 수포자들이 찍은 결과를 answers와 비교 가능한 길이만큼 늘려서 pick에 저장
answer와 pick이 같은 갯수만큼 count
맞춘 개수가 가장 많은 경우라면 idx + 1을 결과에 추가

 */

class Solution {
    fun solution(answers: IntArray): IntArray {
        val ways = listOf(
            listOf(1, 2, 3, 4, 5),
            listOf(2, 1, 2, 3, 2, 4, 2, 5),
            listOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        )

        val size = answers.size
        val count = IntArray(3)

        ways.forEachIndexed { idx, pattern ->
            val r = size / pattern.size + 1
            val pick = (1..r).flatMap { pattern }.take(size)
            count[idx] = answers.zip(pick).count { (a, p) -> a == p }
        }

        val max = count.maxOrNull() ?: 0

        return count.withIndex().mapNotNull { (idx, c) ->
            if (c == max) idx + 1 else null
        }.toIntArray()
    }
}