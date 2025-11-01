/*

공원 산책 : https://school.programmers.co.kr/learn/courses/30/lessons/172928

공원의 정보와 명령어들이 주어졌을 때, 모든 명령 수행 후의 위치를 구하는 문제
- 공원은 지나다니는 길 'O'와 장애물 'X'로 이루어진다
- 명령은 다음을 먼저 확인한 후, 두 가지 중 하나라도 해당된다면 해당 명령을 무시하고 다음 명령을 수행한다
    - 주어진 방향으로 이동할 때 공원을 벗어나는지 확인한다
    - 주어진 방향으로 이동할 때 장애물을 만나는지 확인한다
- 공원을 나타내는 문자열 배열 park와 park의 원소의 길이는 3 이상 50 이하이다
    - park[i]는 'S', 'O', 'X'로 이루어져 있으며, 'S'는 시작점을 의미한다
    - 시작지점은 하나만 주어진다
    - park는 직사각형 모양이다
- 명령이 담긴 문자열 배열 routes의 길이는 1 이상 50 이하이다
    - routes의 첫 번째 원소부터 순서대로 명령을 수행한다
    - routes의 원소는 "op n"과 같은 구조로 이루어져 있다
        - op는 이동할 방향을, n은 이동할 칸수를 의미한다
        - op는 N(북쪽), S(남쪽), W(서쪽), E(동쪽) 네 가지 중 하나로 이루어져 있다
        - n은 1 이상 9 이하의 정수이다
- 모든 명령 수행 후의 위치를 [세로 방향 좌표, 가로 방향 좌표] 순으로 배열에 담아 리턴한다

Example:
- Input : park=["SOO","OOO","OOO"], routes=["E 2","S 2","W 1"]
- Output : [2, 1]

- Input : park=["SOO","OXX","OOO"], routes=["E 2","S 2","W 1"]
- Output : [0, 1]

- Input : park=["OSO","OOO","OXO","OOO"], routes=["E 2","S 3","W 1"]
- Output : [0, 0]

Note:
move에서 이동 불가능한 경우 기존 위치를 그대로 반환하고, 이동 가능한 경우 이동한 위치를 반환하도록 구성
kotlin은 Char와 String 타입을 ''와 ""로 구분하므로, 주의할 것 (str[i]와 같이 인덱스로 접근하면 Char)

 */

class Solution {
    lateinit var map: Array<String>
    val direction = mapOf("N" to (-1 to 0), "S" to (1 to 0), "W" to (0 to -1), "E" to (0 to 1))

    fun solution(park: Array<String>, routes: Array<String>): IntArray {
        map = park
        var (currX, currY) = findStart()

        routes.forEach { route ->
            val (op, n) = route.split(" ")
            val next = move(currX, currY, op, n.toInt())
            currX = next.first
            currY = next.second
        }

        return intArrayOf(currX, currY)
    }

    private fun findStart(): Pair<Int, Int> {
        for (i in 0 until map.size) {
            for (j in 0 until map[0].length) {
                if (map[i][j] == 'S') {
                    return Pair(i, j)
                }
            }
        }
        return Pair(-1, -1)
    }

    private fun move(x: Int, y: Int, op: String, n: Int): Pair<Int, Int> {
        val (dx, dy) = direction[op] ?: (0 to 0)
        var currX = x
        var currY = y

        repeat(n) {
            val nx = currX + dx
            val ny = currY + dy

            if (nx !in (0 until map.size) || ny !in (0 until map[0].length) || map[nx[ny] == 'X']) {
                return Pair(x, y)
            }

            currX = nx
            currY = ny
        }

        return Pair(currX, currY)
    }
}