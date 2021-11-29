"""

888. Fair Candy Swap : https://leetcode.com/problems/fair-candy-swap/

alice와 bob이 동일한 개수의 캔디를 가질 수 있도록 하려면 어떤 캔디 박스를 교환해야 하는지 구하는 문제
- alice와 bob이 가지고 있는 캔디 박스 내의 개수가 list 형태로 주어진다
- 답이 여러 개 존재하는 경우 어떤 답을 제출하더라도 상관 없다
- 처음 주어지는 alice와 bob의 전체 캔디의 개수는 다르다
- 적어도 하나의 유효한 답이 존재한다

Example:
- Input : aliceSizes = [1,1], bobSizes = [2,2]
- Output : [1,2]

- Input : aliceSizes = [1,2], bobSizes = [2,3]
- Output : [1,2]

- Input : aliceSizes = [2], bobSizes = [1,3]
- Output : [2,3]

- Input : aliceSizes = [1,2,5], bobSizes = [2,4]
- Output : [5,4]

Note:
유효한 답이 존재한다는 가정이 있으므로, alice 내에서 x와 bob 내에서 y의 캔디 박스를 교환한다고 했을 때,
sum(alice)-x+y = sum(bob)+x-y가 성립하고,
y가 bob이 가진 캔디 박스 list 내에 있다면 답이 된다

"""

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diffsum, setbob = sum(bobSizes) - sum(aliceSizes), set(bobSizes)
        for num in aliceSizes:
            if num + diffsum // 2 in setbob:
                return [num, num + diffsum // 2]
