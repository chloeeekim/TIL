"""

24. Swap Nodes in Pairs : https://leetcode.com/problems/swap-nodes-in-pairs/

linked list가 주어졌을 때, 두 개의 노드씩 순서를 바꾸는 문제
- node의 값을 변경하지 말고 노드 자체의 순서를 바꿀 것

Example:
- Input : 1->2->3->4
- Output : 2->1->4->3

Note:
반복문을 돌면서 두 개씩 swap
노드가 홀수개인 경우 마지막은 swap이 불가능하므로 break

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(-1)
        res.next = head
        node = res
        while node.next :
            first = node.next
            second = first.next
            if not second :
                break
            first.next = second.next
            node.next = second
            node = second.next = first
        return res.next