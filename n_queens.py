def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False
    for i in range(row):
         if abs(board[i] - col) == abs(i - row):
            return False
    return True
def solve_n_queens(n):
    board = [-1] * n

    def backtrack(row):
        if row == n:
            print_solution(board, n)
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    backtrack(0)
def print_solution(board, n):
    print("\nSolution:")
    for i in range(n):
        row = ["Q" if board[i] == j else "." for j in range(n)]
        print(" ".join(row))
n = int(input("Enter value of N: "))
solve_n_queens(n)