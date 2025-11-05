/*

거리두기 확인하기 : https://school.programmers.co.kr/learn/courses/30/lessons/81302

5개의 대기실의 구조와 자리에 앉아있는 응시자들의 정보가 주어졌을 때, 각 대기실별로 거리두기를 지키고 있는지 확인하는 문제
- 대기실은 총 5개이며, 각 대기실은 5x5 크기이다
- 응시자들끼리는 맨해튼 거리가 2 이하로 앉은 경우 거리두기를 지키지 않은 것으로 간주한다
    - 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용한다
- 각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않은 경우 0을 배열에 담아 리턴한다
- places의 행 길이는 5(대기실의 개수)이며, 각 행은 하나의 대기실 구조를 나타낸다
- places의 원소는 P, O, X로 이루어진 문자열이다
    - P는 응시자가 앉아있는 자리를 의미한다
    - O는 빈 테이블을 의미한다
    - X는 파티션을 의미한다

Example:
- Input : places=[
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]
- Output : [1, 0, 1, 1, 1]

Note:
각 응시자들의 위치로부터 시작하여 queue를 사용한 bfs 방식으로 해결
상하좌우로 한 번 이동할 때마다 해밀턴 거리는 1씩 증가한다

 */

class Solution {
    data class Elem(val x: Int, val y: Int, val dist: Int)
    val size = 5

    fun solution(places: Array<Array<String>>): IntArray {
        return places.map { solve(it) }.toIntArray()
    }

    private fun solve(place: Array<String>): Int {
        val dirs = listOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)

        for (i in 0 until size) {
            for (j in 0 until size) {
                if (place[i][j] != 'P') continue

                val queue = ArrayDeque<Elem>().apply { addLast(Elem(i, j, 0))}
                val visited = Array(size) { BooleanArray(size) }
                visited[i][j] = true

                while (queue.isNotEmpty()) {
                    val (x, y, dist) = queue.removeFirst()
                    visited[x][y] = true

                    for ((dx, dy) in dirs) {
                        val nx = x + dx
                        val ny = y + dy

                        if (nx in 0 until size && ny in 0 until size && !visited[nx][ny]) {
                            if (place[nx][ny] == 'O' && dist < 2) {
                                queue.addLast(Elem(nx, ny, dist + 1))
                            }
                            else if (place[nx][ny] == 'P' && dist <= 1) {
                                return 0
                            }
                        }
                    }
                }
            }
        }

        return 1
    }
}