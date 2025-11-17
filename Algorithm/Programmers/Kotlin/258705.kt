/*

산 모양 타일링 : https://school.programmers.co.kr/learn/courses/30/lessons/258705

한 변의 길이가 1인 정삼각형 2n+1개를 이어 붙여 만든 사다리꼴 위에 정삼각형을 붙인 형태의 모양이 주어졌을 때, 정삼각형 또는 마름모 타일로 빈 곳이 없도록 채우는 경우의 수를 구하는 문제
- 정삼각형 2n+1개를 이어 붙여 만든 사다리꼴의 윗변의 길이는 n, 아랫변의 길이는 n+1이다
- 사다리꼴의 윗변과 변을 공유하는 n개의 정삼각형 중 일부의 위쪽에 같은 크기의 정삼각형을 붙이는 형태로 구성된다
- 모양을 채우는 정삼각형 또는 마름모(정삼각형 2개를 이어 붙인 형태) 타일은 돌려서 사용할 수 있다
- 타일을 놓을 때 다른 타일과 겹치거나 모양을 벗어나게 놓을 수는 없다
- 구해진 경우의 수는 10007로 나눈 나머지를 리턴한다
- n은 1 이상 100,000 이하의 정수이다
- tops의 길이는 n이며, tops[i]는 사다리꼴의 윗변과 변을 공유하는 i+1번째 정삼각형의 위쪽에 정삼각형을 붙이는 경우 1, 붙이지 않는 경우는 0이다

Example:
- Input : n=4, tops=[1, 1, 0, 1]
- Output : 149

- Input : n=2, tops=[0, 1]
- Output : 11

- Input : n=10, tops=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- Output : 7704

Note:
dp로 해결
n이 1인 경우, top이 존재한다면 채울 수 있는 경우의 수는 4개, top이 존재하지 않는다면 경우의 수는 3개이다
n이 늘어나면, 다음 사다리꼴과 겹치는 부분이 존재하게 되는데, 이전 사다리꼴의 오른쪽 삼각형이 마름모에 포함되는 경우 다음 사다리꼴을 채우는 경우의 수에 영향을 끼친다
type_a 리스트는 사다리꼴의 오른쪽 삼각형이 마름모에 포함되는 경우, type_b 리스트는 사다리꼴의 오른쪽 삼각형이 마름모에 포함되지 않는 경우로 구분하여 계산

 */

class Solution {
    fun solution(n: Int, tops: IntArray): Int {
        val MOD = 10007
        val type_a = IntArray(n)
        val type_b = IntArray(n)

        type_a[0] = 1
        type_b[0] = if (tops[0] == 1) 3 else 2

        for (i in 1 until n) {
            type_a[i] = (type_a[i-1] + type_b[i-1]) % MOD

            if (tops[i] == 1) {
                type_b[i] = (type_a[i-1] * 2 + type_b[i-1] * 3) % MOD
            }
            else {
                type_b[i] = (type_a[i-1] + type_b[i-1] * 2) % MOD
            }
        }

        return (type_a[n-1] + type_b[n-1]) % MOD
    }
}