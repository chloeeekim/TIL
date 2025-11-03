/*

리코쳇 로봇 : https://school.programmers.co.kr/learn/courses/30/lessons/169199

보드게임판의 정보가 주어졌을 때, 말이 목표위치에 도달하는 데 최소 몇 번 이동해야 하는지 구하는 문제
- 리코쳇 로봇이라는 보드게임은 다음과 같이 진행된다
    - 말은 시작위치에서 출발한다
    - 현재 위치에서 상, 하, 좌, 우 중 한 방향으로 게임판 위의 장애물이나 게임판 가장자리까지 부딪힐 때까지 미끄러져 움직이는 것을 한 번의 이동으로 정의한다
    - 목표 위치에 정확하게 멈추는 것을 목표로 한다
- 게임판의 상태를 나타내는 문자열 배열 board의 길이는 3 이상 100 이하이다
    - board의 원소의 길이는 3 이상 100 이하이다
    - board의 원소의 길이는 모두 동일하다
    - 문자열은 ".", "D", "R", "G"로만 구성되어 있다
        - "."는 빈 공간, "D"는 장애물, "R"은 시작 위치, "G"는 목표 위치를 의미한다
    - "R"과 "G"는 한 번씩만 등장한다
- 만약 목표위치에 도달할 수 없다면 -1을 리턴한다

Example:
- Input : board=["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
- Output : 7

- Input : board=[".D.R", "....", ".G..", "...D"]
- Output : -1

Note:
ArrayDeque를 queue로 사용하여 BFS 방식으로 탐색
Move 라는 data class를 정의하여 탐색 시 필요한 정보들을 저장하는 용도로 사용

 */

class Solution {
    data class Move(val x: Int, val y: Int, val count: Int)
    val direction = listOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)

    fun solution(board: Array<String>): Int {
        return getMinimumMove(board, getStartPosition(board))
    }

    private fun getStartPosition(board: Array<String>): Pair<Int, Int> {
        for (i in board.indices) {
            for (j in board[0].indices) {
                if (board[i][j] == 'R') return i to j
            }
        }
        return -1 to -1
    }

    private fun getMinimumMove(board: Array<String>, start: Pair<Int, Int>): Int {
        val height = board.size
        val width = board[0].length
        val queue = ArrayDeque<Move>()
        val visited = Array(height) { BooleanArray(width) }
        queue.addLast(Move(start.first, start.second, 0))

        while (queue.isNotEmpty()) {
            var (x, y, count) = queue.removeFirst()

            for ((dx, dy) in direction) {
                var nx = x
                var ny = y
                while (nx + dx in 0 until height && ny + dy in 0 until width && board[nx + dx][ny + dy] != 'D') {
                    nx += dx
                    ny += dy
                }

                if (board[nx][ny] == 'G') return count + 1

                if (!visited[nx][ny]) {
                    queue.addLast(Move(nx, ny, count + 1))
                    visited[nx][ny] = true
                }
            }
        }

        return -1
    }
}