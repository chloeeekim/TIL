"""

684. Redundant Connection : https://leetcode.com/problems/redundant-connection/

N개의 노드들이 어떻게 연결되어 있는지를 나타내는 edge의 리스트가 주어졌을 때, cycle이 생기지 않도록 지워야 하는 하나의 edge를 찾는 문제
- 정답이 여러 개가 될 수 있다면, 마지막에 주어진 edge를 출력한다
- 각 edge는 undirected이며, [u, v]는 u와 v 노드가 연결된 것을 의미한다
- 주어진 edge의 리스트의 길이는 3 이상 1000 이하이다
- 주어진 리스트의 길이는 N이며, 노드는 1부터 N까지 존재한다

Example:
- Input : [[1,2], [1,3], [2,3]]
- Output : [2,3]

- Input : [[1,2], [2,3], [3,4], [1,4], [1,5]]
- Output : [1,4]

Note:
union-find 방식으로 cycle이 생기는지를 판단하여 해결
cycle에 속한 edge가 여러 개일 때, 마지막 노드를 출력하면 되므로, cycle이 생기는 시점의 edge를 출력

"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = {}
        def findRoot(node: int) -> int:
            while union[node] != -1:
                node = union[node]
            return node
        for [u, v] in edges:
            if u not in union and v not in union:
                union[u] = -1
                union[v] = u
            elif u not in union and v in union:
                union[u] = v
            elif u in union and v not in union:
                union[v] = u
            else:
                uroot = findRoot(u)
                vroot = findRoot(v)
                if uroot == vroot :
                    return [u, v]
                union[vroot] = uroot