N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!

arr.sort()

max_length = float('inf')
for i in range(N):
    for j in range(i+1, N):
        remain_sum = sum(arr) - (arr[i]+arr[j])
        diff = abs(S - remain_sum)

        if diff < max_length:
            max_length = diff 

print(max_length)