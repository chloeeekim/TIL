"""

491. Increasing Subsequences : https://leetcode.com/problems/increasing-subsequences/

숫자로 이루어진 list가 주어졌을 때, 만들 수 있는 모든 increasing subsequences를 찾는 문제
- increasing subsequence의 길이는 최소 2 이상이어야 한다
- 주어지는 list의 길이는 15를 넘지 않는다
- list에 포함된 숫자는 [-100,100] 범위이다
- 주어지는 list에는 중복이 포함될 수 있다

Example:
- Input : [4, 6, 7, 7]
- Output : [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

- Input : [4,3,2,1]
- Output : []

Note:
solve() 함수를 생성하여 해결
중복 제거를 위해 set을 사용하였으나, list를 set에 add할 수 없으므로 tuple을 사용

"""

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res, l = set(), len(nums)
        def solve(self, idx: int, temp=()):
            if idx >= l:
                if len(temp) > 1:
                    res.add(temp)
                return
            solve(self, idx+1, temp)
            if not temp or temp[-1] <= nums[idx]:
                solve(self, idx+1, temp+(nums[idx],))
        solve(self, 0)
        return list(res)