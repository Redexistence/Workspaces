import random
import pygame


WIDTH = 600
HEIGHT = 700
CELL_SIZE = WIDTH // 3
BACKGROUND = (245, 245, 235)
GRID_COLOR = (45, 55, 65)
X_COLOR = (220, 75, 65)
O_COLOR = (55, 125, 195)


def winner(board):
	lines = (
		(0, 1, 2), (3, 4, 5), (6, 7, 8),
		(0, 3, 6), (1, 4, 7), (2, 5, 8),
		(0, 4, 8), (2, 4, 6),
	)
	for a, b, c in lines:
		if board[a] != " " and board[a] == board[b] == board[c]:
			return board[a]
	return None


def best_move(board, player):
	result = winner(board)
	if result == "X":
		return 1, None
	if result == "O":
		return -1, None

	moves = [i for i, cell in enumerate(board) if cell == " "]
	if not moves:
		return 0, None

	scored_moves = []
	other_player = "O" if player == "X" else "X"
	for move in moves:
		board[move] = player
		score, _ = best_move(board, other_player)
		board[move] = " "
		scored_moves.append((score, move))

	target = (max if player == "X" else min)(score for score, _ in scored_moves)
	choices = [move for score, move in scored_moves if score == target]
	return target, random.choice(choices)


def play_game():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Tic-Tac-Toe: Computer vs. Computer")
	font = pygame.font.Font(None, 40)
	clock = pygame.time.Clock()
	board = [" "] * 9
	player = "X"
	result = None
	last_move_time = pygame.time.get_ticks()
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
				board = [" "] * 9
				player = "X"
				result = None
				last_move_time = pygame.time.get_ticks()

		if result is None and pygame.time.get_ticks() - last_move_time >= 600:
			_, move = best_move(board, player)
			board[move] = player
			result = winner(board)
			if result is None and " " not in board:
				result = "Draw"
			player = "O" if player == "X" else "X"
			last_move_time = pygame.time.get_ticks()

		screen.fill(BACKGROUND)
		for i in (1, 2):
			pygame.draw.line(screen, GRID_COLOR, (i * CELL_SIZE, 20),
							 (i * CELL_SIZE, WIDTH - 20), 5)
			pygame.draw.line(screen, GRID_COLOR, (20, i * CELL_SIZE + 20),
							 (WIDTH - 20, i * CELL_SIZE + 20), 5)

		for index, mark in enumerate(board):
			if mark == " ":
				continue
			center = ((index % 3) * CELL_SIZE + CELL_SIZE // 2,
					  (index // 3) * CELL_SIZE + CELL_SIZE // 2 + 20)
			if mark == "X":
				offset = 65
				pygame.draw.line(screen, X_COLOR,
							 (center[0] - offset, center[1] - offset),
							 (center[0] + offset, center[1] + offset), 12)
				pygame.draw.line(screen, X_COLOR,
							 (center[0] + offset, center[1] - offset),
							 (center[0] - offset, center[1] + offset), 12)
			else:
				pygame.draw.circle(screen, O_COLOR, center, 72, 12)

		if result == "Draw":
			message = "It's a draw!"
		elif result:
			message = f"{result} wins!"
		else:
			message = f"{player}'s turn"
		label = font.render(message, True, GRID_COLOR)
		screen.blit(label, label.get_rect(center=(WIDTH // 2, 620)))
		restart = font.render("Press R to restart", True, GRID_COLOR)
		screen.blit(restart, restart.get_rect(center=(WIDTH // 2, 665)))
		pygame.display.flip()
		clock.tick(60)

	pygame.quit()


if __name__ == "__main__":
	play_game()
