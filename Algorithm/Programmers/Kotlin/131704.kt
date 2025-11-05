/*

택배상자 : https://school.programmers.co.kr/learn/courses/30/lessons/131704

택배 기사님이 원하는 상자 순서가 주어졌을 때, 보조 컨테이너 벨트를 사용하여 몇 개의 상자를 실을 수 있는지 구하는 문제
- 택배상자는 크기가 모두 같으며, 1번 상자부터 n번 상자까지 번호가 증가하는 순서대로 컨테이너 벨트에 일렬로 놓여 전달된다
    - 컨테이너 벨트는 한 방향으로만 진행이 가능하며, 벨트에 놓인 순서대로 (1번 상자부터) 상자를 내릴 수 있다
    - 컨테이너 벨트의 맨 앞에 놓인 상자가 현재 트럭에 실어야 하는 순서가 아니라면, 상자를 보조 컨테이너 벨트에 보관할 수 있다
- 보조 컨테이너 벨트는 맨 앞의 상자만 뺄 수 있다 (즉, 가장 마지막에 보조 컨테이너 벨트에 보관한 상자부터 꺼낼 수 있다)
- 보조 컨테이너 벨트를 이용해도 기사님이 원하는 순서대로 상자를 싣지 못하는 경우, 더 이상 상자를 싣지 않는다
- 택배 기사님이 원하는 상자 순서를 나타내는 정수 배열 order의 길이는 1 이상 1,000,000 이하이다
    - order는 1 이상 order 길이 이하의 모든 정수가 한 번씩 등장한다
    - order[i]는 기존 컨테이너 벨트에 order[i]번째 상자를 i+1번째로 트럭에 실어야 함을 의미한다

Example:
- Input : order=[4, 3, 1, 2, 5]
- Output : 2

- Input : order=[5, 4, 3, 2, 1]
- Output : 5

Note:
보조 컨테이너 벨트를 stack으로 구현
스택이 비어 있거나, 실어야 하는 상자의 번호가 현재 확인한 것보다 크다면 실어야 하는 상자가 도착할 때까지 스택에 추가
스택이 비어 있지 않고, 실어야 하는 상자의 번호가 현재 확인한 것과 같거나 작다면,
1. 컨테이너 벨트에서 추가할 수 있으면 O
2. 스택에서 추가할 수 있으면 O
3. 둘 다 안 되는 경우 원하는 순서대로 상자를 싣지 못하므로 중단

 */

class Solution {
    fun solution(order: IntArray): Int {
        val n = order.size
        val stack = ArrayDeque<Int>()

        var curr = 1
        for ((idx, num) in order.withIndex()) {
            if (stack.isEmpty() || curr < num) {
                while (curr < num) {
                    stack.addLast(curr)
                    curr++
                }
                curr++
            }
            else {
                if (curr == num) curr++
                else if (stack.last() == num) stack.removeLast()
                else return idx
            }
        }

        return n
    }
}