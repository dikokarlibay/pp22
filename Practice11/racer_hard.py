import pygame
import random
import time

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
FPS = 60

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
backgroud = pygame.image.load("/Users/diyarkarlibay/Downloads/AnimatedStreet.png")
player_img = pygame.image.load("/Users/diyarkarlibay/Downloads/Player.png")
enemy_img = pygame.image.load("/Users/diyarkarlibay/Downloads/Enemy.png")
coin_img = pygame.image.load("/Users/diyarkarlibay/Downloads/coin.png")
coin_img = pygame.transform.scale(coin_img, (55, 55))
backgroud_music = pygame.mixer.music.load("/Users/diyarkarlibay/Downloads/background.wav")
crash_sound = pygame.mixer.Sound("/Users/diyarkarlibay/Downloads/crash.wav")

font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, "red")

coin_count_font = pygame.font.SysFont("Verdana", 20)
coin_count = 0

pygame.mixer.music.play(-1)

PLAYER_SPEED = 5
ENEMY_SPEED = 4
last_speed_increase_time = pygame.time.get_ticks()  # Время последнего увеличения скорости
SPEED_INCREMENT = 1  # Величина увеличения скорости
SPEED_INCREASE_INTERVAL = 5000  # Интервал увеличения скорости (5 секунд)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.w // 2
        self.rect.y = HEIGHT - self.rect.h
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0) #moves the rectangle, in place
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
        
    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
            
    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = 0
        
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
        
    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED // 2)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
            
    def generate_random_rect(self):
        x = random.randint(45, 70)
        self.image = pygame.transform.scale(self.image, (x, x)) #изменяем размер
        self.rect.x = random.randint(0, WIDTH - self.rect.w )
        self.rect.y = -self.rect.h    #Спавн за пределами экрана

        
player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy, coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(backgroud, (0, 0))

    player.move()
    enemy.move()
    coin.move()
    
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    
    #Проверяем столкновение игрока с монетой
    if pygame.sprite.spritecollideany(player, coin_sprites):
        coin_count += 1
        #ENEMY_SPEED +=2 #Увеличивает скорость при подбирает монеты
        coin.generate_random_rect()
    
    #Проверяем столкновение игрока и врага
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        time.sleep(1)

        screen.fill("black")
        center_rect = game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)

        pygame.display.flip()

        time.sleep(2)
        running = False
    
    #Отображение счёта
    counting = coin_count_font.render(f"Coins: {coin_count}", True, "black")
    screen.blit(counting, (10, 10))

    # Увеличение скорости со временем
    current_time = pygame.time.get_ticks()
    if current_time - last_speed_increase_time >= SPEED_INCREASE_INTERVAL:
        ENEMY_SPEED += SPEED_INCREMENT
        last_speed_increase_time = current_time  # Обновляем время последнего увеличения скорости


    
    #if coin_count == 3:
        #ENEMY_SPEED = 6
    #elif coin_count == 6:
        #ENEMY_SPEED = 7
    #elif coin_count == 12:
        #ENEMY_SPEED = 8         #Increasing speed when player earns n coin
    
    pygame.display.flip() 
    clock.tick(FPS)
pygame.quit()
