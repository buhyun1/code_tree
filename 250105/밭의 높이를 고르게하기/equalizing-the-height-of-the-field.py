N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!

min_cost = float('inf')

for i in range(N-T+1):
    cur_sec = arr[i:i+T]
    cost = sum(max(0, abs(H-height)) for height in cur_sec )

    min_cost = min(min_cost,cost)

print(min_cost)

