N, T = map(int, input().split())
commands =  list(input())
grid = [list(map(int,input().split())) for i in range(N)]

cur_pos = (N//2, N//2)
directions = ['N', 'E', 'S', 'W']
cur_dir = 0

deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

total_sum = grid[cur_pos[0]][cur_pos[1]]


for cmd in commands:
    if cmd == 'R':
        cur_dir = (cur_dir +1) %4
    elif cmd == 'L':
        cur_dir = (cur_dir -1) %4
    elif cmd == 'F':
        new_pos = (cur_pos[0] + deltas[cur_dir][0], cur_pos[1] + deltas[cur_dir][1])
        if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:
            cur_pos = new_pos
            total_sum += grid[cur_pos[0]][cur_pos[1]]

print(total_sum)