/*

비밀 코드 해독 : https://school.programmers.co.kr/learn/courses/30/lessons/388352

1부터 n까지 서로 다른 정수 5개가 오름차순으로 정렬된 비밀 코드가 있을 때, m번의 시도 후 비밀 코드로 가능한 정수 조합의 개수를 구하는 문제
- 각 시도마다 서로 다른 5개의 정수를 입력하면, 몇 개가 비밀 코드에 포함되어 있는지 확인 가능하다
- 비밀 코드가 존재하지 않는 경우(답이 0인 경우)는 주어지지 않는다

Example:
- Input : n=10, q=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], ans=[2, 3, 4, 3, 3]
- Output : 3
- 가능한 정수 조합은 [3, 4, 7, 9, 10], [3, 5, 7, 8, 9], [3, 5, 7, 8, 10]으로 3가지

- Input : n=15, q=	[[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], ans=[2, 1, 3, 0, 1]
- Output : 5
- 가능한 정수 조합은 [1, 2, 3, 5, 8], [1, 3, 5, 8, 12], [2, 4, 5, 8, 12], [2, 5, 8, 9, 10], [5, 8, 9, 10, 12]으로 5가지

Note:
ans가 5라면 비밀 코드와 일치하는 것이므로 가능한 정수 조합은 1가지
ans가 0이라면 비밀 코드와 일치하는 숫자가 하나도 없으므로, 해당 숫자들은 제외
가능한 모든 조합을 구성한 후 교집합을 통해 비밀 코드로 가능한지 확인

 */

class Solution {
    fun solution(n: Int, q: Array<IntArray>, ans: IntArray): Int {
        if (ans.any { it == 5 }) return 1

        val unavailable = q.indices
            .filter { ans[it] == 0 }
            .flatMap { q[it].asIterable() }
            .toSet()

        val available = (1 .. n).filterNot { it in unavailable }

        val lists = makeList(available)

        return lists.count { a ->
            q.indices.all { i ->
                checkMatchCount(a, q[i], ans[i])
            }
        }
    }

    private fun makeList(available: List<Int>): MutableList<List<Int>> {
        val lists = mutableListOf<List<Int>>()
        val size = available.size
        for (i in 0 until size - 4) {
            for (j in i+1 until size - 3) {
                for (k in j+1 until size - 2) {
                    for (l in k+1 until size - 1) {
                        for (m in l+1 until size) {
                            lists.add(listOf(available[i], available[j], available[k], available[l], available[m]))
                        }
                    }
                }
            }
        }

        return lists
    }

    private fun checkMatchCount(a: List<Int>, b: IntArray, match: Int): Boolean {
        return a.intersect(b.toList()).size == match
    }
}