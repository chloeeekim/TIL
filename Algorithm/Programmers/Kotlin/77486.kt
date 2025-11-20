/*

다단계 칫솔 판매 : https://school.programmers.co.kr/learn/courses/30/lessons/77486

피라미드 식의 구조를 가진 조직 정보와 판매 정보가 주어졌을 때, 각 판매원이 얻은 이익금을 구하는 문제
- 모든 판매원은 칫솔의 판매에 의해 발생하는 이익에서 10%를 추천인에게 배분하고, 나머지는 자신이 가진다
- 모든 판매원은 자신이 추천하여 가입시킨 판매원에게서 발생하는 이익의 10%까지 자신의 이익이 되며, 이 또한 마찬가지의 규칙으로 자신의 추천인에게 분배된다
- 10%를 계산할 때에는 원 단위에서 절사하며, 10%를 계산한 금액이 1원 미만인 경우 이득을 분배하지 않고 자신이 모두 가진다
- 칫솔의 판매에서 발생하는 이익은 개당 100원이다
- enroll은 각 판매원의 이름을 담은 길이 1 이상 10,000 이하의 배열이다
    - enroll에 조직장(민호)의 이름은 없다
- referral은 각 판매원을 조직에 참여시킨 다른 판매원의 이름을 담은 배열로, 길이는 enroll과 같다
    - 어느 누구의 추천도 없이 조직에 참여한 사람은 추천인의 이름 대신 "-"가 기입된다
    - enroll에 등장하는 이름은 조직에 참여한 순서에 따른다
- seller는 판매량 집계 데이터의 판매원 이름을 나열한 길이 1 이상 100,000 이하의 배열이다
    - seller에는 같은 이름이 중복해서 들어있을 수 있다
- amount는 판매량 집계 데이터의 판매 수량을 나열한 배열로, 길이는 seller와 같다
    - amount의 원소는 1 이상 100 이하인 자연수이다
- 모든 조직 구성원들의 이름은 10글자 이내의 영문 알파벳 소문자로만 이루어져 있다
- 판매원에게 배분된 이익금의 총합을 입력으로 주어진 enroll에 이름이 포함된 순서에 따라 나열하여 리턴한다

Example:
- Input : enroll=["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], referral=["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], seller=["young", "john", "tod", "emily", "mary"], amount=[12, 4, 2, 5, 10]
- Output : [360, 958, 108, 0, 450, 18, 180, 1080]

- Input : enroll=["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], referral=["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], seller=["sam", "emily", "jaimie", "edward"], amount=[2, 3, 5, 4]
- Output : [0, 110, 378, 180, 270, 450, 0, 0]

Note:
map을 이용하여 이름과 인덱스를 매핑
while 문을 돌면서 추천인이 더 이상 없거나("-") 배분할 돈이 0이 되면 배분을 멈춘다

 */

class Solution {
    fun solution(enroll: Array<String>, referral: Array<String>, seller: Array<String>, amount: IntArray): IntArray {
        val names = mutableMapOf<String, Int>().apply {
            for ((index, name) in enroll.withIndex()) {
                this[name] = index
            }
        }
        val answer = IntArray(enroll.size)

        for ((s, a) in seller.zip(amount.toTypedArray())) {
            var money = a * 100
            var sell = s
            while (sell != "-" && money > 0) {
                val idx = names[sell]!!
                answer[idx] += money - money / 10
                money /= 10
                sell = referral[idx]
            }
        }

        return answer
    }
}