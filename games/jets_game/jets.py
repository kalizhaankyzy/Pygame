import pygame, random, os

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

class Player(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 3

    def update(self):
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255,255,255))
        screen.blit(self.surf, (self.x,self.y))
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: self.y -= self.speed
        if pressed[pygame.K_DOWN]: self.y += self.speed
        if pressed[pygame.K_LEFT]: self.x -= self.speed
        if pressed[pygame.K_RIGHT]: self.x += self.speed

        if self.x < 0: self.x = 0
        if self.x > width: self.x = width
        if self.y <= 0: self.y = 0
        if self.y >= height: self.y = height

class Enemy(object):
    def __init__(self):
        self.x = random.randint(width + 20,width+100)
        self.y = random.randint(0,height)
        self.speed = random.randint(5,15)

    def update(self):
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255,255,255))
        screen.blit(self.surf, (self.x,self.y))

class Cloud(object):
    def __init__(self):
        self.x = random.randint(width + 20,width+100)
        self.y = random.randint(0,height)
        self.speed = 5

    def update(self):
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0,0,0))
        screen.blit(self.surf, (self.x,self.y))

player = Player()
enemy = Enemy()
cloud = Cloud()

enemies = []
enemies.append(enemy)
clouds = []
clouds.append(cloud)

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

pygame.mixer.music.load("Electric.mp3")
pygame.mixer.music.play(loops=-1)

    
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                        
            run = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.append(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.append(new_cloud)

    screen.fill((135, 206, 250))
    player.update()
    
    for enemy in enemies:
        enemy.update()
        enemy.x -= enemy.speed  

    for cloud in clouds:
        cloud.update()
        cloud.x -= cloud.speed

    for enemy in enemies:
        if player.x <= enemy.x <= player.x+62 and player.y <= enemy.y <= player.y+25:
            run = False
    
    pygame.display.update()
    clock.tick(60)
pygame.mixer.quit()