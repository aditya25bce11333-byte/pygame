# pygame Pong Game in Pygame

This is a classic two-player Pong game made in Python using the Pygame library. Players control paddles on the left and right sides of the screen. The goal is to hit the ball past the other player to score points.

Features

- Two-Player Local Multiplayer: Control two different paddles with separate key sets.
- Collision Detection: The ball collides accurately with paddles and screen boundaries.
- Angle/Spin Physics: The angle of the ball's bounce changes based on where it hits the paddle; hitting closer to the edge results in a steeper angle.
- Score Tracking: Shows the current score for both players.
- Game Over Condition: The first player to reach 5 points wins the game.

Prerequisites

You need to have Python 3 installed on your system. This project requires the Pygame library.

Installation

You can install Pygame using pip:

```bash
pip install pygame
```

How to Run

1. Save the Code: Save the provided Python code into a file named pong.py.
2. Run from Terminal: Navigate to the directory where you saved the file and execute:

```bash
python pong.py
```

A game window titled "Pong Game" will open.

Controls

Player Movement Keys

- Left Player: Up (W), Down (S)
- Right Player: Up (Up Arrow), Down (Down Arrow)

Configuration (Constants)

You can adjust the game difficulty and appearance by changing the following global constants near the top of the pong.py file:

| Constant        | Description                                       | Default Value |
|------------------|---------------------------------------------------|---------------|
| SCREEN_WIDTH     | Width of the game window                          | 800           |
| SCREEN_HEIGHT    | Height of the game window                         | 600           |
| PADDLE_W         | Width of the paddles                              | 20            |
| PADDLE_H         | Height of the paddles                             | 100           |
| BALL_SIZE        | Radius of the ball                                | 7             |
| Paddle.SPEED     | Movement speed of the paddles                     | 4             |
| Ball.MAX_SPEED   | Maximum speed of the ball (affects x and y velocity) | 5             |
| winning_score    | The score needed to win the game                  | 5             |

Code Overview

The code is organized with two main classes and several functions:

Classes

- Paddle: Handles the position, drawing, movement, and resetting of the paddles.
- Ball: Manages the position, drawing, movement, and velocity, including angle calculation on collision.

Functions

- draw_everything(...): Renders the background, scores, paddles, ball, and the center line.
- check_collisions(...): Implements physics for wall and paddle bounces.
- move_paddles(...): Maps keyboard inputs to paddle movement.
- main(): Contains the main game loop, handles events, updates the game state, and manages scoring and game over conditions.   
