class Solution:
    def __init__(self):
        self.dp = {}
        
    def util(self, i, j):
        ans = self.A[i][j]
        
        temp = []
        for op in [-1, 0, 1]:
            if 0 <= j + op < len(self.A):
                if i == len(self.A)-1:
                    temp.append(0)
                else:
                    if (i+1, j+op) in self.dp:
                        temp.append(self.dp[(i+1, j+op)])
                    else:
                        temp.append(self.util(i+1, j+op))
        
        print(ans, min(temp))
        ans = min([x+ans for x in temp])
        self.dp[(i,j)] = ans
        return ans
                
                
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        self.A = A
        ans = min([self.util(0, j) for j in range(len(self.A))])
        return ans