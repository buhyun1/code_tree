N = int(input())

class man:
    def __init__ (self, h,w,i):
        self.h = h
        self.w = w
        self.i = i

men = []
for i in range(N):
    h,w = map(int, input().split())
    men.append(man(h,w,i+1))

men.sort(key = lambda x: (x.h, -x.w))

for man in men:
    print(man.h, man.w, man.i)