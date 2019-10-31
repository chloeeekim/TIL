"""

303. Range Sum Query - Immutable : https://leetcode.com/problems/range-sum-query-immutable/

숫자가 포함된 리스트인 nums가 주어졌을 때, i부터 j까지의 합을 구하는 함수를 작성하는 문제
- 입력된 리스트는 변경되지 않는다
- sumRange 함수는 여러 번 호출될 수 있다

Example:
- Input : ["NumArray","sumRange","sumRange","sumRange"], [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]
- Output : [null,1,-1,-3]
- sumRange(0,2) -> 1 / sumRange(2,5) -> -1, sumRange(0,5) -> -3

Note:
sumRange 요청이 들어올 때마다 합을 구하는 것은 비효율적
nums 리스트의 순서나 값이 변경되지 않고, 특정 구간의 합만 구하면 되므로
sums 리스트를 생성하여 해당 인덱스까지의 전체 합을 저장
sums[0] = 0이 되도록 생성하면 i부터 j까지의 합은 sums[j+1] - sums[i]가 된다

"""

class NumArray:
    def __init__(self, nums: List[int]):
        self.sums, sum = [0], 0
        for num in nums :
            sum += num
            self.sums.append(sum)
            
    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)