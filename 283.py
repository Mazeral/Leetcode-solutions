class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for n in nums:
            if n == 0:
                nums = self.move_to_end(nums, n)
        
    def move_to_end(self, lst, el):
        lst.append(lst.pop(lst.index(el)))
        return lst
