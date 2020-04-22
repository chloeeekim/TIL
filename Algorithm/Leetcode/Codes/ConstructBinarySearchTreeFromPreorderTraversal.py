"""

1008. Construct Binary Search Tree from Preorder Traversal : https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

트리를 preorder traversal한 결과가 list로 주어졌을 때, 이를 BST로 변환하는 문제
- preorder traversal: 각 subtree에서 루트를 먼저 방문하고, 왼쪽 subtree와 오른쪽 subtree를 순서대로 방문한다
- 주어지는 list의 길이는 1 이상 100 이하이다
- 주어지는 preorder list에 중복되는 값은 없다

Example:
- Input : [8,5,1,7,10,12]
- Output : [8,5,10,1,7,null,12]

Note:
construct() 함수를 생성하여 recursive하게 해결
preorder로 순회하므로 리스트의 첫 원소가 subtree의 root가 된다
남은 리스트에서 root보다 큰 값이 나오기 이전까지는 left subtree가, 큰 값들은 right subtree를 구성한다

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def construct(self, arr: List[int]) -> TreeNode:
            root = TreeNode(arr[0])
            idx = length = len(arr)
            for i in range(1, length):
                if arr[i] > arr[0]:
                    idx = i
                    break
            root.left = construct(self, arr[1:idx]) if idx > 1 else None
            root.right = construct(self, arr[idx:]) if idx < length else None
            return root
        return construct(self, preorder)