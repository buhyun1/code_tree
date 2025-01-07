X, Y = map(int, input().split())
cnt = 0
def check(a):
    a = list(str(a))
    while len(a)>1:
        if a[0] == a[-1]:
            a.pop(0)
            a.pop(-1)
        else:
            return False
    return True


for i in range(X,Y+1):
   if check(i):
        cnt+= 1

print(cnt)