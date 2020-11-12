class Solution:
    def __init__(self):
        self.table = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
    
    def intToRoman(self, num: int) -> str:
        val = num
        ans= ''
        while val > 0:
            
            close = 0
            for key in self.table:
                if key > val:
                    break
                else:
                    close = key
            
            val -= close
            ans += self.table[close]
        
        return ans
