n = int(input())

for i in range(n):
	x, y, a, b = map(int, input().split())
	
	b *= -1

	num = y - x
	den = a - b

	if (num % den) == 0:
		print(num // den)
	else:
		print(-1)