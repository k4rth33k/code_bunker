t = int(input())

def flip(str_, k):
	return ''.join([str(int(_ == '0')) for _ in str_[:k]]) + str_[k:]

for _ in range(t):
	l = int(input())
	x = input()
	y = input()

	count = 0
	ops = []
	
	while (x != y):
		_ = None
		for i in range(l-1, -1, -1):
			if x[i] != y[i]:
				_ = i
				break
		
		x = flip(x, _+1)
		count += 1
		ops.append(_+1)

	print(count, ''.join([str(_) + ' ' for _ in ops]).strip(), end='\n')
