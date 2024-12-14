A = []

def range_sum(a1,a2):
    return sum(A[a1-1:a2])

def main():
    global A
    n, m = map(int, input().split())
    A = list(map(int, input().split()))  
    
    for _ in range(m):
        a1, a2 = map(int, input().split())  # 각 쿼리 입력
        print(range_sum(a1, a2))  # 구간 합 출력

main()