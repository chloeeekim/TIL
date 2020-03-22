"""

605. Can Place Flowers : https://leetcode.com/problems/can-place-flowers/

flowerbed에 식물이 심어져 있는 상태와 심어야 하는 식물의 개수가 주어졌을 때, 서로 인접하지 않도록 심는 것이 가능한지 확인하는 문제

Example:
- Input : flowerbed = [1,0,0,0,1], n = 1
- Output : True

- Input : flowerbed = [1,0,0,0,1], n = 2
- Output : False

Note:
인덱스 처리 대신 flowerbed의 앞뒤로 [0]을 붙여서 처리
해당 인덱스의 값이 0이며 양 옆의 인덱스의 값도 0이면 식물을 심을 수 있다
최종적으로 n개 (혹은 이상의) 식물을 심을 수 있다면 True

"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, flowerbed = 0, [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1) :
            if flowerbed[i] == 1 :
                continue
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 :
                flowerbed[i] = 1
                count += 1
            if count == n :
                return True
        return True if count >= n else False