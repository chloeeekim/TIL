/*

도넛과 막대 그래프 : https://school.programmers.co.kr/learn/courses/30/lessons/258711

도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프들과 그들을 연결한 정점 하나가 있을 때, 생성한 정점의 번호와 각 그래프들의 개수를 구하는 문제
- 크기 n인 도넛 모양 그래프는 n개의 정점과 n개의 간선으로 이루어진다
- 크기 n인 막대 모양 그래프는 n개의 정점과 n-1개의 간선으로 이루어진다
- 크기 n인 8자 모양 그래프는 2n+1개의 정점과 2n+2개의 간선으로 이루어진다
- 생성한 정점은 그래프들과 무관하며, 각 그래프의 임의의 정점 하나로 향하는 간선들을 연결한다
- edges의 원소는 [a, b] 형태이며, a번 정점에서 b번 정점으로 향하는 간선이 있다는 것을 의미한다
- 각 그래프의 수의 합은 2 이상이다

Example:
- Input : edges=[[2, 3], [4, 3], [1, 1], [2, 1]]
- Output : [2, 1, 1, 0]

- Input : edges=[[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
- Output : [4, 0, 1, 2]

Note:
map을 사용하여 각 정점의 inside, outside 간선의 개수를 Pair<Int, Int> 형태로 저장
생성한 정점은 inside가 하나도 없는 정점
막대 모양 그래프에는 무조건 1개의 outside 간선이 없는 정점이 존재
8자 모양 그래프에는 무조건 2개 이상의 outside와 2개 이상의 inside 간선이 있는 정점이 존재
전체 그래프의 개수는 생성한 정점에서 outside 간선의 개수
도넛 모양 그래프 개수 = 전체 그래프 개수 - 막대 모양 그래프 개수 - 8자 모양 그래프 개수

 */

class Solution {
    fun solution(edges: Array<IntArray>): IntArray {
        val edgeCount = mutableMapOf<Int, Pair<Int, Int>>()

        for ((a, b) in edges) {
            edgeCount[a] = edgeCount.getOrDefault(a, 0 to 0).let { it.first + 1 to it.second }
            edgeCount[b] = edgeCount.getOrDefault(b, 0 to 0).let { it.first to it.second + 1}
        }

        val answer = IntArray(4)
        var graphs = 0
        for ((key, pair) in edgeCount) {
            when {
                pair.first == 0 -> answer[2]++
                pair.first >= 2 && pair.second == 0 -> {
                    answer[0] = key
                    graphs = pair.first
                }
                pair.first == 2 && pair.second >= 2 -> answer[3]++
            }
        }
        answer[1] = graphs - answer[2] - answer[3]

        return answer
    }
}