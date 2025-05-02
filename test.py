
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Object")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Player
player_image = pygame.image.load('player.png').convert_alpha()
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Enemy
enemy_size = 90
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = -enemy_size
enemy_speed = 2


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

player = Player (100,100)
all_sprites = pygame.sprite.Group(player)

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    screen.fill(WHITE)
    screen.blit(player_image,(player_x, player_y))
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < WIDTH - player_size:
        player_y += player_speed
    
    

    # Move enemy
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -enemy_size
        enemy_x = random.randint(0, WIDTH - enemy_size)

    # Collision detection
    if (
        player_x < enemy_x + enemy_size and
        player_x + player_size > enemy_x and
        player_y < enemy_y + enemy_size and
        player_y + player_size > enemy_y
    ):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    #trying character sprite
    screen.fill((30,30,30))
    all_sprites.draw(screen)
    pygame.display.flip()


    # Draw player and enemy
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_size, enemy_size))

    pygame.display.flip()

pygame.quit()