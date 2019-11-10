"""

599. Minimum Index Sum of Two Lists : https://leetcode.com/problems/minimum-index-sum-of-two-lists/

문자열을 포함한 두 개의 list가 주어졌을 때, index의 합이 가장 작은 common element를 찾는 문제
- 답이 여러개인 경우 모두 출력하되, 순서는 중요하지 않다
- 항상 답은 존재한다
- 두 list의 범위는 [1, 1000]
- 각 list에 포함된 문자열의 길이는 [1, 30] 범위
- index는 0부터 시작한다
- 각 리스트 내에서 중복은 존재하지 않는다

Example:
- Input : ["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
- Output : ["Shogun"]
- 유일한 common element

- Input : ["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]
- Output : ["Shogun"]
- Shogun의 index sum = 1 (0 + 1) / KFC의 index sum = 3 (3 + 0) 따라서 Shogun만 답이 된다

Note:
리스트를 순회하며 겹치는 element를 찾아 index sum을 구하는 방법
index sum이 동일하다면 결과 list에 append하고, index sum이 더 작은 경우 결과 list를 갱신
idx1이 index sum보다 큰 경우, 어떠한 경우에도 답이 될 수 없으므로 break

"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res, idxsum = [], 2000
        for idx1, i in enumerate(list1) :
            if idx1 > idxsum :
                break
            if i in list2 :
                idx2 = list2.index(i)
                idx = idx1 + idx2
                if idx < idxsum :
                    res = [i]
                    idxsum = idx
                elif idx == idxsum :
                    res.append(i)
        return res