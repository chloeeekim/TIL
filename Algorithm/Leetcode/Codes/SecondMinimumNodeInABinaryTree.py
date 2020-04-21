"""

671. Second Minimum Node In a Binary Tree : https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

binary tree가 주어졌을 때, 두 번째로 작은 노드의 값을 찾는 문제
- 두 번째로 작은 값이 존재하지 않는 경우 -1을 리턴

Example:
- Input : [2,2,5,null,null,5,7]
- Output : 5
- 가장 작은 값은 2이고, 두 번째로 작은 값은 5

- Input : [2,2,2]
- Output : -1
- 두 번째로 작은 값이 존재하지 않는다

Note:
solve() 함수를 생성하여 트리를 순회
중복을 제거하기 위하여 set에 노드의 값을 add하고, 최종적으로 set을 정렬하여 두 번째로 작은 값을 찾는 방식

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        nodes = set()
        def solve(self, node: TreeNode):
            nodes.add(node.val)
            if node.left:
                solve(self, node.left)
            if node.right:
                solve(self, node.right)
        solve(self, root)
        return sorted(nodes)[1] if len(nodes) > 1 else -1