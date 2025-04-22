class NQueensCSP:
    def __init__(self, N):
        self.N = N
        self.board = [-1] * N  # Board positions

    def is_safe(self, row, col):
        """ Check if placing a queen at (row, col) is safe """
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
               return False
        return True

    def solve(self, row=0):
        """ Backtracking algorithm to solve N-Queens """
        if row == self.N:
            self.print_solution()
            return True  # Return True to stop after one solution

        for col in range(self.N):  # Try placing a queen in each column
            if self.is_safe(row, col):
                self.board[row] = col
                if self.solve(row + 1):
                    return True  # Stop when a solution is found
                self.board[row] = -1  # Backtrack

        return False

    def print_solution(self):
        """ Print board solution in terms of 0s and 1s """
        for i in range(self.N):
            row = [0] * self.N
            row[self.board[i]] = 1  # Place the queen
            print(' '.join(map(str, row)))  # Print row as space-separated numbers
        print("\n")

N = int(input("Enter the number of queens: "))

if N < 1:
    print("Invalid input! The number of queens must be at least 1.")
elif N in [2, 3]:
    print("No solution exists for", N, "queens.")  # 2-Queens and 3-Queens have no solutions
else:
    solver = NQueensCSP(N)
    if not solver.solve():
        print("No solution found, but this should never happen for valid N ≥ 4.")
