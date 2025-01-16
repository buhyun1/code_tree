n = int(input())
box = [list(map(int, input().split())) for _ in range(n)]

def is_intersecting_after_removal(n, box):
    for k in range(n):  # k번째 선분을 제거
        left, right = -1, 101  # 초기값: 최대 범위를 설정
        for i in range(n):
            if i == k:  # k번째 선분은 제외
                continue
            # 나머지 선분들의 겹치는 구간 갱신
            left = max(left, box[i][0])  # 최댓값으로 겹치는 왼쪽 구간 갱신
            right = min(right, box[i][1])  # 최솟값으로 겹치는 오른쪽 구간 갱신
        if left <= right:  # 공통 구간이 존재
            return "Yes"
    return "No"

print(is_intersecting_after_removal(n, box))
