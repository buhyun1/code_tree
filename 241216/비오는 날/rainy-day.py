n = int(input())

box = []
for i in range(n):
    date, hol, wea = map(str, input().split())
    if wea == 'Rain':
        box.append((date, hol, wea))

box.sort()
print(' '.join(box[0]))