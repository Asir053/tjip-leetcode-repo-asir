#O(N^2),O(N)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1

        for i, (x, y) in enumerate(points):
            slopes = defaultdict(int) #for every pair formed by curr point
            for x0, y0 in points[i+1:]:
                if x0-x == 0:
                    slope = float(inf)
                else:
                    slope = (y0-y)/(x0-x) 
                slopes[slope] += 1
                res = max(res, slopes[slope]+1)

        return res
