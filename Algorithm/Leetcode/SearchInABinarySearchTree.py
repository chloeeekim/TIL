"""

700. Search in a Binary Search Tree : https://leetcode.com/problems/search-in-a-binary-search-tree/

binary search tree가 하나 주어졌을 때, 주어진 값과 동일한 노드를 root로 하는 subtree를 찾는 문제
- 만약 주어진 값과 동일한 노드가 없는 경우 NULL(여기서는 None)을 리턴

Example:
- Input : [4,2,7,1,3], 2
- Output : [2,1,3]

- Input : [4,2,7,1,3], 5
- Output : []

Note:
search() 함수를 생성하여 recursive하게 해결
트리를 순회하며 동일한 값을 지닌 노드가 있는지 확인하여 찾는 경우 해당 노드를 return

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def search(self, node: TreeNode) -> TreeNode:
            if node.val == val :
                return node
            res = None
            if node.left :
                res = search(self, node.left) if not res else res
            if node.right :
                res = search(self, node.right) if not res else res
            return res
        return search(self, root)