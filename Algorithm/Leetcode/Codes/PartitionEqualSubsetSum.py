"""

416. Partition Equal Subset Sum : https://leetcode.com/problems/partition-equal-subset-sum/

정수로 이루어진 리스트가 주어졌을 때, 이 리스트를 합이 동일한 두 개의 subset으로 나눌 수 있는지 확인하는 문제
- 주어진 리스트는 비어있지 않으며, 양의 정수만 포함된다
- 리스트의 길이는 200을 넘지 않으며, 포함된 정수의 값은 100을 넘지 않는다

Example:
- Input : [1,5,11,5]
- Output : true
- [1,5,5]와 [11]로 나눌 수 있다

- Input : [1,2,3,5]
- Output : false

Note:
solve() 함수를 생성하여 recursive하게 해결
두 개의 subset으로 나누어야 하므로 각 subset의 합은 전체 합의 절반
따라서 리스트의 합이 홀수인 경우 어떤 경우에도 합이 동일한 subset으로 나눌 수 없고,
가장 큰 값이 절반보다 큰 경우에도 합이 동일한 subset으로 나눌 수 없다
이후 리스트의 값을 하나씩 순회하며 합이 전체의 절반이 되는 subset이 만들어지는지 확인
참고) 'max 값이 절반보다 큰 경우'에서 걸러지는 경우가 많은 듯

"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total / 2
        if max(nums) > half:
            return False
        def solve(idx: int, tempsum: int) -> bool:
            if idx < 0 or tempsum >= half:
                return tempsum == half
            return solve(idx-1, tempsum + nums[idx]) or solve(idx-1, tempsum)
        return solve(len(nums)-1, 0)