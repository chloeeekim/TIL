"""

382. Linked List Random Node : https://leetcode.com/problems/linked-list-random-node/

linked list가 주어졌을 때, 각 노드의 값을 랜덤하게 리턴하는 함수를 생성하는 문제
- 각 노드의 값은 랜덤하지만 동일한 비율로 출력되어야 한다

Example:
- Input : ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
- Output : [null, 1, 3, 2, 2, 3]

Note:
노드의 값을 리스트에 추가한 다음 randomrange 함수를 사용하여 특정 값을 선택하는 방식
참고) Reservoir Sampling에 대해 알아볼 것

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next
        self.len = len(self.nums)

    def getRandom(self) -> int:
        rand = random.randrange(0, self.len)
        return self.nums[rand]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()