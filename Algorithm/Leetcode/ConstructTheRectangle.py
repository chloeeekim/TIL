"""

492. Construct the Rectangle : https://leetcode.com/problems/construct-the-rectangle/

area의 사이즈가 주어졌을 때, width와 height의 차이가 최소가 되는 값을 구하는 문제
- width와 height의 곱은 area와 정확히 일치해야 한다
- width는 height보다 작거나 같아야 한다 (L >= W)
- 결과는 height, width의 순서로 나타낸다
- 주어지는 area는 10,000,000을 넘지 않으며, 양의 정수로 주어진다

Example:
- Input : 4
- Output : [2,2]
- [1,4], [2,2], [4,1] 세 가지 경우가 가능하지만, [1,4]는 width가 더 크므로 안 되고, [4,1]은 [2,2]보다 차이가 크므로 안 된다

Note:
width와 height의 차이가 가장 작은 경우: 동일한 경우 (square root)
차이가 최소가 되는 경우를 구해야 하므로 root 값에서부터 시작하여 값을 1씩 변경하며 확인

"""

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(area ** 0.5)
        while area % width != 0 :
            width -= 1
        return [int(area / width), width]