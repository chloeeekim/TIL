"""

653. Two Sum IV - Input is a BST : https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

Binary Search Tree가 하나 주어졌을 때, 두 노드의 합이 target이 되는 노드가 존재하는지 찾는 문제

Example:
- Input : [5,3,6,2,4,null,7], target = 9
- Output : True

- Input : [5,3,6,2,4,null,7], target = 28
- Output : False

Note:
solve() 함수를 생성하여 recursive하게 해결
트리를 순회하면서 합이 target이 되는 노드가 있었는지 확인하는 방식
참고) 노드의 값과 target이 음수가 되는 케이스 존재

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = {}
        def solve(self, node: TreeNode) -> bool :
            if node.val in seen :
                return True
            else :
                seen[k - node.val] = 1
            res  = False
            if node.left :
                res = res or solve(self, node.left)
            if node.right :
                res = res or solve(self, node.right)
            return res
        return solve(self, root)