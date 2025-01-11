n, m = map(int, input().split())
box = list(map(int, input().split()))

cur_pos = 0
total = 0

for _ in range(m):
    total += box[cur_pos]
    next_pos = box[cur_pos]-1

    if next_pos <0 and next_pos >= n:
        break
    
    cur_pos = next_pos

print(total)

