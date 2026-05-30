import pygame
import random
import math



class Ball:
    def __init__(self,
                 x = 0,
                 y = 0,
                 color  = (255, 0, 0),
                 radius = 100,
                 speed  = 10
                 ):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = speed
        self.scale = 1


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.y -= self.speed
        if keys[pygame.K_s]: self.y += self.speed
        if keys[pygame.K_a]: self.x -= self.speed
        if keys[pygame.K_d]: self.x += self.speed


    def reset(self):
        self.scale = max(0.3, min(50 / self.radius, 1.5))
        player_screen_radius = int(self.radius * self.scale)
        pygame.draw.circle(screen, self.color, (size[0] // 2, size[1] // 2), player_screen_radius)


    def colide_circle(self, target):
        offset = math.hypot(self.x - target.x, self.y - target.y)
        distanse = self.radius - target.radius
        return offset < distanse



pygame.init()

size = (640 * 1.5, 640 * 1.5)
screen = pygame.display.set_mode((640 * 1.5, 640 * 1.5))
clock = pygame.time.Clock()
bg = pygame.image.load('istockphoto-2184499109-640x640.jpg')
bg = pygame.transform.scale(bg, (640 * 1.5, 640 * 1.5))
# bg = pygame.Surface((100, 100))
# bg.fill((255, 255, 255))


ball = Ball(x = 100, y = 100, color = (255, 0, 0), radius = 100, speed = 10)
font = pygame.font.Font(None, 50)
running = True
lose = False


cells = [
    Ball(
    random.randint(-2000, 2000),
    random.randint(-2000, 2000),
    10,
    (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255))
    )
    for _ in range(300)
]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(bg, (0, 0))
    ball.move()
    ball.reset()

    to_remove = []

    for cell in cells:
        if cell.colide_circle(ball):
            to_remove.append(cell)
            ball.radius += int(cell.radius * 0.2)
        else:
            sx = int((sell.x - ball.x) * ball.scale + size[0] // 2)
            sy = int((sell.y - ball.y) * ball.scale + size[1] // 2)

        cell_radius = int(cell.radius * ball.scale)
        pygame.draw.circle(screen, cell.color, (sx, sy), cell_radius)


    for cell in to_remove:
        cells.remove(cell)


    if not lose:
        ball.reset()


    if lose:
        t = font.render('Loser!', 1, (244, 0, 0))
        screen.blit(t, (400, 500))




    clock.tick(60)
    pygame.display.flip()