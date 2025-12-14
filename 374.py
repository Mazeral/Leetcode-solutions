# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
class Solution:
    def guessNumber(self, n: int) -> int:
        return self.solve(end=n)
    
    def solve(self, start=1, end=0):
        my_guess = (start + end) // 2
        result = guess(my_guess)
        if result == 0:
            return my_guess
        elif result == 1:
            return self.solve(start=my_guess + 1, end=end)
        else:
            return self.solve(start=1, end=my_guess - 1)
