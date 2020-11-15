class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans = 0
        
        while piles:
            piles.pop(0)
            ans += piles.pop(0)
            piles.pop()
        
        return ans