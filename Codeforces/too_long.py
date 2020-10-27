n = int(input())

for _ in range(n):
	s = input()
	l = len(s)
	if l > 10:
		print(f'{s[0]}{l-2}{s[-1]}')
	else:
		print(s)