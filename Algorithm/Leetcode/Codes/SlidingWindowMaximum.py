"""

239. Sliding Window Maximum : https://leetcode.com/problems/sliding-window-maximum/

리스트 nums와 sliding window의 사이즈 k가 주어졌을 때, window 내의 maximum 값을 순서대로 구하는 문제
- sliding window는 왼쪽에서 오른쪽으로 이동한다
- k는 1 이상 nums의 길이 이하이다

Example:
- Input : nums = [1,3,-1,-3,5,3,6,7], k = 3
- Output : [3,3,5,5,6,7]

- Input : nums = [1], k = 1
- Output : [1]

Note:
SortedList를 사용하여 해결

"""

from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = SortedList([])
        for i in range(k):
            window.add(nums[i])
        ans = []
        for i in range(k, len(nums)):
            ans.append(window[-1])
            window.add(nums[i])
            window.remove(nums[i-k])
        ans.append(window[-1])
        return ans