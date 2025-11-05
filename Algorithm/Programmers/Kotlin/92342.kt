/*

양궁대회 : https://school.programmers.co.kr/learn/courses/30/lessons/92342

어피치가 맞힌 과녁 점수의 개수가 주어졌을 때, 라이언이 가장 큰 점수 차이로 우승하기 위한 과녁 점수의 개수를 구하는 문제
- 어피치가 화살 n발을 다 쏜 후에 라이언이 화살 n발을 쏜다
- 만약 k점을 어피치가 a발을 맞혔고 라이언이 b발을 맞혔을 경우, 더 많은 화살을 k점에 맞힌 선수가 k점을 가져간다
- 만약 a = b일 경우 어피치가 k점을 가져간다
- 만약 최종 점수가 같을 경우 어피치를 우승자로 결정한다
- 라이언이 우승할 수 없는 경우 [-1]을 리턴한다
- info의 i번째 원소는 과녁의 10-i점을 맞힌 화살의 개수이다 (i는 0 이상 10 이하의 정수이다)
- 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 리턴한다

Example:
- Input : n=5, info=[2,1,1,1,0,0,0,0,0,0,0]
- Output : [0,2,2,0,1,0,0,0,0,0,0]

- Input : n=1, info=[1,0,0,0,0,0,0,0,0,0,0]
- Output : [-1]

- Input : n=9, info=[0,0,1,2,0,1,1,1,1,1,1]
- Output : [1,1,2,0,1,2,2,0,0,0,0]

- Input : n=10, info=[0,0,0,0,0,0,0,0,3,4,3]
- Output : [1,1,1,1,1,1,1,1,0,0,2]

Note:
bfs 방식으로 해결
k점을 얻기 위해서는 어피치보다 1발 더 많이 맞히면 된다
우승 방법이 여러 가지일 경우, 가장 낮은 점수를 더 많이 맞힌 경우가 답이므로, 0점에 다 맞힌다
낮은 점수부터 계산하여 점수 차가 동일할 때 낮은 점수를 더 많이 맞힌다는 비교 조건을 항상 만족하도록 구현

 */

class Solution {
    data class Shoot(val score: IntArray, val remain: Int, val nextIdx: Int)

    fun solution(n: Int, info: IntArray): IntArray {
        val size = 11
        val queue = ArrayDeque<Shoot>().apply { addLast(Shoot(IntArray(size), n, size - 2)) }

        var answer = intArrayOf()
        var maxDiff = 0
        while (queue.isNotEmpty()) {
            val (score, remain, nextIdx) = queue.removeFirst()

            if (remain == 0 || nextIdx == -1) {
                score[size - 1] += remain
                val gap = calcScoreGap(info, score)
                if (gap >= maxDiff) {
                    maxDiff = gap
                    answer = score.copyOf()
                }
                continue
            }

            val aScore = info[nextIdx]

            queue.add(Shoot(score.copyOf(), remain, nextIdx - 1))
            if (aScore + 1 <= remain) {
                score[nextIdx] = aScore + 1
                queue.addLast(Shoot(score.copyOf(), remain - aScore - 1, nextIdx - 1))
            }
        }

        return if (maxDiff != 0) answer else intArrayOf(-1)
    }

    private fun calcScoreGap(apeach: IntArray, ryan: IntArray): Int {
        var aScore = 0
        var rScore = 0

        for (i in apeach.indices) {
            if (apeach[i] >= ryan[i] && apeach[i] != 0) aScore += 10 - i
            else if (apeach[i] < ryan[i]) rScore += 10 - i
        }

        return rScore - aScore
    }
}