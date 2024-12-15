n = map(int, input().split())
box = list(map(int, input().split()))
    
def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def lcm(a,b):
    return a*b // gcd(a,b)

def lcm_recursive(numbers, idx=0):
    if len(numbers) == 1:
        return numbers[0]
    return lcm(numbers[idx], lcm_recursive(numbers[idx + 1:]))

result = lcm_recursive(box)
print(result)