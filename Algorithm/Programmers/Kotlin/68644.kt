/*

두 개 뽑아서 더하기 : https://school.programmers.co.kr/learn/courses/30/lessons/68644

정수 배열이 주어졌을 때, 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 구하는 문제
- 가능한 모든 수를 배열에 오름차순으로 담아 리턴한다
- numbers의 길이는 2 이상 100 이하이며, numbers의 모든 원소는 0 이상 100 이하이다

Example:
- Input : numbers=[2,1,3,4,1]
- Output : [2,3,4,5,6,7]

- Input : numbers=[5,0,2,7]
- Output : [2,5,7,9,12]

Note:
가능한 수가 중복되는 경우가 있을 수 있으므로 set을 사용하여 중복 제거
buildSet을 사용하여 set을 만들고, 정렬 후 IntArray 타입으로 변환

 */

class Solution {
    fun solution(numbers: IntArray): IntArray {
        return buildSet {
            for (i in 0 until numbers.size - 1) {
                for (j in i + 1 until numbers.size) {
                    add(numbers[i] + numbers[j])
                }
            }
        }.sorted().toIntArray()
    }
}