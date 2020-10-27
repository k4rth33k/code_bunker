n, k = [int(_) for _ in input().split()]
scores = [int(_) for _ in input().split()]

count = 0
for score in scores:
	if score >= scores[k - 1] and score > 0:
		count += 1

print(count)