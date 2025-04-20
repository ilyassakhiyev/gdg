import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic-Tac-Toe")

drawn_points = []

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        drawn_points.append(mouse_pos)

    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0,0,0), (0, 200), (600, 200), 5)
    pygame.draw.line(screen, (0,0,0), (0, 400), (600, 400), 5)
    pygame.draw.line(screen, (0,0,0), (200, 0), (200, 600), 5)
    pygame.draw.line(screen, (0,0,0), (400, 0), (400, 600), 5)

    for point in drawn_points:
        pygame.draw.circle(screen, (0,0,0), point, 5)

    pygame.display.flip()