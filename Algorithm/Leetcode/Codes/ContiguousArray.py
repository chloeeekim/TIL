"""

525. Contiguous Array : https://leetcode.com/problems/contiguous-array/

binary array가 주어졌을 때, 0과 1의 개수가 동일한 contiguous subarray의 최대 길이를 구하는 문제
- 주어진 array의 길이는 50,000을 넘지 않는다

Example:
- Input : [0,1]
- Output : 2
- 0과 1의 개수가 동일한 longest contiguous subarray : [0,1]

- Input : [0,1,0]
- Output : 2
- 0과 1의 개수가 동일한 longest contiguous subarray : [0,1] 혹은 [1,0]

Note:
dict를 사용하여 해결
숫자가 두 종류만 나오기 때문에 1이면 1을 더하고, 0이면 1을 빼는 방식으로 구한 값이 이전에 있었다면,
해당 인덱스부터 현재 인덱스까지의 subarray는 0과 1의 개수가 동일하다
최대 길이를 구하는 문제이므로 dict의 값을 갱신하지 않고, 없는 경우에만 추가

"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        temp, count, maxlength = {0: -1}, 0, 0
        for idx in range(len(nums)):
            count = count+1 if nums[idx] == 1 else count-1
            if count in temp:
                maxlength = max(maxlength, idx-temp[count])
            else:
                temp[count] = idx
        return maxlength