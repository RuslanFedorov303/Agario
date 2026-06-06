from math import hypot
from pygame import *
from random import randint
import socket
import threading



HOST = '0.0.0.0'
PORT = 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

recv_data = client_socket.recv(64).decode().strip(',')
my_id, my_x, my_y, my_r = map(int, recv_data)


all_players = {}


# Налаштування
size = (1000, 800)
init()
window = display.set_mode(size)
clock = time.Clock()



def receive_data():
    global all_players, lose
    while True:
        try:
            data = sock.recv(4096).decode()
            if "LOSE" in data:
                lose = True
            elif data:
                # Оновлюємо дані ворогів
                for p in data.split("|"):
                    if "," in p:
                        parts = p.split(",")
                        if len(parts) >= 4:
                            pid = int(parts[0])
                            if pid != my_id:
                                all_players[pid] = [int(parts[1]), int(parts[2]), int(parts[3])]
        except:
            break



threading.Thread(target = receive_data, daemon = True).start()



class Ball:
    def __init__(self, x, y, radius, color, speed=0):
        self.x, self.y = x, y
        self.radius = radius
        self.color = color
        self.base_speed = speed
        self.scale = 1.0
        self.growth_limit = 60

    def update_player(self, cells):
        # Масштабування
        self.scale = self.growth_limit / self.radius if self.radius > self.growth_limit else 1.0

        keys = key.get_pressed()
        speed = 15 * self.scale
        if keys[K_UP]: self.y -= speed
        if keys[K_DOWN]: self.y += speed
        if keys[K_LEFT]: self.x -= speed
        if keys[K_RIGHT]: self.x += speed

        # Логіка поїдання (спрощено)
        for cell in cells[:]:
            if self.collidecircle(cell):
                self.radius += cell.radius * 0.2
                cells.remove(cell)

    def draw(self, surface, camera_x, camera_y, camera_scale):
        sx = int((self.x - camera_x) * camera_scale + size[0] // 2)
        sy = int((self.y - camera_y) * camera_scale + size[1] // 2)
        r = int(self.radius * camera_scale)
        draw.circle(surface, self.color, (sx, sy), max(2, r))

    def collidecircle(self, ball2):
        distance = hypot(self.x - ball2.x, self.y - ball2.y)
        return distance < (self.radius + ball2.radius)


# TODO: dkq
# Ініціалізація гравця
player = Ball(0, 0, 30, (0, 255, 100))

# Генерація їжі (яблук)
cells = [Ball(randint(-1000, 1000), randint(-1000, 1000), 10,
              (randint(50, 200), randint(50, 200), randint(50, 200))) for _ in range(1000)]

running = True
while running:
    for e in event.get():
        if e.type == QUIT: running = False

    window.fill((40, 40, 40))

    # Логіка руху
    keys = key.get_pressed()
    speed = 15 * player.scale
    if keys[K_UP]: player.y -= speed
    if keys[K_DOWN]: player.y += speed
    if keys[K_LEFT]: player.x -= speed
    if keys[K_RIGHT]: player.x += speed

    # Оновлення масштабу
    player.scale = player.growth_limit / player.radius if player.radius > player.growth_limit else 1.0

    # Логіка поїдання
    to_remove = []
    for cell in cells:
        # Малюємо їжу
        cell.draw(window, player.x, player.y, player.scale)

        # Перевірка зіткнення
        if player.collidecircle(cell.x, cell.y, cell.radius):
            to_remove.append(cell)
            player.radius += cell.radius * 0.2

    for cell in to_remove:
        cells.remove(cell)
        # Додаємо нове яблуко замість з'їденого
        # cells.append(Ball(randint(-1000, 1000), randint(-1000, 1000), 10, (200, 200, 0)))

    # Малювання гравця
    player.draw(window, player.x, player.y, player.scale)

    display.update()
    clock.tick(60)

quit()