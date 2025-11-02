/*

없는 숫자 더하기 : https://school.programmers.co.kr/learn/courses/30/lessons/86051

0부터 9까지의 숫자 중 일부가 들어있는 정수 배열이 주어졌을 때, 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 구하는 문제
- numbers의 길이는 1 이상 9 이하이며, 모든 원소는 0 이상 9 이하의 자연수이다
    - numbers의 모든 원소는 서로 다르다

Example:
- Input : numbers=[1,2,3,4,6,7,8,0]
- Output : 14

- Input : numbers=[5,8,4,0,6,7,9]
- Output : 6

Note:
0부터 9까지의 숫자를 모두 더하면 45
주어진 숫자들 중 없는 숫자를 모두 찾아 더하는 것이므로, 45에서 존재하는 숫자의 합을 빼는 방식으로 계산

 */

class Solution {
    fun solution(numbers: IntArray): Int {
        return 45 - numbers.sum()
    }
}