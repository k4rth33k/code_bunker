def watermelon(w):
	if not w & 1 and w > 2:
		return 'YES'
	else:
		return 'NO'

w = int(input())
print(watermelon(w))