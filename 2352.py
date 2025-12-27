class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        import numpy as np
        numpy_array = np.array(grid)
        transposed = np.transpose(numpy_array)
        counter = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if (numpy_array[i] == transposed[j]).all():
                    counter += 1
        return counter
