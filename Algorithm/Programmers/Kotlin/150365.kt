/*

미로 탈출 명령어 : https://school.programmers.co.kr/learn/courses/30/lessons/150365

n x m 크기의 격자 미로가 주어졌을 때, k만큼 이동하여 탈출하는 경로를 구하는 문제
- (x, y)에서 시작하여 (r, c)까지 이동하여야 한다
- (x, y)와 (r, c)를 포함하여 같은 위치를 두 번 이상 방문할 수 있다
- 미로에서 탈출한 경로를 문자열로 나타냈을 때, 사전 순으로 가장 빠른 경로로 탈출해야 한다
    - l: 왼쪽으로 한 칸 이동 / r: 오른쪽으로 한 칸 이동 / u: 위쪽으로 한 칸 이동 / d: 아래쪽으로 한 칸 이동
- 조건대로 미로를 탈출할 수 없는 경우 "impossible"을 리턴한다
- (x, y)와 (r, c)는 서로 다른 위치로 주어진다

Example:
- Input : n=3, m=4, x=2, y=3, r=3, c=1, k=5
- Output : "dllrl"

- Input : n=2, m=2, x=1, y=1, r=2, c=2, k=2
- Output : "dr"

- Input : n=3, m=3, x=1, y=2, r=3, c=3, k=4
- Output : "impossible"

Note:
시작점과 도착점의 최단 거리가 k보다 크다면 impossible
bfs 방식으로, 사전순으로 빠른 d, l, r, u 순서로 탐색
도착지점에 도달했는데 아직 k만큼 움직이지 않은 경우, 남은 거리가 2의 배수여야 다시 돌아올 수 있다

 */

import kotlin.math.abs

class Solution {
    data class Elem(val i: Int, val j: Int, val path: String)

    fun solution(n: Int, m: Int, x: Int, y: Int, r: Int, c: Int, k: Int): String {
        val direction = mapOf('d' to Pair(1, 0), 'l' to Pair(0, -1), 'r' to Pair(0, 1), 'u' to Pair(-1, 0))
        val queue = ArrayDeque<Elem>().apply { add(Elem(x, y, "")) }

        fun distance(i: Int, j: Int) = (abs(i - r) + abs(j - c)).toInt()

        val dist = distance(x, y)
        if (dist > k || (dist - k) % 2 == 1) return "impossible"

        while (queue.isNotEmpty()) {
            val (i, j, path) = queue.removeFirst()
            val d = path.length

            if (i == r && j == c) {
                if (d == k) return path
                else if ((d - k) % 2 == 1) return "impossible"
            }

            for ((ch, dir) in direction.entries) {
                val ni = i + dir.first
                val nj = j + dir.second

                if (distance(ni, nj) + d + 1 > k) continue

                if (ni in 1 .. n && nj in 1 .. m) {
                    queue.add(Elem(ni, nj, path + ch))
                    break
                }
            }
        }

        return "impossible"
    }
}