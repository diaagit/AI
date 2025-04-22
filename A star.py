import heapq
class PuzzleState:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board  # The puzzle board configuration
        self.parent = parent  # Parent state
        self.move = move  # Move to reach this state
        self.depth = depth  # Depth in the search tree
        self.cost = cost  # Cost (depth + heuristic)

    def __lt__(self, other):
        return self.cost < other.cost

# Function to display the board in a visually appealing format
def print_board(board):
    print("+---+---+---+")
    for row in range(0, 9, 3):
        row_visual = "|"
        for tile in board[row:row + 3]:
            if tile == 0:  # Blank tile
                row_visual += "   |"
            else:
                row_visual += f" {tile} |"
        print(row_visual)
        print("+---+---+---+")

# Possible moves for the blank tile (up, down, left, right)
moves = {
    'U': -3,  # Move up
    'D': 3,   # Move down
    'L': -1,  # Move left
    'R': 1    # Move right
}

# Function to calculate the heuristic (Manhattan distance)
def heuristic(board, goal_state):
    distance = 0
    for i in range(9):
        if board[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_state.index(board[i]), 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Function to get the new state after a move
def move_tile(board, move, blank_pos):
    new_board = board[:]
    new_blank_pos = blank_pos + moves[move]
    new_board[blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[blank_pos]
    return new_board

# A* search algorithm
def a_star(start_state, goal_state):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, PuzzleState(start_state, None, None, 0, heuristic(start_state, goal_state)))

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.board == goal_state:
            return current_state

        closed_list.add(tuple(current_state.board))

        blank_pos = current_state.board.index(0)

        for move in moves:
            if move == 'U' and blank_pos < 3:  # Invalid move up
                continue
            if move == 'D' and blank_pos > 5:  # Invalid move down
                continue
            if move == 'L' and blank_pos % 3 == 0:  # Invalid move left
                continue
            if move == 'R' and blank_pos % 3 == 2:  # Invalid move right
                continue

            new_board = move_tile(current_state.board, move, blank_pos)

            if tuple(new_board) in closed_list:
                continue

            new_state = PuzzleState(new_board, current_state, move, current_state.depth + 1, current_state.depth + 1 + heuristic(new_board, goal_state))
            heapq.heappush(open_list, new_state)

    return None

# Function to print the solution path
def print_solution(solution):
    path = []
    current = solution
    while current:
        path.append(current)
        current = current.parent
    path.reverse()

    for step in path:
        print(f"Move: {step.move}")
        print_board(step.board)

# Function to get user input for the puzzle state
def get_puzzle_state(prompt):
    while True:
        try:
            input_state = input(prompt)
            state = list(map(int, input_state.split()))

            if len(state) != 9 or not all(0 <= num <= 8 for num in state) or len(set(state)) != 9:
                print("Invalid input. Please enter 9 distinct numbers from 0 to 8.")
                continue

            return state
        except ValueError:
            print("Invalid input. Please enter only numbers.")

# Get initial and goal state from the user
initial_state = get_puzzle_state("Enter the initial state as a space-separated list of 9 numbers (0 for blank space): ")
goal_state = get_puzzle_state("Enter the goal state as a space-separated list of 9 numbers (0 for blank space): ")

# Solve the puzzle using A* algorithm
solution = a_star(initial_state, goal_state)
if solution:
    print("Solution found:")
    print_solution(solution)
else:
    print("No solution exists.")
