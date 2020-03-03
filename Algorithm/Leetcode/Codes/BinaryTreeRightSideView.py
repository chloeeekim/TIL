"""

199. Binary Tree Right Side View : https://leetcode.com/problems/binary-tree-right-side-view/

binary tree가 하나 주어졌을 때, 해당 트리를 오른쪽에서 본 결과를 구하는 문제
- 결과는 top에서 bottom 순서

Example:
- Input : [1,2,3,null,5,null,4]
- Output : [1,3,4]

Note:
getview() 함수를 만들어서 recursive하게 해결
왼쪽에서부터 depth first search로 트리를 순회하며 view 리스트를 갱신

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        view = []
        def getview(self, node: TreeNode, depth: int) :
            if len(view) < depth :
                view.append(node.val)
            else :
                view[depth-1] = node.val
            if node.left :
                getview(self, node.left, depth+1)
            if node.right :
                getview(self, node.right, depth+1)
        getview(self, root, 1)
        return view