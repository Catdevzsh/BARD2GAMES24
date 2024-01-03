import pygame
import sys

# Initialize pygame
pygame.init()

# Set the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption('Pong')

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create a paddle object for each player
paddle_left = pygame.Rect(30, SCREEN_HEIGHT / 2 - 75, 10, 150)
paddle_right = pygame.Rect(SCREEN_WIDTH - 40, SCREEN_HEIGHT / 2 - 75, 10, 150)

# Create the ball object
ball = pygame.Rect(SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2 - 10, 20, 20)

# Set the speed of the ball
ball_speed_x = 5
ball_speed_y = 5

# Set the score for each player
player_left_score = 0
player_right_score = 0

# Create a variable to keep track of who is serving
server = 1

# Create a variable to keep track of when the ball was last hit
last_hit = 0

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # If the left player presses the up key, move the paddle up
            if event.key == pygame.K_w:
                paddle_left.y -= 10

            # If the left player presses the down key, move the paddle down
            elif event.key == pygame.K_s:
                paddle_left.y += 10

            # If the right player presses the up key, move the paddle up
            if event.key == pygame.K_UP:
                paddle_right.y -= 10

            # If the right player presses the down key, move the paddle down
            elif event.key == pygame.K_DOWN:
                paddle_right.y += 10

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check if the ball has hit the left or right walls
    if ball.x < 0 or ball.x > SCREEN_WIDTH:
        # If the ball has hit the left wall, the right player scores a point
        if ball.x < 0:
            player_right_score += 1

        # If the ball has hit the right wall, the left player scores a point
        elif ball.x > SCREEN_WIDTH:
            player_left_score += 1

        # Reset the ball to the center of the screen
        ball.x = SCREEN_WIDTH / 2 - 10
        ball.y = SCREEN_HEIGHT / 2 - 10

        # Reverse the direction of the ball
        ball_speed_x = -ball_speed_x

    # Check if the ball has hit the top or bottom walls
    if ball.y < 0 or ball.y > SCREEN_HEIGHT:
        # If the ball has hit the top wall, reverse the direction of the ball
        if ball.y < 0:
            ball_speed_y = -ball_speed_y

        # If the ball has hit the bottom wall, reverse the direction of the ball
        elif ball.y > SCREEN_HEIGHT:
            ball_speed_y = -ball_speed_y

    # Check if the ball has hit either paddle
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        # If the ball has hit the left paddle, reverse the direction of the ball
        if ball.colliderect(paddle_left):
            ball_speed_x = -ball_speed_x

        # If the ball has hit the right paddle, reverse the direction of the ball
        elif ball.colliderect(paddle_right):
            ball_speed_x = -ball_speed_x

        # Increase the speed of the ball
        ball_speed_x += 1
        ball_speed_y += 1

        # Reset the last_hit timer
        last_hit = pygame.time.get_ticks()

    # Check if the ball has been in play for too long
    if pygame.time.get_ticks() - last_hit > 5000:
        # If the ball has been in play for too long, reset the ball to the center of the screen
        ball.x = SCREEN_WIDTH / 2 - 10
        ball.y = SCREEN_HEIGHT / 2 - 10

        # Reverse the direction of the ball
        ball_speed_x = -ball_speed_x

        # Reset the last_hit timer
        last_hit = pygame.time.get_ticks()

    # Check if either player has won
    if player_left_score == 11 or player_right_score == 11:
        # If the left player has won, display a message
        if player_left_score == 11:
            message = 'Player Left Wins!'

        # If the right player has won, display a message
        elif player_right_score == 11:
            message = 'Player Right Wins!'

        # Display the message
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(message, True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        screen.fill(BLACK)
        screen.blit(text, text_rect)
        pygame.display.update()

        # Wait for the user to press a key
        pygame.event.wait()

        # Reset the game
        player_left_score = 0
        player_right_score = 0
        ball.x = SCREEN_WIDTH / 2 - 10
        ball.y = SCREEN_HEIGHT / 2 - 10
        ball_speed_x = 5
        ball_speed_y = 5
        server = 1
        last_hit = 0

    # Draw the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_left)
    pygame.draw.rect(screen, WHITE, paddle_right)
    pygame.draw.rect(screen, WHITE, ball)

    # Display the score
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(str(player_left_score) + ' : ' + str(player_right_score), True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH / 2, 30)
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()

    # Clock tick
    pygame.time.Clock().tick(60)
