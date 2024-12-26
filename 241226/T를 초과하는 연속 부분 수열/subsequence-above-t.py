n, t = map(int, input().split())
box = list(map(int,input().split()))

cnt = 0
max_length = 0

for i in box:
    if i > t :
        cnt += 1
        max_length = max(cnt, max_length)
    else:
        cnt = 0

print(max_length)