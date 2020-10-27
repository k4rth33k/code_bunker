import math

def print_(c):
	return str(c) + '\n'
	
def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))
    
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    c = int(math.log(n, 2))
    c = 1 << c
    ans.append(fibonacci(c - 1) % 10)


print(''.join(map(print_, ans)))
