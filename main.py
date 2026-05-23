import pygame
import math



class Ball:
    def __init__(self, x, y, color, radius, speed):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = speed


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.y -= self.speed
        if keys[pygame.K_s]: self.y += self.speed
        if keys[pygame.K_a]: self.x -= self.speed
        if keys[pygame.K_d]: self.x += self.speed


    def reset(self):
        pygame.draw.circle(screen, self.color, (self.x, self.x), self.radius)


    def colide_circle(self, target):
        offset = math.hypot(self.x - target.x, self.y - target.y)
        distanse = self.radius - target.radius
        return offset < distanse



pygame.init()
screen = pygame.display.set_mode((640 * 1.5, 640 * 1.5))
clock = pygame.time.Clock()
bg = pygame.image.load('istockphoto-2184499109-640x640.jpg')
bg = pygame.transform.scale(bg, (640 * 1.5, 640 * 1.5))
# bg = pygame.Surface((100, 100))
# bg.fill((255, 255, 255))


ball = Ball(x = 100, y = 100, color = (255, 0, 0), radius = 100, speed = 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()



    screen.blit(bg, (0, 0))
    ball.move()
    ball.reset()

    clock.tick(60)
    pygame.display.flip()
