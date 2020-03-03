"""

86. Partition List : https://leetcode.com/problems/partition-list/

Linked List와 숫자 x가 주어졌을 때,
x보다 작은 노드가 x보다 크거나 같은 노드보다 앞에 위치하는 Linked List로 바꾸는 문제
- 기존 노드의 상대적인 순서는 유지되어야 한다

Example:
- Input : head = 1->4->3->2->5->2, x = 3
- Output : 1->2->2->4->3->5

Note:
x보다 작은 리스트(less)와 큰 리스트(greater)로 구분한 뒤,
큰 리스트를 작은 리스트의 뒤에 붙이는 방법으로 구현

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less, greater = ListNode(-1), ListNode(-1)
        less_now, greater_now = less, greater
        node = head
        while node :
            if node.val < x :
                less_now.next = ListNode(node.val)
                less_now = less_now.next
            else :
                greater_now.next = ListNode(node.val)
                greater_now = greater_now.next
            node = node.next
        less_now.next = greater.next
        return less.next