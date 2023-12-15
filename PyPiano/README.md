# Pygame Cheatsheet

## Installation

```bash
pip install pygame
```

## Basic Structure

```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Game logic and rendering here

    pygame.display.flip()
```

## Drawing Shapes

```python
# Draw a rectangle
pygame.draw.rect(screen, color, (x, y, width, height))

# Draw a circle
pygame.draw.circle(screen, color, (x, y), radius)

# Draw a line
pygame.draw.line(screen, color, (x1, y1), (x2, y2), thickness)
```

## Loading Images

```python
# Load an image
image = pygame.image.load("image.png")

# Get the rectangle of the image
rect = image.get_rect()

# Blit the image onto the screen
screen.blit(image, rect)
```

## Handling Keyboard and Mouse Events

```python
# Event handling in the game loop
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            # Handle spacebar press
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            # Handle left mouse button click
```

## Clock and Framerate

```python
# Set up the clock
clock = pygame.time.Clock()

# Limit the frames per second
clock.tick(fps)
```

## Colors

```python
# Define colors using RGB values
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
```

## Sound

```python
# Load a sound
sound = pygame.mixer.Sound("sound.wav")

# Play the sound
sound.play()
```

## Font

```python
# Initialize font
font = pygame.font.Font(None, font_size)

# Render text
text = font.render("Hello, Pygame!", True, text_color)

# Blit text onto the screen
screen.blit(text, (x, y))
```

For more detailed information, refer to the official Pygame documentation: [Pygame Documentation](https://www.pygame.org/docs/)
```
