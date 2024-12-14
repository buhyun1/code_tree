
def cre_sol(current, n):
    while current <= n:
        print("* " * current)
        current += 1

def des_sol(n):
    while n > 0:
        print("* " * n)
        n -= 1

# 메인 로직
def main():
    n = int(input())  # 사용자로부터 정수 입력 받기
    des_sol(n)  # 별 감소 출력
    cre_sol(1, n)  # 별 증가 출력

# 프로그램 실행
main()