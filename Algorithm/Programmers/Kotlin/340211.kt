/*

[PCCP 기출문제] 3번 / 충돌위험 찾기 : https://school.programmers.co.kr/learn/courses/30/lessons/340211

2차원 좌표 상에서 운송 경로가 정해진 로봇들이 최단 경로로 이동할 때, 충돌 가능성이 발생하는 횟수를 구하는 문제
- n개의 포인트가 (r,c)와 같이 2차원 좌표 형태로 주어진다
- 로봇마다 m개의 포인트를 순서대로 방문하는 경로가 주어진다
- 모든 로봇은 0초에 동시에 출발하며, 1초마다 r 좌표와 c 좌표 중 하나가 1만큼 증감한 좌표로 이동한다
- 로봇은 항상 최단 경로로 이동하며, 최단 경로가 여러 가지일 경우, r 좌표가 변하는 이동을 c 좌표가 변하는 이동보다 먼저 진행한다
- 마지막 포인트에 도착한 이후의 경로는 고려하지 않는다
- 동일한 시간에 여러 좌표에서 충돌 위험이 발생한다면 그 횟수를 모두 더한다

Example:
- Input : points=[[3,2],[6,4],[4,7],[1,4]], routes=[[4,2],[1,3],[2,4]]
- Output : 1

- Input : points=[[3,2],[6,4],[4,7],[1,4]], routes=[[4,2],[1,3],[4,2],[4,3]]
- Output : 9

- Input : points=[[2,2],[2,3],[2,7],[6,6],[5,2]], routes=[[2,3,4,5],[1,3,4,5]]
- Output : 0

Note:
최단 경로를 구할 때 r 좌표가 변하는 이동이 c 좌표가 변하는 이동보다 먼저 하므로, r 좌표를 전부 이동한 이후 c 좌표 이동
각 로봇마다 경로를 구하여 (time, r, c)를 key로 하여 map에 value를 1씩 증가
map에 value가 2 이상인 경우는 충돌위험이 있는 것으로 판단

 */

class Solution {
    fun solution(points: Array<IntArray>, routes: Array<IntArray>): Int {
        val positions = mutableMapOf<Triple<Int, Int, Int>, Int>()

        for (route in routes) {
            val path = getPath(points, route)

            for (p in path) {
                positions[p] = (positions[p] ?: 0) + 1
            }
        }

        return positions.count { it.value >= 2 }
    }

    private fun getPath(points: Array<IntArray>, route: IntArray): MutableList<Triple<Int, Int, Int>> {
        var (currX, currY) = points[route[0] - 1]
        val path = mutableListOf<Triple<Int, Int, Int>>()
        path.add(Triple(0, currX, currY))
        var time = 0

        for (i in 1 until route.size) {
            val (endX, endY) = points[route[i] - 1]
            val dx = if (currX < endX) 1 else -1
            val dy = if (currY < endY) 1 else -1

            while (currX != endX) {
                currX += dx
                time++
                path.add(Triple(time, currX, currY))
            }
            while (currY != endY) {
                currY += dy
                time++
                path.add(Triple(time, currX, currY))
            }

            currX = endX
            currY = endY
        }

        return path
    }
}