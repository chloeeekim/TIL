/*

섬 연결하기 : https://school.programmers.co.kr/learn/courses/30/lessons/42861

n개의 섬 사이에 다리를 건설하는 비용이 주어질 때, 최소의 비용으로 모든 섬이 통행 가능하도록 만들 때 필요한 최소 비용을 구하는 문제
- 다리를 여러 번 건너더라도, 도달할 수 있다면 통행 가능하다고 본다
- 섬의 개수 n은 1 이상 100 이하이다
- 다리를 건설하는 비용 정보 배열 costs의 길이는 ((n-1) * n) / 2 이하이다
    - 임의의 i에 대해, costs[i][0]와 costs[i][1]는 다리가 연결되는 두 섬의 번호이고, costs[i][2]에는 두 섬을 연결하는 다리를 건설할 때 드는 비용이다
    - 같은 연결은 두 번 주어지지 않는다 (순서가 바뀌더라도 같은 연결로 본다)
    - 모든 섬 사이의 다리 건설 비용이 주어지지 않는다
        - 이 경우, 두 섬 사이의 건설이 불가능한 것으로 본다
    - 연결할 수 없는 섬은 주어지지 않는다

Example:
- Input : n=4, costs=[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
- Output : 4

Note:
크루스칼 알고리즘을 사용하여 해결
cost가 작은 순으로 정렬하여 기존에 연결된 정보와 비교 후 추가를 결정
a와 b가 둘 다 연결되어 있는 경우, 사이클이 생기는 것이므로 제외

 */

class Solution {
    fun solution(n: Int, costs: Array<IntArray>): Int {
        val sCosts = costs.sortedBy { it[2] }
        val connected = mutableSetOf<Int>()
        connected.add(sCosts[0][0])
        var answer = 0

        while (connected.size < n) {
            for ((a, b, cost) in sCosts) {
                if (a in connected && b in connected) continue
                else if (a in connected || b in connected) {
                    connected.add(a)
                    connected.add(b)
                    answer += cost
                    break
                }
            }
        }

        return answer
    }
}