"""

82. Remove Duplicates From Sorted List II : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

정렬된 숫자로 이루어진 Linked List가 하나 주어졌을 때, 중복된 값이 존재하는 모든 노드를 제거한 리스트를 만드는 문제

Example:
- Input : 1->2->3->3->4->4->5
- Output : 1->2->5

- Input : 1->1->1->2->3
- Output : 2->3

Note:
linked list를 순회하면서 해당 숫자가 몇 번 등장하는지를 확인하여 dict로 관리
한 번만 등장하는 숫자들만 새로운 linked list로 재구성

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        seen = {}
        node = head
        while node :
            if node.val in seen :
                seen[node.val] += 1
            else :
                seen[node.val] = 1
            node = node.next
        res = ListNode(-1)
        node = res
        for key, val in seen.items() :
            if val == 1 :
                node.next = ListNode(key)
                node = node.next
        return res.next