
a = input().lower()
b = input().lower()

x = [a, b]
x.sort()

if a == b:
	print(0)
else:
	if x[0] == a:
		print(-1)
	else:
		print(1)

