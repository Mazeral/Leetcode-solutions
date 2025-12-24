class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        if len(gain) == 1:
            return max(0, gain[0])
        altitude = [0] * (len(gain) + 1)
        altitude[0] = 0
        for i, n in enumerate(gain):
            altitude[i + 1] = n + altitude[i]
        return max(altitude)
