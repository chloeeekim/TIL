/*

표 편집 : https://school.programmers.co.kr/learn/courses/30/lessons/81303

표의 행을 선택, 삭제, 복구하는 명령어들이 주어졌을 때, 모든 명령어를 수행한 후 표의 상태를 구하는 문제
- 한 번에 하나의 행만 선택할 수 있으며, 표의 범위(0행 ~ 마지막 행)를 벗어날 수 없다
- 주어지는 명령어들은 다음과 같다
    - "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택한다
    - "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택한다
    - "C": 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택한다
        - 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택한다
    - "Z": 가장 최근에 삭제된 행을 원래대로 복구한다
        - 단, 현재 선택된 행은 바뀌지 않는다
- 삭제되지 않은 행은 "O", 삭제된 행은 "X"로 표시하여 문자열 형태로 리턴한다
- 표의 행 개수를 나타내는 정수 n은 5 이상 1,000,000 이하이다
- 처음 선택된 행의 위치를 나타내는 정수 k는 0 이상 n 미만이다
- 명령어들이 담긴 문자열 배열 cmd의 원소 개수는 1 이상 200,000 이하이다
    - cmd의 각 원소는 "U X", "D X", "C", "Z" 중 하나이다
    - X는 1 이상 300,000 이하인 자연수이며, 0으로 시작하지 않는다
    - X가 나타내는 자연수에 ','는 주어지지 않는다 (e.g., 123,456의 경우 123456으로 주어진다)
    - cmd에 등장하는 모든 X들의 값을 합친 결과가 1,000,000 이하인 경우만 입력으로 주어진다
    - 표의 모든 행을 제거하여, 행이 하나도 남지 않는 경우는 입력으로 주어지지 않는다
    - 표의 범위를 벗어나는 이동은 입력으로 주어지지 않는다
    - 원래대로 복구할 행이 없을 때, "Z"가 명령어로 주어지지 않는다

Example:
- Input : n=8, k=2, cmd=["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
- Output : "OOOOXOOO"

- Input : n=8, k=2, cmd=["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
- Output : "OOXOXOOO"

Note:
map을 linked list처럼 사용하여 해결
삭제된 행은 복구가 가능해야 하므로, 삭제 정보를 stack에 저장

 */

class Solution {
    data class Elem(val loc: Int, val prv: Int, val nxt: Int)

    fun solution(n: Int, k: Int, cmd: Array<String>): String {
        val stack = ArrayDeque<Elem>()
        val linked = mutableMapOf<Int, IntArray>().apply {
            for (i in 0 until n) {
                this[i] = intArrayOf(i - 1, i + 1)
            }
        }
        val deleted = BooleanArray(n)
        var curr = k

        for (c in cmd) {
            val sp = c.split(" ")
            when (sp[0]) {
                "U" -> repeat(sp[1].toInt()) { curr = linked[curr]!![0] }
                "D" -> repeat(sp[1].toInt()) { curr = linked[curr]!![1] }
                "C" -> {
                    deleted[curr] = true
                    val (prv, nxt) = linked[curr]!!
                    stack.addLast(Elem(curr, prv, nxt))

                    curr = if (nxt == n) prv else nxt

                    if (prv == -1) linked[nxt]!![0] = prv
                    else if (nxt == n) linked[prv]!![1] = nxt
                    else {
                        linked[prv]!![1] = nxt
                        linked[nxt]!![0] = prv
                    }
                }
                "Z" -> {
                    val (loc, prv, nxt) = stack.removeLast()
                    deleted[loc] = false

                    if (prv == -1) linked[nxt]!![0] = loc
                    else if (nxt == n) linked[prv]!![1] = loc
                    else {
                        linked[prv]!![1] = loc
                        linked[nxt]!![0] = loc
                    }
                }
            }
        }

        return deleted.map { if (it) 'X' else 'O' }.joinToString("")
    }
}