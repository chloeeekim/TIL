/*

롤케이크 자르기 : https://school.programmers.co.kr/learn/courses/30/lessons/132265

롤케이크에 올라간 토핑 정보가 주어졌을 때, 동일한 가짓수의 토핑이 올라가도록 이등분하는 방법의 수를 구하는 문제
- 공평하게 잘린 롤케이크는 각 조각에 동일한 가짓수의 토핑이 올라간 경우이다
    - 잘린 롤케이크 조각의 크기나 올려진 토핑의 개수는 상관 없다
- 롤케이크에 올려진 토핑들의 번호를 저장한 정수 배열 topping의 길이는 1 이상 1,000,000 이하이다
    - topping의 원소는 1 이상 10,000 이하의 정수이다

Example:
- Input : topping=[1, 2, 1, 3, 1, 4, 1, 2]
- Output : 2
- [1, 2, 1, 3], [1, 4, 1, 2]로 자르거나, [1, 2, 1, 3, 1], [4, 1, 2]로 자르는 경우 두 가지가 있다

- Input : topping=[1, 2, 3, 1, 4]
- Output : 0

Note:
left, right 배열의 i번째 index에 토핑 i의 개수를 저장
오른쪽 조각에 모든 토핑이 다 올라가 있는 상태로 시작하여 왼쪽으로 토핑을 하나씩 옮겨가며 공평한지 확인
왼쪽 조각의 토핑의 종류가 오른쪽 조각의 토핑의 종류보다 많아지는 경우, 더 이상 공평하게 자를 수 없다

 */

class Solution {
    fun solution(topping: IntArray): Int {
        val maxTopping = topping.maxOrNull() ?: 0
        val left = IntArray(maxTopping + 1)
        val right = IntArray(maxTopping + 1)

        var leftKinds = 0
        var rightKinds = 0

        for (t in topping) {
            if (right[t]++ == 0) rightKinds++
        }

        var answer = 0
        for (t in topping) {
            if (left[t]++ == 0) leftKinds++
            if (--right[t] == 0) rightKinds--
            if (leftKinds == rightKinds) answer++
            else if (leftKinds > rightKinds) break
        }

        return answer
    }
}