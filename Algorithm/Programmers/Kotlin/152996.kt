/*

시소 짝꿍 : https://school.programmers.co.kr/learn/courses/30/lessons/152996

사람들의 몸무게가 주어졌을 때, 시소 짝꿍이 몇 쌍 존재하는지 구하는 문제
- 시소는 중심으로부터 2m, 3m, 4m 거리의 지점에 좌석이 하나씩 존재한다
- 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면 시소 짝꿍이라고 한다
- 사람들의 몸무게 목록 weights의 길이는 2 이상 100,000 이하이다
    - weights의 원소는 100 이상 1,000 이하의 정수로, 몸무게 단위는 N(뉴턴)으로 주어진다

Example:
- Input : weights=[100,180,360,100,270]
- Output : 4
- (100, 100), (180, 360), (180, 270), (270, 360) 이렇게 네 쌍이 존재

Note:
Counter를 사용하여 몸무게 별로 인원수를 확인
몸무게가 같은 사람들은 무조건 시소 짝꿍이 된다 (1:1)
거리를 고려했을 때, 몸무게 비율이 2:3, 2:4, 3:4인 사람들과 시소 짝꿍이 될 수 있다
부동소수점 비교 시 정밀도 문제가 발생하므로, 비율로 나누는 방법 대신 양쪽에 비율을 곱하는 방법을 선택

 */

class Solution {
    fun solution(weights: IntArray): Long {
        val wCount = weights.toTypedArray().groupingBy { it }.eachCount()
        var answer = 0L

        val wSet = weights.toSet().sorted()
        val size = wSet.size

        for (i in 0 until size) {
            val iWeight = wSet[i]
            val iCount = wCount[iWeight]!!

            answer += iCount.toLong() * (iCount - 1) / 2

            for (j in i+1 until size) {
                val jWeight = wSet[j]
                val jCount = wCount[jWeight]!!

                if (iWeight * 3 == jWeight * 2 ||
                    iWeight * 2 == jWeight ||
                    iWeight * 4 == jWeight * 3) {
                    answer += iCount.toLong() * jCount
                }
            }
        }

        return answer
    }
}