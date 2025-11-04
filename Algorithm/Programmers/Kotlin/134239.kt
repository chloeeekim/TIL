/*

우박수열 정적분 : https://school.programmers.co.kr/learn/courses/30/lessons/134239

우박수의 초항 k와 정적분을 구하는 구간들의 목록이 주어졌을 때, 정적분의 결과 목록을 구하는 문제
- 우박수열을 구하는 방법은 다음과 같다
    - 1-1. 입력된 수가 짝수라면 2로 나눈다
    - 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다
    - 2. 결과로 나온 수가 1보다 크다면 1번 작업을 반복한다
- 초항이 k인 우박수열이 있다면, x = 0일 때 y = k이고, 다음 우박수는 x = 1에 표시한다
    - 우박수가 1이 될 때까지 점을 찍고, 인접한 점들끼리 직선으로 연결하여 꺾은선 그래프를 만들 수 있다
- x에 대한 범위 [a, b]의 정적분 결과는 꺾은선 그래프와 x = a, x = b, y = 0으로 둘러 쌓인 공간의 면적과 같다
- 0 이상의 수 b에 대해 [a, -b]에 대한 정적분 결과는 x = a, x = n - b, y = 0으로 둘러 싸인 공간의 면적과 같다
    - 이때 n은 k가 초항인 우박수열이 1이 될 때까지의 횟수를 의미한다
- 우박수의 초항 k는 2 이상 10,000 이하의 정수이다
- 정적분을 구하는 구간들의 목록 ranges의 길이는 1 이상 10,000 이하이다
    - ranges의 원소는 [a, b] 형식이며, 0 <= a < 200, -200 < b <= 0을 만족한다
- 주어진 모든 입력에 대해 정적분의 결과는 2^27을 넘지 않는다
- 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간이 주어지는 경우, 정적분의 결과는 -1로 정의한다

Example:
- Input : k=5, ranges=[[0,0],[0,-1],[2,-3],[3,-3]]
- Output : [33.0,31.5,0.0,-1.0]
- 5로 시작하는 우박수열은 5 -> 16 -> 8 -> 4 -> 2 -> 1이다

- Input : k=3, ranges=[[0,0], [1,-2], [3,-3]]
- Output : [47.0,36.0,12.0]
- 3으로 시작하는 우박수열은 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1이다

Note:
getSequenceSum 함수를 통해 k로 시작하는 우박수열의 정적분 결과의 누적값을 구한다
즉, sums[b]는 x = 0부터 x = b까지의 정적분 결과이므로,
[a, b] 구간의 정적분은 sums[b] - sums[a]가 된다

 */

class Solution {
    fun solution(k: Int, ranges: Array<IntArray>): DoubleArray {
        val sums = getSequenceSum(k)
        val n = sums.size - 1

        val answer = DoubleArray(ranges.size)
        for ((idx, range) in ranges.withIndex()) {
            if (range[0] > n + range[1]) {
                answer[idx] = -1.0
                continue
            }

            val left = sums[range[0]]
            val right = sums[n + range[1]]
            answer[idx] = right - left
        }

        return answer
    }

    private fun getSequenceSum(k: Int): List<Double> {
        var before = k
        var num = k
        var beforeSum = 0.0
        return buildList {
            add(beforeSum)
            while (num > 1) {
                when {
                    num % 2 == 0 -> num /= 2
                    else -> num = num * 3 + 1
                }
                val temp = (before.toDouble() + num) / 2.0

                add(beforeSum + temp)
                before = num
                beforeSum += temp
            }
        }
    }
}