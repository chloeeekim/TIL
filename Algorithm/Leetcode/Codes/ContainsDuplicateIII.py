"""

220. Contains Duplicate III : https://leetcode.com/problems/contains-duplicate-iii/

숫자들이 포함된 리스트와 숫자 k, t가 주어졌을 때,
해당 리스트에 최대 k만큼의 거리가 차이나며, 최대 t만큼 값이 차이나는 케이스가 있는지를 구하는 문제

Example:
- Input : [1,2,3,1], k = 3, t = 0
- Output : true

- Input : [1,0,1,1], k = 1, t = 2
- Output : true

- Input : [1,5,9,1,5,9], k = 2, t = 3
- Output : false

Note:
이전에 순회한 값의 scope를 list에 저장하여 확인하는 방법
거리가 k 이내여야 하므로 해당 거리를 벗어나는 경우 list에서 삭제
참고) 더 효율적인 방법? time limit을 겨우 벗어난 수준...

"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) < 2 or k < 1 or t < 0 :
            return False
        seen = []
        for i, num in enumerate(nums) :
            for scope in seen :
                if num >= scope[0] and num <= scope[1] :
                    return True
            scope = [num - t, num + t]
            seen.append(scope)
            if len(seen) > k :
                del seen[0]
        return False