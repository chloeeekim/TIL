/*

모두 0으로 만들기 : https://school.programmers.co.kr/learn/courses/30/lessons/76503

각 점에 가중치가 부여된 트리가 주어졌을 때, 특정 연산을 통하여 트리의 모든 점들의 가중치를 0으로 만드는 데 필요한 최소 횟수를 구하는 문제
- 다음 연산을 반복한다
    - 임의의 연결된 두 점을 골라서 한쪽은 1 증가시키고, 다른 한쪽은 1 감소시킨다
- 위 행동을 통해 트리의 모든 점들의 가중치를 0으로 만드는 것이 불가능하다면 -1을 리턴한다
    - 만약 처음부터 트리의 모든 정점의 가중치가 0이라면, 0을 리턴한다
- 트리의 각 점의 가중치를 의미하는 1차원 정수 배열 a의 길이는 2 이상 300,000 이하이다
    - a의 모든 수는 각각 -1,000,000 이상 1,000,000 이하이다
    - a[i]는 i번 정점의 가중치를 의미한다
- 트리의 간선 정보를 의미하는 배열 edges의 행의 개수는 a의 길이 -1이다
    - edges의 각 행은 [u, v]와 같이 2개의 정수로 이루어져 있으며, u번 정점과 v번 정점이 간선으로 연결되어 있음을 의미한다
    - edges가 나타내는 그래프는 항상 트리로 주어진다

Example:
- Input : a=[-5,0,2,1,2], edges=[[0,1],[3,4],[2,3],[0,3]]
- Output : 9

- Input : a=[0,1,0], edges=[[0,1],[1,2]]
- Output : -1

Note:
트리의 가중치들의 합이 0이 아니라면 모든 가중치를 0으로 만들 수 없으므로 -1을 리턴
루트 노드(0번 노드)에서부터 시작하여 dfs 방식으로 가중치를 더하는 방식
어떤 노드든 루트 노드가 될 수 있으며, 0번 노드는 항상 존재하므로 0번 노드를 루트로 가정
특정 테스트 케이스에서 런타임 에러가 발생하는데, 전역함수 + 전역변수로 사용하여 런타임 에러 발생하지 않도록 해결

 */

import kotlin.math.abs

val maxNum = 300000
val aLong = LongArray(maxNum)
val tree = Array(maxNum) { mutableListOf<Int>() }
var answer = 0L

fun solve(curr: Int, parent: Int): Long {
    var ret = aLong[curr]
    for (i in 0 until tree[curr].size) {
        if (tree[curr][i] == parent) continue
        ret += solve(tree[curr][i], curr)
    }
    answer += abs(ret)
    return ret
}

class Solution {
    fun solution(a: IntArray, edges: Array<IntArray>): Long {
        if (a.sum() != 0) return -1

        for (i in a.indices) { aLong[i] = a[i].toLong() }
        for ((u, v) in edges) {
            tree[u].add(v)
            tree[v].add(u)
        }

        return if (solve(0, -1) != 0L) -1L else answer
    }
}