"""

108. Convert Sorted Array to Binary Search Tree : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

정렬된 리스트가 주어졌을 때, height balanced BST로 변환하는 문제
- height-balanced BST란 각 서브트리의 높이 차이가 1보다 크지 않은 경우이다

Example:
- Input : [-10,-3,0,5,9]
- Output : [0,-3,9,-10,null,5]

Note:
makeBST() 함수를 생성하여 recursive하게 해결
각 서브트리에서 루트 노드가 되는 건 해당 리스트의 중앙에 위치한 원소
BST이므로 루트 노드를 기준으로 왼쪽 리스트는 왼쪽 서브트리를, 오른쪽 리스트는 오른쪽 서브트리를 구성하게 된다

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def makeBST(self, parent: TreeNode, temp: List[int], isLeft: bool) :
            if not temp:
                return
            rootidx = int(len(temp) / 2)
            root = TreeNode(temp[rootidx])
            if isLeft :
                parent.left = root
            else :
                parent.right = root
            makeBST(self, root, temp[0:rootidx], True)
            makeBST(self, root, temp[rootidx+1:], False)
        tree = TreeNode(None)
        makeBST(self, tree, nums, False)
        return tree.right