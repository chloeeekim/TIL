/*

다리를 지나는 트럭 : https://school.programmers.co.kr/learn/courses/30/lessons/42583

다리의 정보와 트럭별 무게가 주어졌을 때, 모든 트럭이 다리를 건너는 데 필요한 최소 시간을 구하는 문제
- 트럭은 정해진 순서대로 다리를 건넌다
- 다리에 올라갈 수 있는 트럭 수 bridge_length는 1 이상 10,000 이하이다
- 다리가 견딜 수 있는 무게 weight는 1 이상 10,000 이하이다
- 트럭별 무게 truck_weights의 길이는 1 이상 10,000 이하이다
    - 모든 트럭의 무게는 1 이상 weight 이하이다

Example:
- Input : bridge_length=2, weight=10, truck_weights=[7, 4, 5, 6]
- Output : 8

- Input : bridge_length=100, weight=100, truck_weights=[10]
- Output : 101

- Input : bridge_length=100, weight=100, truck_weights=[10,10,10,10,10,10,10,10,10,10]
- Output : 110

Note:
ArrayDeque를 사용하여 queue를 구현하여 현재 다리 위를 지나고 있는 트럭 정보를 저장
시간(answer)를 증가시키면서 다리의 끝에 도달한 경우 queue에서 제거하고, 더 건널 수 있는 경우 queue에 추가

 */

class Solution {
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
        var answer = 0
        val queue = ArrayDeque<Pair<Int, Int>>().apply { addLast(truck_weights[0] to 1) }
        var idx = 1
        var currSum = truck_weights[0]
        val trucks = truck_weights.size

        while (queue.isNotEmpty()) {
            answer++
            if (queue[0].second + bridge_length <= answer) {
                val (w, i) = queue.removeFirst()
                currSum -= w
            }

            if (idx < trucks && currSum + truck_weights[idx] <= weight) {
                queue.addLast(truck_weights[idx] to answer)
                currSum += truck_weights[idx]
                idx++
            }
        }

        return answer
    }
}