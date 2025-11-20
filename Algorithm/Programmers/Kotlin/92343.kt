/*

양과 늑대 : https://school.programmers.co.kr/learn/courses/30/lessons/92343

2진 트리 형태에 놓여진 양과 늑대의 정보가 주어졌을 때, 조건에 따라 노드를 방문하면서 모을 수 있는 양의 최대 수를 구하는 문제
- 루트 노드(0번 노드)에서 출발하며, 루트 노드에는 항상 양이 있다
- 각 노드를 방문할 때마다 해당 노드에 있는 양 혹은 늑대가 따라온다
- 모아진 양의 수보다 늑대의 수가 같거나 더 많아지면 모든 양을 잡아먹는다
- 중간에 양이 잡아먹히지 않도록 하면서 최대한 많은 수의 양을 모아 루트 노드로 돌아와야 한다
- info는 길이 2 이상 17 이하의 정수 배열이며, 0은 양, 1은 늑대를 의미한다
- edges의 원소는 [부모 노드 번호, 자식 노드 번호]의 형태로, 서로 연결된 두 노드를 의미한다
- 동일한 간선에 대한 정보가 중복해서 주어지지 않는다
- 항상 하나의 이진 트리 형태로 입력이 주어지며, 잘못된 데이터가 주어지는 경우는 없다
- 0번 노드는 항상 루트 노드이다

Example:
- Input : info=[0,0,1,1,1,0,1,0,1,0,1,1], edges=[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
- Output : 5

- Input : info=[0,1,0,1,1,0,1,0,0,1,0], edges=[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
- Output : 5

Note:
dfs 방식으로 해결
visited 배열로 방문 여부를 관리
부모 노드에 방문했으면서 자식 노드에 방문하지 않았다면 방문 가능한 노드

 */

class Solution {
    fun solution(info: IntArray, edges: Array<IntArray>): Int {
        var answer = mutableListOf<Int>()
        val visited = BooleanArray(info.size)

        fun solve(sheep: Int, wolf: Int) {
            if (sheep > wolf) answer.add(sheep)
            else return

            for ((parent, child) in edges) {
                if (visited[parent] && !visited[child]) {
                    visited[child] = true
                    if (info[child] == 0) solve(sheep + 1, wolf)
                    else solve(sheep, wolf + 1)
                    visited[child] = false
                }
            }
        }

        visited[0] = true
        solve(1, 0)
        return answer.maxOf { it }
    }
}