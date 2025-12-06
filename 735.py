class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        length = len(asteroids)
        stack = []
        if length == 1:
            return asteroids
        for i in asteroids:
            stack.append(i)
            if len(stack) > 1:
                if stack[-1] < 0:
                    while len(stack) > 1:
                        if abs(stack[-1]) > stack[-2] and stack[-2] > 0:
                            stack.pop(-2)
                        elif abs(stack[-1]) == stack[-2] and stack[-2] > 0:
                            stack.pop()
                            stack.pop()
                            break
                        elif abs(stack[-1]) < stack[-2] and stack[-2] > 0:
                            stack.pop()
                            break
                        else:
                            break
        return stack
