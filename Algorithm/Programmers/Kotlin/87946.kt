/*

피로도 : https://school.programmers.co.kr/learn/courses/30/lessons/87946

유저의 현재 피로도와 던전별 피로도 정보가 주어졌을 때, 유저가 탐험할 수 있는 최대 던전 수를 구하는 문제
- 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 존재한다
- 각 던전은 한 번씩만 탐험할 수 있다
- 유저의 현재 피로도 k는 1 이상 5,000 이하인 자연수이다
- 던전별 피로도가 담긴 2차원 배열 dungeons의 길이는 1 이상 8 이하이다
    - dungeons의 가로(열) 길이는 2이다
    - dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"]이다
    - "최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같다
    - "최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수이다
    - 서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있다

Example:
- Input : k=80, dungeons=[[80,20],[50,40],[30,10]]
- Output : 3
- 1 -> 3 -> 2번째 순서로 던전을 탐험할 수 있다

Note:
queue를 이용하여 bfs 방식으로 완전 탐색
visited set에 포함되어 있는지 여부와 최소 필요 피로도가 남아 있는 피로도보다 작거나 같은지를 기준으로 탐험 가능한 던전을 필터링
더 이상 탐험 가능한 던전이 없는 경우 기존 answer와 비교하여 큰 값을 선택

 */

class Solution {
    data class Elem(val visited: Set<Int>, val remain: Int, val count: Int)

    fun solution(k: Int, dungeons: Array<IntArray>): Int {
        val queue = ArrayDeque<Elem>().apply { addLast(Elem(setOf<Int>(), k, 0)) }

        var answer = 0
        while (queue.isNotEmpty()) {
            val (visited, remain, count) = queue.removeFirst()

            val canVisit = dungeons.indices
                .filterNot { it in visited }
                .filter { dungeons[it][0] <= remain }

            if (canVisit.size == 0) {
                answer = maxOf(answer, count)
            }

            for (i in canVisit) {
                queue.addLast(Elem(visited + i, remain - dungeons[i][1], count + 1))
            }
        }

        return answer
    }
}