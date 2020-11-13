class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        new = []
        for idx, row in enumerate(A):
            A[idx] = [1-x for x in row[::-1]]
        
        return A