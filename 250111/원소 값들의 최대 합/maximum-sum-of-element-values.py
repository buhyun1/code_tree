n, m = map(int, input().split())
box = list(map(int, input().split()))

max_total = 0

for start_pos in range(n):
    cur_pos = start_pos
    total = 0

    for _ in range(m):
        total += box[cur_pos]
        next_pos = box[cur_pos]-1

        if next_pos <0 and next_pos >= n:
            break
        
        cur_pos = next_pos

    max_total = max(max_total, total)
print(max_total)

