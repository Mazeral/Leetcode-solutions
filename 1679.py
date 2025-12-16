class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        p1, p2 = 0, len(nums) - 1
        result = 0
        if len(nums) == 1:
            if nums[0] == k:
                return 1
            return 0
        length = len(nums)
        nums.sort()
        while p1 != p2 and p2 > p1:
            # print("length: {}\np1: {}\n p2: {}".format(length, p1, p2))
            if nums[p1] + nums[p2] < k:
                p1 += 1
                if p1 == p2:
                    break
            elif nums[p1] + nums[p2] > k:
                p2 -= 1
                if p2 == p1:
                    break
            else:
                p1 += 1
                p2 -= 1
                result += 1
        return result
