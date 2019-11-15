"""

78. Subsets : https://leetcode.com/problems/subsets/

모두 다른 정수가 포함된 nums 리스트가 주어졌을 때, 가능한 모든 subset들을 구하는 문제
- 중복되는 subset이 포함되어서는 안 된다

Example:
- Input : nums = [1,2,3]
- Output : [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

Note:
solve() 함수를 생성하여 recursive하게 해결
nums 리스트에 중복되는 정수가 없으므로 함수가 호출될 때 생기는 모든 temp는 중복되지 않음을 보장
[1,2]와 [2,1]은 중복이므로, remain의 앞부분([:idx])은 고려할 필요가 없다

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def solve(self, temp: List[int], remain: List[int]) :
            if temp :
                res.append(temp)
            if not remain :
                return
            for idx, i in enumerate(remain) :
                solve(self, temp + [i], remain[idx+1:])
        solve(self, [], nums)
        return res