import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Butterfly Catching Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Player (boy) settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Net settings (attached to the player)
net_size = 30
net_offset_x = player_size // 2
net_offset_y = -net_size

# Butterfly settings
butterfly_size = 20
butterfly_speed = 3
butterflies = []

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to spawn a butterfly
def spawn_butterfly():
    x = random.randint(0, WIDTH - butterfly_size)
    butterflies.append([x, 0])

# Main game loop
running = True
spawn_timer = 0
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Spawn butterflies periodically
    spawn_timer += 1
    if spawn_timer >= 60:  # Spawn every 60 frames (~1 second at 60 FPS)
        spawn_butterfly()
        spawn_timer = 0

    # Update butterflies
    for butterfly in butterflies[:]:
        butterfly[1] += butterfly_speed  # Move butterfly down
        # Check if caught by net
        net_x = player_x + net_offset_x
        net_y = player_y + net_offset_y
        if (net_x < butterfly[0] + butterfly_size and
            net_x + net_size > butterfly[0] and
            net_y < butterfly[1] + butterfly_size and
            net_y + net_size > butterfly[1]):
            butterflies.remove(butterfly)
            score += 1
        # Remove butterfly if it goes off-screen
        elif butterfly[1] > HEIGHT:
            butterflies.remove(butterfly)

    # Drawing
    screen.fill(WHITE)  # Background

    # Draw player (boy)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    # Draw net
    pygame.draw.rect(screen, GREEN, (player_x + net_offset_x, player_y + net_offset_y, net_size, net_size))

    # Draw butterflies
    for butterfly in butterflies:
        pygame.draw.circle(screen, YELLOW, (butterfly[0], butterfly[1]), butterfly_size // 2)

    # Draw score
    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
