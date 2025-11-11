/*

H-Index : https://school.programmers.co.kr/learn/courses/30/lessons/42747

어떤 과학자가 발표한 논문의 인용 횟수가 주어졌을 때, H-Index를 구하는 문제
- H-Index는 다음과 같이 구할 수 있다
    - 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하 인용되었다면, h의 최댓값이 H-Index가 된다
- 논문의 인용 횟수를 담은 배열 citations의 길이는 1 이상 1,000 이하이다
    - 논문별 인용 횟수는 0회 이상 10,000회 이하이다

Example:
- Input : citations=[3, 0, 6, 1, 5]
- Output : 3

Note:
내림차순으로 정렬 후, i번 이상 인용된 논문의 개수를 카운트

 */

class Solution {
    fun solution(citations: IntArray): Int {
        var answer = 0
        for ((i, curr) in citations.sortedDescending().withIndex()) {
            if (i < curr) answer++
            else break
        }
        return answer
    }
}