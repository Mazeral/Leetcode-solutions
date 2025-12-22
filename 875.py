from math import ceil
class Solution:
    def get_hours(self, piles, k):
        return sum(ceil(i / k) for i in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        left, right = 1, max(piles)
        mid = (left + right) // 2
        least_hours = 0
        while left < right:
            mid = (left + right) // 2
            least_hours = self.get_hours(piles=piles, k=mid)
            if least_hours > h:
                left = mid + 1
            else:
                right = mid
        return left
