/*

행렬 테두리 회전하기 : https://school.programmers.co.kr/learn/courses/30/lessons/77485

rows x columns 크기의 행렬과 회전할 직사각형 범위들이 주어졌을 때, 회전에 의해 위치가 바뀐 숫자 중 가장 작은 숫자들을 구하는 문제
- 직사각형 모양의 범위의 테두리 부분에 있는 숫자들을 시계 방향으로 회전한다
- 처음 행렬에는 가로 방향으로 숫자가 1부터 하나씩 증가하면서 적혀 있다
- 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현한다
    - 1 <= x1 < x2 <= rows, 1 <= y1 < y2 <= columns이다
- 모든 회전은 수넛대로 이루어진다

Example:
- Input : rows=6, columns=6, queries=[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
- Output : [8, 10, 25]

- Input : rows=3, columns=3, queries=[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
- Output : [1, 1, 5, 3]

- Input : rows=100, columns=97, queries=[[1,1,100,97]]
- Output : [1]

Note:
직사각형에서 (x1, y1)은 좌상단, (x2, y2)는 우하단의 꼭지점
순서대로 시계 방향으로 회전하도록 구현하고, 각 회전에 영향을 받은 숫자 중 최솟값을 결과에 저장

 */

class Solution {
    fun solution(rows: Int, columns: Int, queries: Array<IntArray>): IntArray {
        val arr = Array(rows) { i -> Array(columns) { j -> i * columns + j + 1 } }
        val answer = IntArray(queries.size)

        for ((idx, query) in queries.withIndex()) {
            val (x1, y1, x2, y2) = query.map { it - 1 }

            var swap = arr[x1][y1]
            var temp = 0
            var minimum = swap
            for (i in y1+1 .. y2) {
                temp = arr[x1][i]
                arr[x1][i] = swap
                swap = temp
                minimum = minOf(minimum, swap)
            }
            for (i in x1+1 .. x2) {
                temp = arr[i][y2]
                arr[i][y2] = swap
                swap = temp
                minimum = minOf(minimum, swap)
            }
            for (i in y2-1 downTo y1) {
                temp = arr[x2][i]
                arr[x2][i] = swap
                swap = temp
                minimum = minOf(minimum, swap)
            }
            for (i in x2-1 downTo x1) {
                temp = arr[i][y1]
                arr[i][y1] = swap
                swap = temp
                minimum = minOf(minimum, swap)
            }

            answer[idx] = minimum
        }

        return answer
    }
}