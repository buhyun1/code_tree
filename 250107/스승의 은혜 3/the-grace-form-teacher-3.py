# 입력 받기
N, B = map(int, input().split())  # 학생 수와 예산
gifts = [list(map(int, input().split())) for _ in range(N)]  # 선물 가격(P)와 배송비(S)

# 전체 비용 계산
costs = []
for P, S in gifts:
    costs.append((P + S, (P // 2) + S))  # 쿠폰 X 비용, 쿠폰 O 비용

# 가능한 최대 학생 수 계산
max_students = 0

# 각 학생에 대해 쿠폰을 사용하는 경우를 시뮬레이션
for i in range(N):
    # 쿠폰을 i번째 학생에게 사용
    temp_costs = []
    for j in range(N):
        if i == j:  # 쿠폰 사용 학생
            temp_costs.append(costs[j][1])  # 쿠폰 적용 비용
        else:  # 다른 학생들
            temp_costs.append(costs[j][0])  # 일반 비용

    # 비용을 정렬
    temp_costs.sort()

    # 예산 내에서 최대 학생 수 계산
    budget = B
    students = 0
    for cost in temp_costs:
        if budget >= cost:
            budget -= cost
            students += 1
        else:
            break

    # 최대 학생 수 업데이트
    max_students = max(max_students, students)

# 결과 출력
print(max_students)
