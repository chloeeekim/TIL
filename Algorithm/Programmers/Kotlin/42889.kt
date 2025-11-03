/*

실패율 : https://school.programmers.co.kr/learn/courses/30/lessons/42889

사용자가 현재 도전 중인 스테이지의 번호 리스트가 주어졌을 때, 실패율이 높은 스테이지부터 내림차순으로 구하는 문제
- 실패율은 스테이지에 도달했으나 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수이다
- stages의 원소는 1 이상 N+1 이하의 자연수로, 각 숫자는 사용자가 현재 도전 중인 스테이지의 번호이다
- stages가 N+1인 경우, 마지막 스테이지(N번째 스테이지)까지 클리어한 사용자를 의미한다
- 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 정렬한다
- 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의한다

Example:
- Input : N=5, stages=[2, 1, 2, 6, 2, 4, 3, 3]
- Output : [3,4,2,1,5]

- Input : N=4, stages=[4,4,4,4,4]
- Output : 	[4,1,2,3]
- 4번 스테이지의 실패율은 1이며, 나머지 스테이지의 실패율은 0이므로 작은 번호부터 정렬

Note:
groupingBy와 eachCount로 동일한 스테이지에 있는 사용자들의 수를 카운트
스테이지 1부터 시작하여 실패율을 구하는데, i-1 스테이지를 클리어하지 못한 경우, i 스테이지를 도전할 수 없다는 것을 이용하여 도전한 사용자의 수를 계산
sortedWith(compareByDescending...thenBy...)를 사용하여 다중 정렬

 */

class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        val stageMap = stages.toTypedArray().groupingBy { it }.eachCount()

        var remain = stages.size.toDouble()
        val failRate = (1..N).map { stage ->
            val fail = stageMap[stage] ?: 0
            val rate = if (remain > 0) fail / remain else 0.0
            remain -= fail
            stage to rate
        }

        return failRate
            .sortedWith(compareByDescending<Pair<Int, Double>> { it.second }.thenBy { it.first })
            .map { it.first }
            .toIntArray()
    }
}