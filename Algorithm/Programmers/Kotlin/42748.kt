/*

K번째수 : https://school.programmers.co.kr/learn/courses/30/lessons/42748

배열과 연산에 대한 명령어가 주어졌을 때, 연산을 적용했을 때의 결과를 구하는 문제
- 연산은 다음과 같이 이루어진다
    - 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 숫자를 구한다
- 배열 array의 길이는 1 이상 100 이하이다
    - array의 원소는 1 이상 100 이하이다
- commands는 길이는 1 이상 50 이하인 2차원 배열이다
    - commands의 각 원소는 길이가 3이며, [i, j, k] 형식으로 이루어진다

Example:
- Input : array=[1, 5, 2, 6, 3, 7, 4], commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
- Output : [5, 6, 3]

Note:
주어진 방식대로 array를 자르고 정렬 후 특정 인덱스에 있는 값을 확인
주어진 문제에서는 인덱스가 1부터 시작하는 부분에 유의

 */

class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        return commands.map { (i, j, k) ->
            array.slice(i-1 .. j-1).sorted()[k-1]
        }.toIntArray()
    }
}