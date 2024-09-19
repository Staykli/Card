import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Налаштування екрану
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple 2D Game")

# Кольори
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Гравець
player_size = 50
player_pos = [screen_width // 2, screen_height - 2 * player_size]
player_speed = 10

# Перешкоди
obstacle_size = 50
obstacle_pos = [random.randint(0, screen_width - obstacle_size), 0]
obstacle_speed = 10

# Головний цикл гри
game_over = False
clock = pygame.time.Clock()

def detect_collision(player_pos, obstacle_pos):
    p_x, p_y = player_pos
    o_x, o_y = obstacle_pos

    if (o_x >= p_x and o_x < (p_x + player_size)) or (p_x >= o_x and p_x < (o_x + obstacle_size)):
        if (o_y >= p_y and o_y < (p_y + player_size)) or (p_y >= o_y and p_y < (o_y + obstacle_size)):
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed

    screen.fill(black)

    if obstacle_pos[1] >= 0 and obstacle_pos[1] < screen_height:
        obstacle_pos[1] += obstacle_speed
    else:
        obstacle_pos[0] = random.randint(0, screen_width - obstacle_size)
        obstacle_pos[1] = 0

    if detect_collision(player_pos, obstacle_pos):
        game_over = True

    pygame.draw.rect(screen, red, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))
    pygame.draw.rect(screen, white, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()