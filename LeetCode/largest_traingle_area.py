import math as m
import itertools

class Solution:
    def area(self, A, B, C):
        return .5 * m.sqrt(((B[0] - A[0]) ** 2)  +  ((B[1] - A[1]) ** 2)) * m.sqrt(((C[0] - A[0]) ** 2)  +  ((C[1] - A[1]) ** 2))
    
    def largestTriangleArea(self, points):
        # def area(p, q, r):
        #     print(p, q, r)
        #     return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
        #                    -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(self.area(*triangle)
            for triangle in itertools.combinations(points, 3))

def util(l):
    _max, s_max = l[0], l[0]

    for e in l[1:]:
        if e > _max:
            s_max = _max
            _max = e

    print(_max, s_max)

if __name__ == '__main__':
    s = Solution()
    print(s.largestTriangleArea([[4,6],[6,5],[3,1]]))
    # util([1,2,3,3,3,3])