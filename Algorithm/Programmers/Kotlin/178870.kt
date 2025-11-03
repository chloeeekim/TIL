/*

연속된 부분 수열의 합 : https://school.programmers.co.kr/learn/courses/30/lessons/178870

비내림차순으로 정렬된 수열이 주어질 때, 조건을 만족하는 부분 수열의 시작 인덱스와 마지막 인덱스를 구하는 문제
- 부분 수열은 다음 조건을 만족해야 한다
    - 기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열이어야 한다
    - 부분 수열의 합은 k이다
    - 합이 k인 부분 수열이 여러 개인 경우, 길이가 짧은 수열을 찾는다
    - 길이가 짧은 수열이 여러 개인 경우, 시작 인덱스가 작은 수열을 찾는다
- 수열을 나타내는 정수 배열 sequence의 길이는 5 이상 1,000,000 이하이다
    - sequence의 원소는 1 이상 1,000 이하이다
- 부분 수열의 합 k는 5 이상 1,000,000,000 이하의 정수이다
    - k는 항상 sequence의 부분 수열로 만들 수 있는 값이다

Example:
- Input : sequence=[1, 2, 3, 4, 5], k=7
- Output : [2, 3]

- Input : sequence=[1, 1, 1, 2, 3, 4, 5], k=5
- Output : [6, 6]

- Input : sequence=[2, 2, 2, 2, 2], k=6
- Output : [0, 2]

Note:
투 포인터 방식으로 해결
부분 수열의 합이 k일 경우: answer와 비교하여 길이가 짧은 것으로 업데이트하고, left를 증가시켜 다음 부분 수열을 찾는다
부분 수열의 합이 k보다 작은 경우: right를 증가시켜 합을 늘린다
부분 수열의 합이 k보다 클 경우: left를 증가시켜 합을 줄인다

 */

class Solution {
    fun solution(sequence: IntArray, k: Int): IntArray {
        val size = sequence.size
        var left = 0
        var right = 0
        var tSum = sequence[0]
        var answer = intArrayOf(0, size)

        while (right < size) {
            when {
                tSum == k -> {
                    if (right - left < answer[1] - answer[0]) {
                        answer[0] = left
                        answer[1] = right
                    }
                    tSum -= sequence[left++]
                }
                tSum < k -> {
                    if (++right < size) tSum += sequence[right]
                }
                else -> tSum -= sequence[left++]
            }
        }

        return answer
    }
}