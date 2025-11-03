/*

지게차와 크레인 : https://school.programmers.co.kr/learn/courses/30/lessons/388353

컨테이너가 2차원 배열 형태로 놓여 있을 때, 요청을 순서대로 처리한 후 남은 컨테이너의 수를 구하는 문제
- "A"처럼 알파벳 하나만 요청으로 들어온 경우, 요청이 들어온 순간 접근 가능한 컨테이너를 제거
- "BB"처럼 알파벳이 두 번 반복된 경우, 요청된 종류의 모든 컨테이너를 제거

Example:
- Input : storage=["AZWQY", "CAABX", "BBDDA", "ACACA"], requests=["A", "BB", "A"]
- Output : 11

- Input : storage=["HAH", "HBH", "HHH", "HAH", "HBH"], requests=["C", "B", "B", "B", "B", "H"]
- Output : 4

Note:
storage의 사방으로 한 칸씩 '0'(외부)으로 패딩한 map 생성
bfs 방식으로 접근 가능 여부 배열인 canAccess를 구해 지게차 요청인 경우 접근 가능한지 확인하는 방식

 */

class Solution {
    val move = listOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)

    fun solution(storage: Array<String>, requests: Array<String>): Int {
        val n = storage.size
        val m = storage[0].length
        val map = Array(n + 2) { CharArray(m + 2) { '0' } }
        for (i in 0 until n) {
            for (j in 0 until m) {
                map[i+1][j+1] = storage[i][j]
            }
        }

        var remain = n * m
        for (request in requests) {
            val isCrane = request.length == 2
            remain -= remove(map, request[0], isCrane)
        }

        return remain
    }

    private fun getCanAccess(map: Array<CharArray>): Array<BooleanArray> {
        val n = map.size
        val m = map[0].size
        val canAccess = Array(n) { BooleanArray(m) { false } }

        val queue = ArrayDeque<Pair<Int, Int>>()
        queue.addLast(0 to 0)
        canAccess[0][0] = true

        while (queue.isNotEmpty()) {
            val (cx, cy) = queue.removeFirst()

            for ((dx, dy) in move) {
                val nx = cx + dx
                val ny = cy + dy
                if (nx !in 0 until n || ny !in 0 until m) {
                    continue
                }

                if (map[nx][ny] == '0' && canAccess[nx][ny] == false) {
                    canAccess[nx][ny] = true
                    queue.addLast(nx to ny)
                }
            }
        }

        return canAccess
    }

    private fun remove(map: Array<CharArray>, ch: Char, isCrane: Boolean): Int {
        var count = 0
        val n = map.size
        val m = map[0].size
        val canAccess = if (isCrane) null else getCanAccess(map)

        for (i in 1 until n - 1) {
            for (j in 1 until m - 1) {
                if (map[i][j] != ch) continue

                val removable = if (isCrane) {
                    true
                } else {
                    move.any { (dx, dy) ->
                        val nx = i + dx
                        val ny = j + dy
                        canAccess!![nx][ny]
                    }
                }

                if (removable) {
                    map[i][j] = '0'
                    count++
                }
            }
        }

        return count
    }
}