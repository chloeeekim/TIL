/*

행렬의 덧셈 : https://school.programmers.co.kr/learn/courses/30/lessons/12950

행과 열의 크기가 같은 두 행렬이 주어졌을 때, 같은 행, 같은 열의 값을 서로 더한 결과를 구하는 문제
- 행렬 arr1과 arr2의 행과 열의 길이는 500을 넘지 않는다

Example:
- Input : arr1=[[1,2],[2,3]], arr2=[[3,4],[5,6]]
- Output : [[4,6],[7,9]]

- Input : arr1=[[1],[2]], arr2=[[3],[4]]
- Output : [[4],[6]]

Note:
Array<IntArray>를 arr1과 동일한 크기로 생성하면서 두 배열의 값을 더한 값으로 초기화

 */

class Solution {
    fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
        return Array(arr1.size) { i ->
            IntArray(arr1[0].size) { j ->
                arr1[i][j] + arr2[i][j]
            }
        }
    }
}