n = int(input())
box = [list(map(int, input().split())) for _ in range(n)]

check = set()

# 각 선분의 범위를 집합에 추가
for i, v in box:
    for j in range(i, v + 1):
        check.add(j)

# 1부터 n까지 모든 값이 포함되어 있는지 확인
if set(range(1, n + 1)) <= check:  # 부분집합 관계 확인
    print("Yes")
else:
    print("No")
