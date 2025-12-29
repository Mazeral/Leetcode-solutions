from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        queue = deque([[entrance[0], entrance[1], 0]])
        while queue:  
            current_row, current_col, current_dist = queue.popleft()
            current = [current_row, current_col]
            if self.is_exit(maze, current) and current != entrance:
                return current_dist

            hor_limit = [0, len(maze[0]) - 1]
            ver_limit = [0, len(maze) - 1]
            directions = []

            if current[0] + 1 >= ver_limit[0] and current[0] + 1 <= ver_limit[1]:
                up = [current[0] + 1, current[1]]
                directions.append(up)

            if current[0] - 1 >= ver_limit[0] and current[0] <= ver_limit[1]:
                down = [current[0] - 1, current[1]]
                directions.append(down)

            if current[1] - 1 >= hor_limit[0] and current[1] - 1 <= hor_limit[1]:
                left = [current[0], current[1] - 1]
                directions.append(left)

            if current[1] + 1 >= hor_limit[0] and current[1] + 1 <= hor_limit[1]:
                right = [current[0], current[1] + 1]
                directions.append(right)

            for direction in directions:
                location = maze[direction[0]][direction[1]]
                if location is not None and location == '.':
                    maze[direction[0]][direction[1]] = '+' 
                    queue.append([direction[0], direction[1], current_dist + 1])
        return -1

    def is_exit(self, maze, location):
        rows = len(maze)
        cols = len(maze[0])
        if location[0] == 0 or location[0] == rows - 1 or location[1] == 0 or location[1] == cols - 1:
            return True
        return False
