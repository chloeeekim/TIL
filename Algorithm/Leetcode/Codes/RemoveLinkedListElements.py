"""

203. Remove Linked List Element : https://leetcode.com/problems/remove-linked-list-elements/

정수로 이루어진 linked list와 정수가 하나 주어졌을 때,
주어진 정수에 해당하는 노드를 제외한 linked list 리스트를 만드는 문제

Example:
- Input : 1->2->6->3->4->5->6, val = 6
- Output : 1->2->3->4->5

Note:
val과 동일한 원소가 있으면 해당 노드를 삭제하고 다음 노드를 연결하는 방법으로 구현
문제에서 'remove all elements'라고 하였으므로 리스트를 전부 다 확인

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = ListNode(-1)
        res.next, before, node = head, res, head
        while node :
            if node.val == val :
                before.next = node.next
                node = node.next
            else :
                before = before.next
                node = node.next
        return res.next