import pygame

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Movement Example")

# Clock for controlling FPS
clock = pygame.time.Clock()
FPS = 60

# Object properties
x = 100  # starting position
y = HEIGHT // 2
velocity = 5  # constant speed in pixels per frame

running = True
while running:
    # Limit loop to 60 FPS
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update position
    x += velocity

    # Wrap around screen
    if x > WIDTH:
        x = -50  # reset to left side

    # Clear screen
    screen.fill((30, 30, 30))

    # Draw moving rectangle
    pygame.draw.rect(screen, (255, 100, 0), (int(x), int(y), 50, 50))

    # Update display
    pygame.display.flip()

pygame.quit()
