import pygame, sys, random
from tkinter import messagebox

def start_game(difficulty):
    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 550, 550
    GRID_SIZE = 20
    GRID_WIDTH = WIDTH // GRID_SIZE
    GRID_HEIGHT = HEIGHT // GRID_SIZE

    # Colors
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # Initialize the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Initialize the snake
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_direction = (1, 0)

    # Initialize the food
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                if event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                if event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                if event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        # Move the snake
        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, new_head)

        # Check for collisions
        if snake[0] == food:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()

        if (
            new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or
            new_head in snake[1:]
        ):
            show_game_over_popup(difficulty, len(snake))

        # Draw the background
        screen.fill(WHITE)

        # Draw the food
        pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw the snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Update the display
        pygame.display.update()

        # Delay to control the game speed based on difficulty
        pygame.time.delay(100 // difficulty)

def show_game_over_popup(difficulty, score):
    result = messagebox.askretrycancel(title="Game Over", message=f"You hit the wall or fouled!\nRetry?")
    if result:
        if messagebox.askyesno(title='Difficulty',message='Retry at a harder level?') :
            start_game(3)
        else:
            start_game(1)
    else:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    # Choose the difficulty level (1 for easy, 2 for medium, 3 for hard)
    difficulty = 1
    start_game(difficulty)
