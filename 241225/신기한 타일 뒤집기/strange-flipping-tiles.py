li=[0]*10000
now = 5000
white, black = 0, 0
n=int(input())

for i in range(n):
    x, direction = input().split()
    x=int(x)
    if direction=='L':
        for j in range(now, now-x+1, -1):
            li[j]=1
        now-=x-1
        li[now]=1
    else:
        for j in range(now, now+x-1):
            li[j]=-1
        now+=x-1
        li[now]=-1
for i in range(10000):
    if li[i]==-1:
        black+=1
    elif li[i]==1:
        white+=1

print(white, black) 