/*

요격 시스템 : https://school.programmers.co.kr/learn/courses/30/lessons/181188

x축에 평행한 직선 형태의 미사일들이 주어졌을 때, 모든 미사일을 요격하기 위해 필요한 요격 미사일의 최솟값을 구하는 문제
- 폭격 미사일은 x축에 평행한 직선 형태의 모양이며, 개구간을 나타내는 정수 쌍 (s, e)로 표현된다
- 요격 미사일은 y축에 평행한 형태이며, 해당 x좌표에 걸쳐 있는 모든 폭격 미사일을 관통하여 한 번에 요격할 수 있다
    - 단, 개구간 (s, e)로 표현되는 폭격 미사일은 s와 e에서 발사하는 요격 미사일로는 요격할 수 없다
    - 요격 미사일은 실수인 x좌표에서도 발사할 수 있다
- 각 폭격 미사일의 x좌표 범위 목록 targets의 길이는 1 이상 500,000 이하이다
    - targets의 각 행은 [s, e] 형태이다
    - s, e는 0 이상 100,000,000 이하이며, s는 e보다 작다

Example:
- Input : targets=[[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
- Output : 3

Note:
각 폭격 미사일을 끝나는 지점을 기준으로 정렬 후 확인
A 미사일의 끝나는 지점이 B 미사일의 시작 지점과 같거나 작다면, 새로운 미사일이 하나 더 필요하다

 */

class Solution {
    fun solution(targets: Array<IntArray>): Int {
        var answer = 0
        var end = -1

        for ((s, e) in targets.sortedBy { it[1] }) {
            if (s >= end) {
                answer++
                end = e
            }
        }

        return answer
    }
}