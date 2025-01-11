n, k = map(int, input().split())
box = list(map(int, input().split()))

min_cost = float('inf')

for a in range(min(box),max(box)-k+1):
    cost=0
    for ele in box:
        if ele < a:
            cost += a - ele
        elif ele > a +k:
            cost += ele - (a+k) 
    min_cost = min(cost, min_cost)

print(min_cost)