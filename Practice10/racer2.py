# Импорты и инициализация
import pygame
import random
import time
from itertools import chain

pygame.init()

# Цвета
black = pygame.Color((0,0,0))
white = pygame.Color((255,255,255))
red = pygame.Color((255,0,0))
blue = pygame.Color((0,0,255))
green = pygame.Color((0,255,0))

# Некоторые игровые переменные
screen_width = 400
screen_height = 600
speed = 5
# Очки
score = 0
coin_score = 0

# Шрифты и текст для завершения игры
font = pygame.font.SysFont("None", 60)
font_small = pygame.font.SysFont("None", 20)
game_over = font.render("Game Over", True, black)

# Фоновое изображение
background = pygame.image.load("/Users/diyarkarlibay/Downloads/AnimatedStreet.png")

# Экран и счетчик кадров
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
loop = True

# Классы для противников и игрока
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/Users/diyarkarlibay/Downloads/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), -20)
    def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > screen_height):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), -20)
    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/Users/diyarkarlibay/Downloads/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < screen_width:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5,0)

# Класс монеты
# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self, enemy):
        super().__init__()
        self.weights = [30, 40]  # Возможные веса для монеты
        self.weight = random.choice(self.weights)  # Случайное назначение веса
        self.image = pygame.image.load('/Users/diyarkarlibay/Downloads/coin.png')
        self.image = pygame.transform.scale(self.image, (self.weight, self.weight))  # Изменение размера изображения в соответствии с весом
        self.rect = self.image.get_rect()
        coord_range = list(chain(range(22, enemy.rect.center[0] - 24 - 22), range(enemy.rect.center[0] + 24 + 22, screen_width - 22)))
        self.rect.center = (random.choice(coord_range), 0)

    def move(self, enemy):  # Движение монеты аналогично противникам
        self.rect.move_ip(0, speed + self.weight // 10)  # Увеличение скорости в зависимости от веса
        if self.rect.top > screen_height:
            self.rect.top = 0
            coord_range = list(chain(range(22, enemy.rect.center[0] - 24 - 22), range(enemy.rect.center[0] + 24 + 22, screen_width - 22)))
            self.rect.center = (random.choice(coord_range), 0)
            self.weight = random.choice(self.weights)  # Случайное назначение веса при каждом спавне

# Экземпляры игрока и противника
P1 = Player()
E1 = Enemy()
coin = Coin(E1)
# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coins_group = pygame.sprite.Group()
coins_group.add(coin)
car_sprites = pygame.sprite.Group()
car_sprites.add(P1, E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, coin)
# Новое пользовательское событие
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

while loop:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += score

        if event.type == pygame.QUIT:
            loop = False
    
    screen.blit(background, (0,0))
    scores = font_small.render(str(score), True, black)
    coin_scores = font_small.render(f"Coins: {coin_score}", True, black)
    screen.blit(scores, (10,10))
    screen.blit(coin_scores, (300, 10))

    # Отображение и движение всех спрайтов
    for entity in car_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    # Движение монеты для каждого кадра
    screen.blit(coin.image, coin.rect)
    coin.move(E1)
    
    # Экран завершения игры
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("/Users/diyarkarlibay/Downloads/crash.wav").play()
        time.sleep(5)

        screen.fill(red)
        screen.blit(game_over, (30,250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
    if pygame.sprite.spritecollide(P1, coins_group, dokill=True):
        coin_score += 1
        coin = Coin(E1)
        coins_group.add(coin)
        all_sprites.add(coin)
    
    try:
        pygame.display.flip()
    except:
        print("Game Over!")
        loop = False
    clock.tick(60)