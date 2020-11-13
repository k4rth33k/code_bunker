from collections import defaultdict, OrderedDict

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        table = [(val, label) for val, label in zip(values, labels)]
        table = sorted(table, reverse=True)
        print(table)
        
        count = defaultdict(int)
        sum_ = 0
        items = 0
        
        for val, label in table:
            if count[label] < use_limit:
                items += 1
                sum_ += val
                count[label] += 1
            
            if items == num_wanted:
                break
        return sum_
        
        