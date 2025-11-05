/*

교점에 별 만들기 : https://school.programmers.co.kr/learn/courses/30/lessons/87377

Ax + By + C = 0으로 표현할 수 있는 n개의 직선이 주어질 때, 직선의 교점 중 정수 좌표에 별을 그리는 문제
- 별이 그려진 부분은 '*', 빈 공간(격자선이 교차하는 지점)은 '.'으로 표현한다
- 모든 별을 포함하는 최소한의 사각형으로 나타낸다
- line의 행 길이는 2 이상 1,000 이하인 자연수이다
    - line의 원소는 [A, B, C]의 형태이다
    - A, B, C는 -100,000 이상 100,000 이하인 정수이다
    - 무수히 많은 교점이 생기는 직선 쌍은 주어지지 않는다
    - A = 0 이면서 B = 0 인 경우는 주어지지 않는다
- 정답은 1,000 * 1,000 크기 이내에서 표현된다
- 별이 한 개 이상 그려지는 입력만 주어진다
- 참고) Ax + By + E = 0과 Cx + Dy + F = 0 이라는 두 직선의 교점이 유일하게 존재할 경우, 그 교점은 다음과 같다
    - x = (BF - ED) / (AD - BC)
    - y = (EC - AF) / (AD - BC)
    - 또, AD - BC = 0인 경우, 두 직선은 평행 또는 일치한다

Example:
- Input : price=3, money=20, count=4
- Output : 10

Note:
참고 사항에 따라 직선들이 교차하는 지점을 구하고, 정수 좌표인 경우에만 pointSet에 추가 (중복 제거용)
최소 사각형을 그려야 하므로, 주어진 points들의 x, y 좌표의 min, max를 범위로 한다
Int 타입으로만 계산했을 때는 실패하는 테스트 케이스가 있어 Long 타입으로 변환하여 계산
x, y 좌표를 구하는 과정에서 부동소수점 연산 오차가 발생할 수 있어 Double 연산 대신 % 연산으로 정수인지 확인

 */

class Solution {
    fun solution(line: Array<IntArray>): Array<String> {
        val pointSet = mutableSetOf<Pair<Long, Long>>()
        val size = line.size
        val longLine = line.map { row -> row.map { it.toLong() } }

        var (xMin, xMax) = Pair(Long.MAX_VALUE, Long.MIN_VALUE)
        var (yMin, yMax) = Pair(Long.MAX_VALUE, Long.MIN_VALUE)
        for (i in 0 until size-1) {
            for (j in i+1 until size) {
                val (a, b, e) = longLine[i]
                val (c, d, f) = longLine[j]

                if (a*d - b*c == 0L) continue

                val divisor = a*d - b*c

                val xUp = b*f - e*d
                val yUp = e*c - a*f

                if (xUp % divisor != 0L || yUp % divisor != 0L) continue

                val x = xUp / divisor
                val y = yUp / divisor
                pointSet.add(x to y)

                if (x < xMin) xMin = x
                if (x > xMax) xMax = x
                if (y < yMin) yMin = y
                if (y > yMax) yMax = y
            }
        }

        val xDiff = (xMax - xMin + 1).toInt()
        val yDiff = (yMax - yMin + 1).toInt()
        val answer = Array(yDiff) { CharArray(xDiff) { '.' } }

        for ((x, y) in pointSet) {
            answer[(yMax - y).toInt()][(x - xMin).toInt()] = '*'
        }

        return answer.map { String(it) }.toTypedArray()
    }
}