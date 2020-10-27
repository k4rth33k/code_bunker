  
def lcs(X, Y, m, n): 
    sub = []
    L = [[0] * (n + 2) for i in
                    range(m + 2)] 
      
    for i in range(m + 1): 
        for j in range(n + 1): 
            if (i == 0 or j == 0): 
                L[i][j] = 0

            elif (X[i - 1] == Y[j - 1]) : 
                L[i][j] = L[i - 1][j - 1] + 1
                sub.append(X[i - 1])

            else:
                L[i][j] = max(L[i - 1][j], 
                                 L[i][j - 1]) 
              
    return L[m][n], sub


t = int(input())

for _ in range(t):
    n, m = [x for x in map(int, input().split())]
    a = [x for x in map(int, input().split())]
    b = [x for x in map(int, input().split())]
    len_, ans = lcs(a, b, n, m)

    if len_ == 0:
        print('NO')
    elif m == n and len_ == m:
        print('YES')
        print(1, ans[0])
    else:
        print('YES')
        print(len_, ''.join([str(_) + ' ' for _ in ans]).strip())


