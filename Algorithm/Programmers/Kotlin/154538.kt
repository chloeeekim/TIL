/*

숫자 변환하기 : https://school.programmers.co.kr/learn/courses/30/lessons/154538

특정 연산을 사용하여 자연수 x를 y로 변환하기 위해 필요한 최소 연산 횟수를 구하는 문제
- 사용할 수 있는 연산은 다음과 같다
    - x에 n을 더한다
    - x에 2를 곱한다
    - x에 3을 곱한다
- 만약 x를 y로 만들 수 없는 경우 -1을 리턴한다
- 자연수 x, y는 1 이상 1,000,000 이하이며, x는 y보다 작거나 같다
- 자연수 n은 1 이상 y 미만이다

Example:
- Input : x=10, y=40, n=5
- Output : 2
- x에 2를 2번 곱하는 경우가 최소 횟수

- Input : x=10, y=40, n=30
- Output : 1
- x에 n인 30을 1번 더하는 경우가 최소 횟수

- Input : x=2, y=5, n=4
- Output : -1

Note:
queue를 사용하여 bfs 방식으로 탐색
visited set을 두어 이미 확인한 숫자에 대해 중복 검사를 방지

 */

class Solution {
    fun solution(x: Int, y: Int, n: Int): Int {
        if (x == y) return 0

        val queue = ArrayDeque<Pair<Int, Int>>().apply { addLast(x to 0) }
        val visited = mutableSetOf<Int>().apply { add(x) }
        while (queue.isNotEmpty()) {
            val (num, count) = queue.removeFirst()

            for (nn in arrayOf(num + n, num * 3, num * 2)) {
                if (nn > y || nn in visited) continue
                if (nn == y) return count + 1

                visited.add(nn)
                queue.addLast(nn to count + 1)
            }
        }

        return -1
    }
}