"""

965. Univalued Binary Tree : https://leetcode.com/problems/univalued-binary-tree/

주어진 binary tree가 uni-valued인지 확인하는 문제
- 트리의 노드 개수는 1개 이상 100개 이하이다
- 각 노드의 값은 0 이상 100 미만이다

Example:
- Input : root = [1,1,1,1,1,null,1]
- Output : true

- Input : root = [2,2,2,5,2]
- Output : false

Note:
recursive하게 해결
root가 무조건 존재하므로(노드 개수는 1개 이상이므로) 루트 노드와 값을 비교

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val
        def solve(temp):
            if not temp:
                return True
            if temp.val != value:
                return False
            return solve(temp.left) and solve(temp.right)
        return solve(root)