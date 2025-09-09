import pygame

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Acceleration Example")

# Clock for 120 FPS
clock = pygame.time.Clock()
FPS = 120

# Object properties
x, y = 100, HEIGHT // 2
vel_x = 0
acc = 0.2   # acceleration per frame
friction = 0.95  # slows object when no input
size = 40

running = True
while running:
    dt = clock.tick(FPS)  # keep FPS at 120
    screen.fill((30, 30, 30))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Apply acceleration
    if keys[pygame.K_RIGHT]:
        vel_x += acc
    elif keys[pygame.K_LEFT]:
        vel_x -= acc
    else:
        vel_x *= friction  # apply friction when no input

    # Update position
    x += vel_x

    # Draw rectangle
    pygame.draw.rect(screen, (0, 200, 255), (x, y, size, size))

    pygame.display.flip()

pygame.quit()
