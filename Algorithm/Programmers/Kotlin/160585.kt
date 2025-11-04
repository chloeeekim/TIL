/*

혼자서 하는 틱택토 : https://school.programmers.co.kr/learn/courses/30/lessons/160585

틱택토 게임판이 주어졌을 때, 규칙을 지켜서 틱택토를 진행했을 때 나올 수 있는 상황인지 확인하는 문제
- 틱택토는 다음과 같이 진행된다
    - 3x3의 빈 칸으로 이루어진 게임판에 선공이 "O", 후공이 "X"를 번갈아가면서 빈칸에 표시한다
    - 가로, 세로, 대각선으로 3개가 같은 표시가 만들어지면 같은 표시를 만든 사람이 승리하고 게임이 종료된다
    - 9칸이 모두 차서 더 이상 표시를 할 수 없는 경우에는 무승부로 게임이 종료된다
- 다음과 같이 규칙을 어기는 실수를 할 수 있다
    - "O"를 표시할 차례인데 "X"를 표시하거나 반대로 "X"를 표시할 차례인데 "O"를 표시한다
    - 선공이나 후공이 승리해서 게임이 종료되었음에도 그 게임을 진행한다
- 게임판의 정보를 담고 있는 문자열 배열 board와 board[i]의 길이는 3이다
    - board의 원소는 모두 "O", "X", "."으로만 이루어져 있다
    - board[i][j]는 i+1행, j+1열에 해당하는 칸의 상태를 나타낸다
    - "."는 빈칸을, "O"와 "X"는 해당 문자로 칸이 표시되어 있음을 의미한다
- 규칙을 지켜서 틱택토를 진행했을 때 나올 수 있는 게임 상황이라면 1을, 아니라면 0을 리턴한다

Example:
- Input : board=["O.X", ".O.", "..X"]
- Output : 1

- Input : board=["OOO", "...", "XXX"]
- Output : 0
- 선공이 승리했음에도 계속 진행되었으므로 0을 리턴

- Input : board=["...", ".X.", "..."]
- Output: 0
- 선공 표시 없이 후공이 먼저 표시했으므로 0을 리턴

- Input : board=["...", "...", "..."]
- Output : 1

Note:
각각의 케이스별로 잘못되었는지 확인하고, 규칙에 어긋난 부분이 없다면 가능한 게임 상황이므로 1을 리턴
1. O의 갯수는 X의 갯수와 같거나 1개 더 많아야 한다
2. O가 이긴 상황에서 O의 갯수는 X의 갯수 + 1이어야 한다
3. X가 이긴 상황에서 X의 갯수는 O의 갯수와 같아야 한다
player가 이겼는지 확인하는 메서드 isWinner는 n x n으로 확장 가능하도록 구성
가능한 가로 / 세로 / 대각선 줄의 좌표들을 lists에 추가한 후 확인

 */

class Solution {
    fun solution(board: Array<String>): Int {
        val oCount = board.sumOf { it.count { it == 'O' } }
        val xCount = board.sumOf { it.count { it == 'X' } }

        if (xCount > oCount || oCount > xCount + 1) return 0

        var oWin = isWinner(board, 'O')
        var xWin = isWinner(board, 'X')

        if (oWin && xWin) return 0
        if (oWin && oCount != xCount + 1) return 0
        if (xWin && xCount != oCount) return 0

        return 1
    }

    private fun isWinner(board: Array<String>, player: Char): Boolean {
        val n = 3
        val lists = mutableListOf<List<Pair<Int, Int>>>()

        for (i in 0 until n) {
            lists.add(List(n) { j -> i to j })
            lists.add(List(n) { j -> j to i })
        }

        lists.add(List(n) { i -> i to i })
        lists.add(List(n) { i -> i to (n - i - 1) })

        return lists.any { line ->
            line.all { (i, j) -> board[i][j] == player }
        }
    }
}