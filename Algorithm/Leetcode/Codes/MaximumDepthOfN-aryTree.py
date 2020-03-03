"""

559. Maximum Depth of N-ary Tree : https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

N-ary tree가 주어졌을 때, 해당 트리의 최대 depth를 구하는 문제
- depth는 root 노드에서부터 leaf 노드까지의 길이를 의미한다
- leaf 노드는 자식 노드가 없는 노드이다
- 트리의 최대 depth는 1000이며, 노드의 최대 갯수는 5000개이다

Example:
- Input : 
{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}
- Output : 3

Note:
solve() 함수를 생성하여 recursive하게 해결
level 값을 넘겨주는 방식으로 해당 노드까지의 depth 계산

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root :
            return 0
        def solve(self, node: 'Node', level: int) -> int :
            if not node.children :
                return level
            res = 0
            for i in node.children :
                res = max(res, solve(self, i, level + 1))
            return res
        return solve(self, root, 1)