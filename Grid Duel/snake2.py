import pygame
import sys
import random
import sqlite3
from tkinter import messagebox

def create_scores_table(conn):
    # Create a table to store scores if it doesn't exist
    query = '''
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        difficulty INTEGER,
        score INTEGER
    )
    '''
    conn.execute(query)
    conn.commit()

def save_score(conn, difficulty, score):
    # Save the score to the database
    query = "INSERT INTO scores (difficulty, score) VALUES (?, ?)"
    conn.execute(query, (difficulty, score))
    conn.commit()

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
            save_score(conn, difficulty, len(snake))
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
    result = messagebox.askretrycancel("Game Over", f"You hit the wall or fouled!\nRetry at difficulty {difficulty}?")
    if result:
        start_game(difficulty)
    else:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    # Connect to the SQLite database
    conn = sqlite3.connect('snake_game_scores.db')
    create_scores_table(conn)

    # Choose the difficulty level (1 for easy, 2 for medium, 3 for hard)
    difficulty = 1
    start_game(difficulty)
