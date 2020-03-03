"""

90. Subsets II : https://leetcode.com/problems/subsets-ii/

정수가 포함된 nums 리스트가 주어졌을 때, 가능한 모든 subset들을 구하는 문제
- nums 리스트에는 중복된 숫자가 포함되어 있을 수 있다
- 중복되는 subset이 포함되어서는 안 된다

Example:
- Input : nums = [1,2,2]
- Output : [[],[1],[2],[1,2],[2,2],[1,2,2]]

Note:
solve() 함수를 생성하여 recursive하게 해결
nums 리스트에 중복되는 정수가 존재하므로 res에 append하기 전에 중복 확인
remain의 앞부분([:idx])을 고려하지 않기 위해 nums를 정렬하여 사용

"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        def solve(self, temp: List[int], remain: List[int]) :
            if temp and temp not in res :
                res.append(temp)
            if not remain :
                return
            for idx, i in enumerate(remain) :
                solve(self, temp + [i], remain[idx+1:])
        solve(self, [], nums)
        return res