/*

입국심사 : https://school.programmers.co.kr/learn/courses/30/lessons/43238

입국 심사를 기다리는 사람의 수와 각 심사관이 심사하는 데 걸리는 시간이 주어졌을 때, 모든 사람들이 심사를 받는데 걸리는 시간의 최솟값을 구하는 문제
- 입국 심사는 다음과 같이 이루어진다
    - 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다르다
    - 처음에 모든 심사대는 비어 있다
    - 한 심사대에서는 동시에 한 명만 심사를 할 수 있다
    - 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수도 있지만, 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있다
- 입국심사를 기다리는 사람의 수 n은 1 이상 1,000,000,000 이하이다
- 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times의 길이는 1 이상 100,000 이하이다
    - times의 원소는 1 이상 1,000,000,000 이하이다

Example:
- Input : n=6, times=[7, 10]
- Output : 28

Note:
이분탐색 방식으로, mid 시간 동안 심사할 수 있는 사람의 수를 구한 다음,
1. 더 많은 사람을 심사할 수 있다면 시간을 줄이고(right = mid - 1)
2. 더 적은 사람을 심사할 수 있다면 시간을 늘린다(left = mid + 1)

 */

class Solution {
    fun solution(n: Int, times: IntArray): Long {
        var left = times.minOf { it }.toLong()
        var right = times.maxOf { it }.toLong() * n

        while (left <= right) {
            val mid = (left + right) / 2

            var count = 0L
            for (t in times) {
                count += mid / t
                if (count >= n) break
            }

            if (count >= n) right = mid - 1
            else left = mid + 1
        }

        return left
    }
}