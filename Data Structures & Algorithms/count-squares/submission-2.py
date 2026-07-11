class CountSquares:

    def __init__(self):
        self.grid = {} # keep grid, where grid[x] is the dict of points with the x coordinate; dict[x][y] gives the number 
        # of points at that coordinate

    def add(self, point: List[int]) -> None:
        x, y = point
        if x not in self.grid:
            self.grid[x] = {}
        if y not in self.grid[x]:
            self.grid[x][y] = 0
        self.grid[x][y] += 1

    def count(self, point: List[int]) -> int:
        # if there is a square, there must be a point with the same x coordinate; thus, just loop over all points with the same x-coord
        # and try to complete the square by looking for the remaining points
        # keep the total sum, and current sum is the product of the number of all points that form a square with the current point
        print(self.grid)
        x, y = point
        if x not in self.grid:
            print('Returning 0, x not in self.grid')
            return 0
        total_squares = 0
        points = self.grid[x]

        print(f'Analysing {x=} {y=}, {points=}')
        for y_i in points:
            if y_i == y:            # skip the current point
                continue
            curr_sum = 0
            a = y_i - y      # side length
            print(f'{x=} {y=} {y_i=} {a=}')
            # if there are points with coords (x+a, y) and (x+a, y_i) then multiply their counts and add to total
            # NEED TO TRY BOTH + and - for x
            if x+a in self.grid:
                print(f'{x+a=} in self.grid, adding to sum')
                curr_sum += self.grid[x][y_i] * self.grid[x+a].get(y, 0) * self.grid[x+a].get(y_i, 0)
                print(f'added to sum {curr_sum=}')

            if x-a in self.grid:
                print(f'{x-a=} in self.grid, adding to sum')
                curr_sum += self.grid[x][y_i] * self.grid[x-a].get(y, 0) * self.grid[x-a].get(y_i, 0)
                print(f'added to sum {curr_sum=}')
            total_squares += curr_sum

        
        return total_squares
