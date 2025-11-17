/*

인사고과 : https://school.programmers.co.kr/learn/courses/30/lessons/152995

각 사원의 근무 태도 점수와 동료 평가 점수 목록이 주어졌을 때, 완호의 석차를 구하는 문제
- 석차는 다음과 같은 방법으로 구할 수 있다
    - 어떤 사원이 다른 임의의 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 있다면 해당 사원은 인센티브를 받지 못한다
    - 인센티브를 받을 수 있는 사원들 중에서 두 점수의 합이 높은 순으로 석차를 낸다
    - 두 점수의 합이 동일한 사원들은 동석차이며, 동석차의 수만큼 다음 석차는 건너 뛴다
- 각 사원의 근무 태도 점수와 동료 평가 점수 목록 scores의 길이는 1 이상 100,000 이하이다
    - scores의 각 행은 [a, b] 형태로, 각각 근무 태도 점수와 동료 평가 점수를 의미한다
    - scores[0]은 완호의 점수이다
    - a, b는 0 이상 100,000 이하의 정수이다
- 완호가 인센티브를 받지 못하는 경우 -1을 리턴한다

Example:
- Input : scores=[[2,2],[1,4],[3,2],[3,2],[2,1]]
- Output : 4

Note:
scores를 첫 번째 점수에 대해 내림차순으로, 두 번째 점수에 대해 오름차순으로 정렬
두 번째 점수가 앞서 나온 최대값보다 작은 경우, 해당 사원은 두 점수가 모두 임의의 사원보다 낮다는 것이 보장된다

 */

class Solution {
    fun solution(scores: Array<IntArray>): Int {
        val sorted = scores.sortedWith(compareBy({ -it[0] }, { it[1] }))
        var bMax = 0
        var answer = 0
        val target = scores[0]
        val targetSum = target.sum()

        for ((a, b) in sorted) {
            if (target[0] < a && target[1] < b) return -1

            if (b >= bMax) {
                bMax = b
                if (targetSum < a + b) answer++
            }
        }

        return answer + 1
    }
}