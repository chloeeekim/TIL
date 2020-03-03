"""

701. Insert into a Binary Search Tree : https://leetcode.com/problems/insert-into-a-binary-search-tree/

binary search tree와 값 하나가 주어졌을 때, BST가 유지되도록 해당 값을 지닌 노드를 추가하는 문제
- 답은 여러 가지 경우가 될 수 있으며, 어느 것이건 BST를 유지하는 방향이면 된다

Example:
- Input : [4,2,7,1,3], 5
- Output : [4,2,7,1,3,5]

Note:
insert() 함수를 생성하여 recursive하게 해결
트리를 순회하면서 해당 값이 들어갈 수 있는 위치를 찾아 추가하는 방식
BST이므로 값의 크기에 따라 왼쪽 자식 노드 혹은 오른쪽 자식 노드만 확인하면 된다

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(self, node: TreeNode) :
            if node.val < val :
                if node.right :
                    insert(self, node.right)
                else :
                    node.right = TreeNode(val)
            else :
                if node.left :
                    insert(self, node.left)
                else :
                    node.left = TreeNode(val)
        insert(self, root)
        return root