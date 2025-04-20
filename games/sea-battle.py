import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Sea Battle")

font = pygame.font.Font(None, 50)

ship_image = pygame.image.load("ship_positions_for_the_sea_battle.png")

drawn_points = []

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        drawn_points.append(mouse_pos)

    screen.fill((255,255,255))
    pygame.draw.line(screen, (0,0,0), (300, 0), (300, 400), 5)
    pygame.draw.line(screen, (0,0,0), (0, 100), (600, 100), 5)

    text1 = font.render("Player1", True, (0,255,0))
    text2 = font.render("Player2", True, (0,255,0))

    screen.blit(text1, (70, 30))
    screen.blit(text2, (390, 30))

    screen.blit(ship_image, (5, 120))
    screen.blit(ship_image, (310, 120))

    for point in drawn_points:
        pygame.draw.circle(screen, (0,0,0), point, 1)

    pygame.display.flip()