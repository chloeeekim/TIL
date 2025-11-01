/*

과일 장수 : https://school.programmers.co.kr/learn/courses/30/lessons/135808

사과의 점수와 한 상자에 들어가는 사과의 개수가 주어졌을 때, 얻을 수 있는 최대 이익을 구하는 문제
- 사과는 상태에 따라 1점부터 k점까지의 점수로 분류한다
    - k점이 최상품의 사과이고, 1점이 최하품의 사과이다
- 사과 한 상자의 가격은 다음과 같이 결정된다
    - 한 상자에 사과를 m개씩 담아 포장한다
    - 상자에 담긴 사과 중 가장 낮은 점수가 p점인 경우, 사과 한 상자의 가격은 p * m이다
- 사과 장수는 가능한 한 많은 사과를 판매한다
    - 사과는 상자 단위로만 판매하며, 남는 사과는 버린다
- 사과의 최대 점수 k는 3 이상 9 이하의 정수이다
- 한 상자에 들어가는 사과의 수 m은 3 이상 10 이하이다
- 사과들의 점수 score의 길이는 7 이상 1,000,000 이하이다
    - score의 원소는 1 이상 k 이하이다
- 이익이 발생하지 않는 경우에는 0을 리턴한다

Example:
- Input : k=3, m=4, score=[1, 2, 3, 1, 2, 3, 1]
- Output : 8

- Input : k=4, m=3, score=[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
- Output : 33

Note:
사과들의 점수를 내림차순으로 정렬하여 점수가 높은 사과부터 순서대로 상자에 담는다
m개씩 들어가므로, m-1, 2m-1, ... 과 같은 인덱스의 사과 점수가 하나의 상자에 들어가는 가장 낮은 점수가 된다

 */

class Solution {
    fun solution(k: Int, m: Int, score: IntArray): Int {
        val size = score.size
        val apples = score.sortedArrayDescending()

        return (m-1 until size step m).sumOf { i ->
            apples[i] * m
        }
    }
}