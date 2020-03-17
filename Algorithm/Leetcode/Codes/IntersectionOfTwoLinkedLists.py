"""

160. Intersection of Two Linked Lists : https://leetcode.com/problems/intersection-of-two-linked-lists/

두 개의 linked list가 주어졌을 때, 겹치는 부분을 구하는 문제
- 겹치는 경우 intersection이 시작되는 노드를 리턴
- 겹치지 않는 경우 null(None)을 리턴

Example:
- Input : intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
- Output : node with value = 8

- Input : intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
- Output : node with value = 2

- Input : intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
- Output : None

Note:
우선 A list를 순회하면서 발견한 노드를 전부 seen에 추가
이후 B list를 순회하며 이전에 발견한 노드가 있다면 해당 노드부터 intersection이 시작되므로 해당 노드를 리턴
B list를 전부 순회할 때까지 seen에 있는 노드가 발견되지 않는다면 intersection이 존재하지 않는다

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set()
        node = headA
        while node :
            seen.add(node)
            node = node.next
        node = headB
        while node :
            if node in seen :
                return node
            node = node.next
        return None