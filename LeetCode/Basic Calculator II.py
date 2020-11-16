class Solution:
    def calculate(self, s: str) -> int:
        self.lookup = {
            '+': (1, lambda x, y: x+y),
            '-': (1, lambda x, y: x-y),
            '*': (2, lambda x, y: x*y),
            '/': (2, lambda x, y: x//y)
        }
        opr_st = []
        opd_st = []
        buffer = ''
        
        tokens = self.split(s)
        for ch in s:
            if ch in self.lookup:
                opd_st.append(int(buffer))
                buffer = ''
                if not opr_st or self.lookup[ch][0] > self.lookup[opr_st[-1]][0]:
                    opr_st.append(ch)
                else:
                    while opr_st and self.lookup[ch][0] <= self.lookup[opr_st[-1]][0]:
                        y = opd_st.pop()
                        x = opd_st.pop()
                        opd_st.append(self.lookup[opr_st.pop()][1](x, y))
                    opr_st.append(ch)
            
            else:
                buffer += ch
                
        opd_st.append(int(buffer))
        
        while opr_st:
            y = opd_st.pop()
            x = opd_st.pop()
            opd_st.append(self.lookup[opr_st.pop()][1](x, y))
        
        return opd_st.pop()