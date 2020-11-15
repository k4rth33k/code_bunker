class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()[::-1]
        
        return ''.join([word+' ' for word in words]).strip()