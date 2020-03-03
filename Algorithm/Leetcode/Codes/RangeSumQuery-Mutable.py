"""

307. Range Sum Query - Mutable : https://leetcode.com/problems/range-sum-query-mutable/

숫자가 포함된 리스트인 nums가 주어졌을 때, i부터 j까지의 합을 구하는 함수를 작성하는 문제
- 입력된 리스트는 update 함수를 통해 변경될 수 있다
- update 함수와 sumRange 함수는 여러 번 호출될 수 있다

Example:
- Input : ["NumArray","sumRange","update","sumRange"], [[[1,3,5]],[0,2],[1,2],[0,2]]
- Output : [null,9,null,8]
- [1,3,5] / sumRange(0,2) -> 9 / update(1,2) -> [1,2,5] / sumRange(0,2) -> 8

Note:
- Solution 1
sumRange 요청이 들어올 때마다 합을 구하는 것이 비효율적이므로,
sums 리스트를 통해 해당 인덱스까지의 전체 합을 저장
하지만 update 함수가 많이 호출되는 케이스의 경우 Time Limit Exceeded
- Solution 2
sumRange 요청이 들어올 때마다 합을 구하는 방식
update 부하가 적어 오히려 Time Limit에 걸리지 않고 통과

"""

# Solution 1
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums, sum = [0], 0
        for num in nums :
            sum += num
            self.sums.append(sum)

    def update(self, i: int, val: int) -> None:
        diff = self.nums[i] - val
        self.nums[i] = val
        for idx in range(i + 1, len(self.nums) + 1) :
            self.sums[idx] -= diff

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]

# Solution 2
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)