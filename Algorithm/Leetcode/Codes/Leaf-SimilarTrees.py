"""

872. Leaf-Similar Trees : https://leetcode.com/problems/leaf-similar-trees/

두 개의 binary tree가 주어졌을 때, leaf 노드의 sequence가 동일한지 확인하는 문제
- 각 트리의 노드의 개수는 1 이상 200 이하이다
- 트리의 노드의 값은 0 이상 200 이하이다

Example:
- Input : tree1 = [3,5,1,6,2,9,8,null,null,7,4], tree2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
- Output : true
- leaf value sequence = [6,7,4,9,8]

Note:
getSeq() 함수를 생성하여 recursive하게 해결
두 트리의 leaf value sequence를 구한 후, 동일한 지 확인

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getSeq(self, node: TreeNode, arr: List[int]):
            if not node.left and not node.right:
                arr.append(node.val)
                return
            if node.left:
                getSeq(self, node.left, arr)
            if node.right:
                getSeq(self, node.right, arr)
        arr1, arr2 = [], []
        getSeq(self, root1, arr1)
        getSeq(self, root2, arr2)
        return arr1 == arr2