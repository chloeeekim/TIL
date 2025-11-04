/*

미로 탈출 : https://school.programmers.co.kr/learn/courses/30/lessons/159993

1 x 1 크기의 칸들로 이루어진 직사각형 격자 형태의 미로에서 탈출하는 데 필요한 최소 시간을 구하는 문제
- 각 칸은 통로 또는 벽으로 이루어져 있다
- 통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 이 문은 레버를 당겨서만 열 수 있다
- 레버 또한 통로들 중 한 칸에 있다
- 출발 지점에서 레버가 있는 칸으로 이동하여 레버를 당긴 후, 미로를 빠져나가는 문이 있는 칸으로 이동하여 탈출할 수 있다
- 미로에서 한 칸을 이동하는데 1초가 소요된다
- 미로를 나타낸 문자열 배열 maps와 maps[i]의 길이는 5 이상 100 이하이다
    - maps[i]는 다음 다섯 개의 문자들로만 이루어져 있다
        - S: 시작 지점
        - E: 출구
        - L: 레버
        - O: 통로
        - X: 벽
    - 시작 지점과 출구, 레버는 항상 다른 곳에 존재하며, 한 개씩만 존재한다
    - 출구는 레버가 당겨지지 않아도 지나갈 수 있으며, 모든 통로, 출구, 레버, 시작점은 여러 번 지나갈 수 있다
- 미로를 탈출할 수 없는 경우 -1을 리턴한다

Example:
- Input : maps=["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
- Output : 16

- Input : maps=["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
- Output : -1

Note:
어떤 시작지점에서 특정 문자가 있는 위치까지 이동하는 데 필요한 최소 시간을 구하는 getMinimumPath 함수 작성
getMinimumPath에서는 queue를 사용하여 BFS로 최소 거리를 구하는 방식
시작 지점에서 레버까지, 레버에서 출구까지 각각 최소 거리를 구한 다음 더하여 답을 계산
만약 둘 중 한 경우라도 종료 지점까지 도달할 수 없는 경우 -1을 리턴

 */

class Solution {
    data class Move(val x: Int, val y: Int, val count: Int)
    val dirs = listOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)

    fun solution(maps: Array<String>): Int {
        val sPos = findChar(maps, 'S') ?: return -1
        val lPos = findChar(maps, 'L') ?: return -1

        val sToL = getMinimumPath(maps, sPos, 'L')
        val lToE = getMinimumPath(maps, lPos, 'E')

        return if (sToL != -1 && lToE != -1) sToL + lToE else -1
    }

    private fun findChar(maps: Array<String>, target: Char): Pair<Int, Int>? {
        for (i in maps.indices) {
            for (j in maps[0].indices) {
                if (maps[i][j] == target) return i to j
            }
        }

        return null
    }

    private fun getMinimumPath(maps: Array<String>, start: Pair<Int, Int>, target: Char): Int {
        val height = maps.size
        val width = maps[0].length
        val visited = Array(height) { BooleanArray(width) }
        val queue = ArrayDeque<Move>().apply {
            addLast(Move(start.first, start.second, 0))
        }
        visited[start.first][start.second] = true

        while (queue.isNotEmpty()) {
            val (cx, cy, count) = queue.removeFirst()

            for ((dx, dy) in dirs) {
                val nx = cx + dx
                val ny = cy + dy
                if (nx !in 0 until height || ny !in 0 until width) continue

                if (maps[nx][ny] == target) return count + 1
                if (maps[nx][ny] != 'X' && !visited[nx][ny]) {
                    visited[nx][ny] = true
                    queue.addLast(Move(nx, ny, count + 1))
                }
            }
        }

        return -1
    }
}