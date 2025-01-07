N, B = map(int, input().split())
gifts = list(list(map(int, input().split())) for _ in range(N))

p = [gift[0] for gift in gifts]
s= [gift[1] for gift in gifts]

total_costs = []
for i in range(N):
    total_cost = p[i]+s[i]
    discount = p[i]//2 +s[i]
    total_costs.append((total_cost, discount))

total_costs.sort(key=lambda x: min(x[0],x[1]))

max_students = 0
remaining_budget = B

for cost_no_coupon, cost_with_coupon in total_costs:
    # 더 저렴한 비용(쿠폰 적용 여부 포함)을 선택
    cost = min(cost_no_coupon, cost_with_coupon)
    if remaining_budget >= cost:
        remaining_budget -= cost
        max_students += 1

# 결과 출력
print(max_students)