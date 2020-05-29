"""

922. Sort Array By Parity II : https://leetcode.com/problems/sort-array-by-parity-ii/

음수가 아닌 숫자로 이루어진 리스트 A가 주어졌을 때, 홀수번째 인덱스에는 홀수가, 짝수번째 인덱스에는 짝수가 위치하도록 재정렬하는 문제
- A의 길이는 2 이상 20000 이하인 2의 배수이다
- A에 포함된 숫자의 범위는 0 이상 1000 이하이다
- 조건을 만족한다면 리스트의 순서는 상관 없다

Example:
- Input : [4,2,5,7]
- Output : [4,5,2,7]
- [4,7,2,5], [2,5,4,7], [2,7,4,5] 모두 가능

Note:
다음 even, odd가 위치할 인덱스를 저장
A를 순회하면서 홀수가 등장하면 결과 리스트의 홀수번째에, 짝수가 등장하면 결과 리스트의 짝수번째에 위치하는 방법

"""

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0 for _ in range(len(A))]
        even, odd = 0, 1
        for num in A:
            if num%2 == 0:
                res[even] = num
                even += 2
            else:
                res[odd] = num
                odd += 2
        return res