from itertools import permutations

def minimize_skill_gap(skills):
    min_difference = float('inf')  # 최소 차이 초기화
    
    # 순열을 사용해 5명의 능력치를 모든 가능한 순서로 나열
    for perm in permutations(skills):
        # 팀 나누기: 2명, 2명, 1명
        team1 = perm[0] + perm[1]  # 첫 번째 팀: 2명
        team2 = perm[2] + perm[3]  # 두 번째 팀: 2명
        team3 = perm[4]            # 세 번째 팀: 1명
        
        # 각 팀의 능력치 중 최대값과 최소값의 차이 계산
        max_team = max(team1, team2, team3)
        min_team = min(team1, team2, team3)
        difference = max_team - min_team
        
        # 모든 팀의 능력치가 서로 다를 경우에만 최소 차이 업데이트
        if len(set([team1, team2, team3])) == 3:
            min_difference = min(min_difference, difference)
    
    # 가능한 최소 차이를 반환, 불가능하면 -1 반환
    return min_difference if min_difference != float('inf') else -1

# 입력 받기
skills = list(map(int, input().split()))
result = minimize_skill_gap(skills)
print(result)
