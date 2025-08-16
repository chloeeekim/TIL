"""

1차 / 캐시 : https://school.programmers.co.kr/learn/courses/30/lessons/17680

캐시 크기와 도시이름 배열이 주어졌을 때, 총 실행시간을 구하는 문제
- cacheSize는 정수이며, 0 이상 30 이하이다
- cities는 도시 이름으로 이루어진 문자열 배열로, 최대 도시 수는 100,000개이다
- 각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다
- 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다
- cache hit일 경우 실행시간은 1이다
- cache miss일 경우 실행시간은 5이다

Example:
- Input : cacheSize=3, cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
- Output : 50

- Input : cacheSize=3, cities=["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
- Output : 21

- Input : cacheSize=2, cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
- Output : 60

- Input : cacheSize=5, cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
- Output : 52

- Input : cacheSize=2, cities=["Jeju", "Pangyo", "NewYork", "newyork"]
- Output : 16

- Input : cacheSize=0, cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
- Output : 25

Note:
collections의 deque에 maxlen을 설정하여 LRU 캐시 구현
cache hit일 경우, cache에서 해당 아이템 제거 후 다시 삽입
cahce miss일 경우, cache에 해당 아이템 삽입

"""

from collections import deque

def solution(cacheSize, cities):
    cache, total = deque(maxlen=cacheSize), 0
    for city in cities:
        city = city.lower()
        if city in cache:
            total += 1
            cache.remove(city)
            cache.append(city)
        else:
            total += 5
            cache.append(city)
    return total