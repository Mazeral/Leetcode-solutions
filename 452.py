class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        if len(points) == 1:
            return 1
        intervals = len(points)
        for i in range(1, len(points)):
            if points[i][0] <= points[i - 1][1]:
                intervals -= 1
                points[i][1] = min(points[i][1], points[i-1][1])
        return intervals
