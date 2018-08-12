def Palindrome(x):
	ref = x
	rev = 0
	while x > 0:
		rem = (x % 10)
		rev = (rev * 10) + rem
		x //= 10
	if rev == ref: return 1
	else: return 0
n = 1580939956
pl = ph = n
while True:
	if Palindrome(pl) == 1:
		low = pl
		break
	pl -= 1
while True:
	if Palindrome(ph) == 1:
		high = ph
		break
	ph += 1
#print(high)
print(low)
#print(abs(high-low))
low_dif = abs(n - low)
high_dif = abs(n - high)
print(low_dif)
print(high_dif)

if (low_dif < high_dif): 
	print(low)
	exit()
elif (high_dif < low_dif): print(high)
else: print(low)