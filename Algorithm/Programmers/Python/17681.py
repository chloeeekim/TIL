"""

1차 / 비밀지도 : https://school.programmers.co.kr/learn/courses/30/lessons/17681

정수 배열 두 개가 주어졌을 때, 이진수로 변환 후 겹쳐서 얻을 수 있는 전체 비밀 지도를 구하는 문제
- 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 공백(" ") 또는 벽("#")으로 이루어져 있다
- 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 잇으며, 지도 1 또는 지도 2 중 어느 하나라도 벽인 곳은 벽이고, 모두 공백인 곳은 공백이다
- 지도 1과 지도 2는 각각 정수 배열로 암호화되어 있다
- 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다
- 정수 배열의 각 원소를 이진수로 변환했을 때의 길이는 n 이하이다

Example:
- Input : n=5, arr1=[9, 20, 28, 18, 11], arr2=[30, 1, 21, 17, 28]
- Output : ["#####","# # #", "### #", "# ##", "#####"]

- Input : n=6, arr1=[46, 33, 33 ,22, 31, 50], arr2=[27 ,56, 19, 14, 14, 10]
- Output : ["######", "### #", "## ##", " #### ", " #####", "### # "]

Note:
arr1과 arr2의 각 원소를 이진수로 변환 후, zfill을 사용하여 길이 n이 되도록 0으로 패딩
공백인지 벽인지의 여부는 or 연산을 통해 확인

"""

def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        temp1 = bin(arr1[i])[2:].zfill(n)
        temp2 = bin(arr2[i])[2:].zfill(n)
        res = "".join(str(int(x) | int(y)) for x, y in zip(temp1, temp2))
        result.append("".join("#" if ch == "1" else " " for ch in res))
    return result