import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

x_start = 300
x_end = 500
y = 50
speed = 5

player_width = 200
player_x = 300
player_y = 550
player_speed = 5

ball_radius = 20
ball_x = 400
ball_y = 300
ball_speed_x = 5
ball_speed_y = 5

start_time = time.time()

font = pygame.font.Font(None, 50)

game_over = False
win_game = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_over:
        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if player_x < 100:
        player_x = 100
    if player_x + player_width > 700:
        player_x = 700 - player_width

    x_start += speed
    x_end += speed

    if x_start >= 500 or x_end <= 300:
        speed = -speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - ball_radius <= 100 or ball_x + ball_radius >= 700:
        ball_speed_x = -ball_speed_x

    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    top_rect = pygame.Rect(x_start, y, x_end - x_start, 5)
    bottom_rect = pygame.Rect(player_x, player_y, player_width, 5)

    if ball_rect.colliderect(top_rect):
        ball_speed_y = abs(ball_speed_y)

    if ball_rect.colliderect(bottom_rect):
        ball_speed_y = -abs(ball_speed_y)

    elapsed_time = time.time() - start_time
    if elapsed_time >= 5:
        ball_speed_x *= 1.1
        ball_speed_y *= 1.1
        start_time = time.time()  

    if ball_y - ball_radius > 600:
        game_over = True
        win_game = False

    if ball_y < 0:
        game_over = True
        win_game = True

    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,255,255), (x_start, y), (x_end, y), 5)
    pygame.draw.line(screen, (255,255,255), (player_x, player_y), (player_x + player_width, player_y), 5)

    pygame.draw.circle(screen, (255, 0, 0), (int(ball_x), int(ball_y)), ball_radius)

    pygame.draw.line(screen, "YELLOW", (100, 50), (100, 550), 5)
    pygame.draw.line(screen, "YELLOW", (700, 50), (700, 550), 5)

    if game_over:
        if win_game:
            text = font.render("YOU WIN", True, (255, 255, 0))
        else:
            text = font.render("YOU LOSE", True, (255, 255, 0))
        screen.blit(text, (320, 280))

    pygame.display.flip()
    clock.tick(60)