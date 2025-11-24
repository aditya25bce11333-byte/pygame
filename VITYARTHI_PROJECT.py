import pygame
import random

# Initialize pygame - always need this first
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game object sizes
PADDLE_W = 20
PADDLE_H = 100
BALL_SIZE = 7

# Font for score display
score_font = pygame.font.SysFont("comicsans", 50)

class Paddle:
    SPEED = 4  # movement speed

    def _init_(self, x, y):
        self.x = x
        self.y = y
        self.original_x = x  # remember starting position
        self.original_y = y
        self.rect = pygame.Rect(x, y, PADDLE_W, PADDLE_H)

    def draw(self, win):
        pygame.draw.rect(win, WHITE, self.rect)

    def move(self, up=True):
        if up:
            self.rect.y -= self.SPEED
        else:
            self.rect.y += self.SPEED
        
        # Keep paddle on screen - prevent going off edges
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_HEIGHT - PADDLE_H:
            self.rect.y = SCREEN_HEIGHT - PADDLE_H

    def reset(self):
        # Put paddle back to starting position
        self.rect.x = self.original_x
        self.rect.y = self.original_y


class Ball:
    MAX_SPEED = 5

    def _init_(self, x, y):
        self.x = x
        self.y = y
        self.original_x = x
        self.original_y = y
        # Random starting direction
        self.x_velocity = self.MAX_SPEED if random.randint(0, 1) else -self.MAX_SPEED
        self.y_velocity = self.MAX_SPEED if random.randint(0, 1) else -self.MAX_SPEED

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (int(self.x), int(self.y)), BALL_SIZE)

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def reset(self):
        # Reset ball position and change direction
        self.x = self.original_x
        self.y = self.original_y
        self.y_velocity = self.MAX_SPEED if random.randint(0, 1) else -self.MAX_SPEED
        self.x_velocity = -self.x_velocity  # reverse horizontal direction


def draw_everything(win, paddles, ball, left_score, right_score):
    # Clear screen
    win.fill(BLACK)

    # Draw scores
    left_text = score_font.render(f"{left_score}", 1, WHITE)
    right_text = score_font.render(f"{right_score}", 1, WHITE)
    win.blit(left_text, (SCREEN_WIDTH//4 - left_text.get_width()//2, 20))
    win.blit(right_text, (SCREEN_WIDTH*3//4 - right_text.get_width()//2, 20))

    # Draw paddles
    for paddle in paddles:
        paddle.draw(win)

    # Draw center line - dashed effect
    dash_height = SCREEN_HEIGHT//20
    for i in range(10, SCREEN_HEIGHT, dash_height):
        if i % 2 == 1:  # skip every other dash to create dotted line
            continue
        pygame.draw.rect(win, WHITE, (SCREEN_WIDTH//2 - 5, i, 10, dash_height))

    ball.draw(win)
    pygame.display.update()


def check_collisions(ball, left_paddle, right_paddle):
    # Ball hits top or bottom wall
    if ball.y + BALL_SIZE >= SCREEN_HEIGHT or ball.y - BALL_SIZE <= 0:
        ball.y_velocity *= -1  # reverse vertical direction

    # Create rect for ball collision detection
    ball_rect = pygame.Rect(ball.x - BALL_SIZE, ball.y - BALL_SIZE, BALL_SIZE*2, BALL_SIZE*2)

    # Check paddle collisions
    if ball.x_velocity < 0:  # ball moving left
        if ball_rect.colliderect(left_paddle.rect):
            ball.x_velocity *= -1
            
            # Add some angle based on where ball hits paddle
            paddle_center = left_paddle.rect.y + PADDLE_H / 2
            hit_pos = paddle_center - ball.y
            angle_factor = (PADDLE_H / 2) / ball.MAX_SPEED
            ball.y_velocity = -1 * (hit_pos / angle_factor)
            
    else:  # ball moving right
        if ball_rect.colliderect(right_paddle.rect):
            ball.x_velocity *= -1

            # Same angle calculation for right paddle
            paddle_center = right_paddle.rect.y + PADDLE_H / 2
            hit_pos = paddle_center - ball.y
            angle_factor = (PADDLE_H / 2) / ball.MAX_SPEED
            ball.y_velocity = -1 * (hit_pos / angle_factor)


def move_paddles(keys, left_paddle, right_paddle):
    # Left paddle controls (W/S keys)
    if keys[pygame.K_w]:
        left_paddle.move(up=True)
    if keys[pygame.K_s]:
        left_paddle.move(up=False)

    # Right paddle controls (Arrow keys)
    if keys[pygame.K_UP]:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN]:
        right_paddle.move(up=False)


def main():
    running = True
    game_clock = pygame.time.Clock()

    # Create game objects
    left_paddle = Paddle(10, SCREEN_HEIGHT // 2 - PADDLE_H // 2)
    right_paddle = Paddle(SCREEN_WIDTH - 10 - PADDLE_W, SCREEN_HEIGHT // 2 - PADDLE_H // 2)
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Score tracking
    left_score = 0
    right_score = 0
    winning_score = 5  # first to 5 wins

    while running:
        game_clock.tick(FPS)
        draw_everything(screen, [left_paddle, right_paddle], ball, left_score, right_score)

        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        # Get currently pressed keys
        pressed_keys = pygame.key.get_pressed()
        move_paddles(pressed_keys, left_paddle, right_paddle)

        # Update ball position
        ball.move()
        check_collisions(ball, left_paddle, right_paddle)

        # Check for scoring
        if ball.x < 0:  # ball went off left side
            right_score += 1
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
        elif ball.x > SCREEN_WIDTH:  # ball went off right side
            left_score += 1
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()

        # Check for game over
        if left_score >= winning_score:
            print("Left Player Wins!")
            running = False
        elif right_score >= winning_score:
            print("Right Player Wins!")
            running = False

    pygame.quit()

if __name__ == '_main_':
    main()