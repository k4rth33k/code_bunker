# # notes = [1,2,5,10,20,50,100,200,500,2000]
# notes = [186,419,83,408]
# notes.sort()

# total = 6249
# # total *= 100
# print(notes)
# i = len(notes) - 1
# # ans = ""
# ans = 0


# while total > 0:
# 	if (i < 0):
# 		print(-1)
# 		break
# 	r = total % notes[i]
# 	q = total / notes[i]
# 	# print(notes[i])

# 	if (q >= 1): #and ((int(q) * 1.0) == q):
# 		# print("enteresd")
# 		# ans += (str(notes[i]) + ' ') * int(q)
# 		print('{} x {} = {}'.format(notes[i], int(q), notes[i] * int(q)))
# 		ans += int(q)

# 		total = r

# 	# if i == 0 and total > 0:
# 	# 	print(-1)
# 	# 	break
# 	i -= 1

# print(ans)


def coinChange(coins, amount):
	dp = [float('inf')] * (amount + 1)
	dp[0] = 0

	for coin in coins:
		print('Changing values of {} to {}'.format(coin, amount+1))
		for x in range(coin, amount + 1):
			dp[x] = min(dp[x], dp[x - coin] + 1)
			# print(dp)
	return dp[amount] if dp[amount] != float('inf') else -1 

print(coinChange([186,419,83,408], 6249))