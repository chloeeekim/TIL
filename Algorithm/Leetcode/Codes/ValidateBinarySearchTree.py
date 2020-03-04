"""

98. Validate Binary Search Tree : https://leetcode.com/problems/validate-binary-search-tree/

Binary Tree가 하나 주어졌을 때, valid한 BST인지 확인하는 문제
BST의 정의는 다음과 같다
- 왼쪽 서브트리는 해당 노드의 키값보다 작은 값으로만 이루어져야 한다
- 오른쪽 서브트리는 해당 노드의 키값보다 큰 값으로만 이루어져야 한다
- 각각의 왼쪽과 오른쪽 서브트리 역시 BST의 정의를 만족해야 한다

Example:
- Input : [2,1,3]
- Output : True

- Input : [5,1,4,null,null,3,6]
- Output : False

Note:
isValid() 함수를 생성하여 recursive하게 해결
트리를 순회하며 각 서브트리의 min, max 범위를 벗어나는 경우 False
최소값과 최대값을 정의하기 위해 각각 -sys.maxmize -1과 sys.maxmize 값을 사용

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root :
            return True
        def isValid(self, node: TreeNode, minval: int, maxval: int) -> bool:
            res = True
            if node.left :
                val = node.left.val
                if val >= node.val or val <= minval or val >= maxval :
                    return False
                else :
                    res = isValid(self, node.left, minval, min(maxval, node.val))
            if node.right : 
                val = node.right.val
                if val <= node.val or val <= minval or val >= maxval :
                    return False
                else :
                    res = res if isValid(self, node.right, max(minval, node.val), maxval) else False
            return res
        return isValid(self, root, -sys.maxsize -1, sys.maxsize)