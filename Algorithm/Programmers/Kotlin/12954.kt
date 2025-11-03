/*

x만큼 간격이 있는 n개의 숫자 : https://school.programmers.co.kr/learn/courses/30/lessons/12954

정수 x와 자연수 n이 주어졌을 때, x부터 시작하여 x씩 증가하는 숫자를 n개 지니는 리스트를 구하는 문제
- x는 -10,000,000 이상 10,000,000 이하인 정수이다
- n은 1,000 이하인 자연수이다

Example:
- Input : x=2, n=5
- Output : [2,4,6,8,10]

- Input : x=4, n=3
- Output : [4,8,12]

- Input : x=-4, n=2
- Output : [-4, -8]

Note:
길이 n인 LongArray를 생성하면서 x * (i+1)로 초기화

 */

class Solution {
    fun solution(x: Int, n: Int): LongArray {
        return LongArray(n) { i -> x.toLong() * (i+1) }
    }
}