t = int(input())
x = 0

for _ in range(t):
	op = input()
	if '+' in op:
		x += 1
	else:
		x -= 1

print(x)