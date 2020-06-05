"""

60. Permutation Sequence : https://leetcode.com/problems/permutation-sequence/

1부터 n까지의 숫자로 만들 수 있는 permutation 중에서 k번째를 구하는 문제
- n은 1 이상 9 이하이다
- k는 1 이상 n! 이하이다

Example:
- Input : n = 3, k = 3
- Output : "213"
- 123 -> 132 -> 213 -> 231 -> 312 -> 321

- Input : n = 4, k = 9
- Output : "2314"

Note:
itertools의 permutations 함수를 사용
map을 사용하면 int 리스트를 문자열로 join할 수 있다
참고) 더 빠른 방법?

"""

from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        perms = list(permutations(range(1, n+1)))
        return ''.join(map(str, perms[k-1]))