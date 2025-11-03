/*

광물 캐기 : https://school.programmers.co.kr/learn/courses/30/lessons/172927

곡괭이들의 개수와 광물의 정보가 주어졌을 때, 작업을 끝내기까지 필요한 최소한의 피로도를 구하는 문제
- 곡괭이와 광물은 각각 다이아몬드, 철, 돌로 이루어져 있다
- 각 곡괭이로 광물을 캘 때의 피로도는 다음과 같다
    - 다이아몬드 곡괭이: 다이아몬드 1 / 철 1 / 돌 1
    - 철 곡괭이: 다이아몬드 5 / 철 1 / 돌 1
    - 돌 곡괭이: 다이아몬드 25 / 철 5 / 돌 1
- 작업을 하는 과정은 다음과 같다
    - 사용할 수 있는 곡괭이 중 아무거나 하나를 선택해 광물을 캔다
    - 한 번 사용하기 시작한 곡괭이는 사용할 수 없을 때까지 사용한다
    - 곡괭이는 종류에 상관없이 광물 5개를 캔 후에는 더 이상 사용할 수 없다
    - 광물은 주어진 순서대로만 캘 수 있다
    - 광산에 있는 모든 광물을 캐거나, 더 사용할 곡괭이가 없을 때까지 광물을 캔다
- 가지고 있는 곡괭이의 개수를 나타내는 정수 배열 picks는 [dia, iron, stone]과 같은 구조로 이루어져 있다
    - dia, iron, stone은 각각 0 이상 5 이하의 정수이다
    - dia는 다이아몬드 곡괭이의 수를, iron은 철 곡괭이의 수를, stone은 돌 곡괭이의 수를 의미한다
    - 곡괭이는 최소 1개 이상 가지고 있다
- 광물들의 순서를 나타내는 문자열 배열 minerals의 길이는 5 이상 50 이하이다
    - minerals의 원소는 "diamond", "iron", "stone"으로 이루어져 있다

Example:
- Input : picks=[1, 3, 2], minerals="diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
- Output : 12

- Input : picks=[0, 1, 1], minerals=["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
- Output : 50

Note:
광물의 개수가 곡괭이가 캘 수 있는 것보다 많은 경우에는 캘 수 있는 범위까지만 고려
광물을 순서대로 5개씩 확인하며 다이아몬드, 철, 돌의 개수를 구한 다음, 다이아몬드, 철, 돌이 많은 순서대로 정렬
광물은 최대 5개이므로, 가중치를 곱한 값을 기준으로 정렬하도록 구현하였으나,
sortedWith와 compareByDescending, thenByDescending으로 다중 정렬을 구현할 수도 있다
정렬된 광물을 피로도를 최소로 하기 위해 다이아몬드, 철, 돌 곡괭이의 순서로 사용하며 피로도 계산

 */

class Solution {
    fun solution(picks: IntArray, minerals: Array<String>): Int {
        val canPick = minOf(picks.sumOf { it } * 5, minerals.size)

        val mineralCount = mutableListOf<Triple<Int, Int, Int>>()
        for (i in 0 until canPick step(5)) {
            val slice = minerals.slice(i until minOf(i+5, canPick))
            val diamond = slice.count { it == "diamond" }
            val iron = slice.count { it == "iron" }
            mineralCount.add(Triple(diamond, iron, slice.size - diamond - iron))
        }

        val sortedCount = mineralCount.sortedByDescending { it.first * 100 + it.second * 10 + it.third }

        return sortedCount.sumOf { (d, i, s) ->
            when {
                picks[0] > 0 -> {
                    picks[0]--
                    d + i + s
                }
                picks[1] > 0 -> {
                    picks[1]--
                    d * 5 + i + s
                }
                else -> {
                    picks[2]--
                    d * 25 + i * 5 + s
                }
            }
        }
    }
}