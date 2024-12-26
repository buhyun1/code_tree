N, M = map(int, input().split())
A_moves = [tuple(map(int, input().split())) for _ in range(N)]
B_moves = [tuple(map(int, input().split())) for _ in range(M)]

def dd(N, M, A_moves, B_moves):
    total_time = sum(t for _, t in A_moves)
    A_positions = [0] * (total_time + 1)
    B_positions = [0] * (total_time + 1)

    time = 0
    for v, t in A_moves:
        for _ in range(t): 
            time += 1
            A_positions[time] = A_positions[time - 1] + v

    time = 0
    for v, t in B_moves:
        for _ in range(t):  
            time += 1
            B_positions[time] = B_positions[time - 1] + v

    cnt = 0
    leader = None

    for t in range(1, total_time + 1):
        if A_positions[t] > B_positions[t]:
            current_leader = "A"
        elif A_positions[t] < B_positions[t]:
            current_leader = "B"
        else:
            current_leader = "Tied"

        if current_leader != leader:
            cnt += 1
            leader = current_leader

    return cnt

print(dd(N, M, A_moves, B_moves))
