/*

가장 먼 노드 : https://school.programmers.co.kr/learn/courses/30/lessons/49189

n개의 노드와 간선의 정보가 주어졌을 때, 1번 노드로부터 가장 멀리 떨어진 노드의 개수를 구하는 문제
- 각 노드는 1부터 n까지 번호가 주어진다
- 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드를 의미한다
- 노드의 개수 n은 2 이상 20,000 이하이다
- 간선에 대한 정보가 담긴 2차원 배열 vertex의 길이는 1 이상 50,000 이하이다
    - vertex의 원소는 [a, b] 형식으로, a번 노드와 b번 노드 사이에 간선이 있다는 의미이다

Example:
- Input : n=6, vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
- Output : 3
- 4, 5, 6번 노드가 가장 멀다

Note:
queue를 이용하여 bfs 방식으로 최단경로를 구하여 해결
가장 먼 노드가 발견되거나, 가장 먼 노드와 거리가 같은 노드가 발견되면 가장 먼 노드에 대한 정보(maxDist, count)를 업데이트

 */

class Solution {
    data class Elem(val node: Int, val dist: Int)

    fun solution(n: Int, edge: Array<IntArray>): Int {
        val graph = Array(n + 1) { mutableListOf<Int>() }.apply {
            for ((a, b) in edge) {
                this[a].add(b)
                this[b].add(a)
            }
        }

        var maxDist = 0
        var count = 0
        val visited = BooleanArray(n + 1)
        val queue = ArrayDeque<Elem>().apply { addLast(Elem(1, 0)) }
        while (queue.isNotEmpty()) {
            val (curr, dist) = queue.removeFirst()
            if (visited[curr]) continue
            visited[curr] = true

            if (maxDist < dist) {
                maxDist = dist
                count = 1
            }
            else if (maxDist == dist) {
                count++
            }

            for (near in graph[curr]) {
                queue.addLast(Elem(near, dist + 1))
            }
        }

        return count
    }
}