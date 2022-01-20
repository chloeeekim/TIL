"""

179. Largest Number : https://leetcode.com/problems/largest-number/

음수가 아닌 정수로 이루어진 리스트 nums가 주어졌을 때, 만들 수 있는 가장 큰 숫자를 구하는 문제
- 결과값이 매우 크므로 숫자 대신 문자열로 리턴할 것
- 주어지는 숫자는 0 이상 10^9 이하이다
- nums의 길이는 1 이상 100 이하이다

Example:
- Input : nums = [10,2]
- Output : "210"

- Input : nums = [3,30,34,5,9]
- Output : "9534330"

Note:
greedy하게 해결
문자열로 변경한 다음 큰 숫자가 만들어지도록 정렬
참고) lambda를 사용하여 해결해보기

"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if set(nums) == {0}:
            return "0"
        l = len(nums)
        if l == 1:
            return str(nums[0])
        nums = list(map(str, nums))
        for i in range(l):
            for j in range(i+1, l):
                s1 = nums[i]+nums[j]
                s2 = nums[j]+nums[i]
                if s1 <= s2:
                    nums[i], nums[j] = nums[j], nums[i]
        return "".join(nums)