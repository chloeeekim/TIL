"""

237. Delete Node in a Linked List : https://leetcode.com/problems/delete-node-in-a-linked-list/

linked list 내에서 주어진 node를 제거하는 문제
- linked list에는 적어도 두 개 이상의 노드가 존재한다
- 모든 노드의 값은 unique하다
- 주어진 node는 linked list의 tail이 아니며, 항상 valid한 값이 주어진다
- 아무것도 return하지 말고 in-place로 해결할 것

Example:
- Input : head = [4,5,1,9], node = 5
- Output : [4,1,9]

- Input : head = [4,5,1,9], node = 1
- Output : [4,5,9]

Note:
문제의 input을 이해하는 데 시간이 많이 소요되고 시행착오가 많았다..
example에는 head라는 input이 있는 것처럼 보였지만 실제로는 node 값만 넘어오기 때문에
node를 node.next로 변경하면 되는 문제

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val, node.next = node.next.val, node.next.next