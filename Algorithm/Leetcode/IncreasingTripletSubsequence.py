"""

334. Increasing Triplet Subsequence : https://leetcode.com/problems/increasing-triplet-subsequence/

정렬되지 않은 숫자가 포함된 리스트가 주어졌을 때, 길이가 3인 increasing subsequence가 존재하는지 찾는 문제
- O(n) time complexity와 O(1) space complexity를 만족하여야 한다

Example:
- Input : [1,2,3,4,5]
- Output : true

- Input : [5,4,3,2,1]
- Output : false

Note:
길이가 3 이상인 케이스가 있는지 확인하면 되므로 이전의 리스트에서 i와 j에 해당하는 케이스를 저장
ival < jval을 항상 만족하므로, jval보다 큰 값이 나타나는 경우 true
참고) not ival(jval)로 확인하는 경우 0이 들어가는 케이스가 문제가 됨

"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3 :
            return False
        ival, jval = None, None
        for num in nums :
            if ival == None or ival >= num :
                ival = num
            elif jval == None or jval >= num :
                jval = num
            else :
                return True
        return False