"""

96. Unique Binary Search Trees : https://leetcode.com/problems/unique-binary-search-trees/

1부터 n까지의 숫자로 만들 수 있는 유니크한 BST의 개수를 구하는 문제

Example:
- Input : 3
- Output : 5

Note:
숫자가 없거나 1개만 있는 경우에는 1가지 트리만 가능하고, 2개가 있는 경우에는 2가지 트리가 가능
3개 이상부터는 부모 노드가 정해졌을 때, 자식 노드(트리)로 가능한 경우의 수를 계산

"""

class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2 :
            return 1
        if n == 2 :
            return 2
        res = [0 for _ in range(n + 1)]
        res[0], res[1], res[2] = 1, 1, 2        
        for i in range(3, n + 1) :
            for j in range(i) :
                res[i] += res[j] * res[i - j - 1]
        return res[n]