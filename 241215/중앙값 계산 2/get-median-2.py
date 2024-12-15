n = map(int, input().split())
box = list(map(int, input().split()))

box_list =[]

for i in range(1, len(box)+1,2):
    a = sorted(box[:i])
    median = a[len(a)//2]
    box_list.append(str(median))

print(' '.join(box_list))
