import pygame
import time

WIDTH, HEIGHT = 400, 400
GRID_SIZE = 8
CELL_SIZE = WIDTH // GRID_SIZE
WHITE, BLACK, RED, GREEN = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8 Queens Puzzle - Backtracking AI")

board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
ai_solved = False

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, GRID_SIZE)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, row=0):
    if row >= GRID_SIZE:
        return True
    for col in range(GRID_SIZE):
        if is_safe(board, row, col):
            board[row][col] = 1
            draw()
            time.sleep(0.2)
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0
    return False

def draw():
    screen.fill(WHITE)
    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = WHITE if (i + j) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            if board[i][j] == 1:
                pygame.draw.circle(screen, RED, (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

    pygame.display.flip()

def get_cell(pos):
    return pos[1] // CELL_SIZE, pos[0] // CELL_SIZE


running = True
while running:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            row, col = get_cell(event.pos)
            board[row][col] = 1 - board[row][col]  # Toggle Queen
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
            ai_solved = solve_n_queens(board)

pygame.quit()
