"""

598. Range Addition : https://leetcode.com/problems/range-addition-ii/

모두 0으로 초기화된 m x n matrix와 ops가 주어졌을 때, matrix 내에 가장 큰 숫자의 개수를 리턴하는 문제
- ops[i]는 [a_i, b_i]로 구성되어 있다
- 0 <= x < a_i, 0 <= y < b_i를 만족하는 M[x][y]는 1씩 증가한다
- a_i는 m을 넘지 않으며, b_i는 n을 넘지 않는다

Example:
- Input : m = 3, n = 3, ops = [[2,2],[3,3]]
- Output : 4

- Input : m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
- Output : 4

Note:
a_i와 b_i가 만드는 가장 작은 범위가 가장 큰 숫자의 범위가 된다

"""

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        mina, minb = m, n
        for a, b in ops:
            mina = min(mina, a)
            minb = min(minb, b)
        return mina * minb