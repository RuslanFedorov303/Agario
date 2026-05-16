import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

player = pygame.Rect(100, 100, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player.y -= 5
    if keys[pygame.K_s]: player.y += 5
    if keys[pygame.K_a]: player.x -= 5
    if keys[pygame.K_d]: player.x += 5

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), player)

    pygame.display.flip()
    clock.tick(60)