"""

897. Increasing Order Search Tree : https://leetcode.com/problems/increasing-order-search-tree/

binary search tree가 주어졌을 때, in-order로 순회한 결과를 새로운 tree로 변환하는 문제
- 결과 트리의 모든 노드의 왼쪽 자식 노드는 없으며, 오른쪽 자식 노드만 존재한다
- 주어진 트리의 노드의 개수는 1 이상 100 이하이다
- 각 노드는 0부터 1000까지의 unique한 값을 지닌다

Example:
- Input : [5,3,6,2,4,null,8,1,null,null,null,7,9]
- Output : [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Note:
getList() 함수를 생성하여 recursive하게 트리를 in-order로 순회하여 노드 list를 생성
구해진 노드 리스트로 새로운 트리를 구성하는 방식

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def getList(self, node: TreeNode):
            if node.left:
                getList(self, node.left)            
            nodes.append(node.val)
            if node.right:
                getList(self, node.right)
        nodes, res = [], TreeNode(-1)
        getList(self, root)
        tmp = res
        for node in nodes:
            tmp.right = TreeNode(node)
            tmp = tmp.right
        return res.right