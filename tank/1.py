import pygame,random,time,math
from math import *
from pygame.locals import(
    KEYDOWN, K_ESCAPE, QUIT, K_UP, K_DOWN, K_LEFT, K_RIGHT,K_RETURN, K_q, K_e, K_a, K_d, K_s, K_w, K_SPACE, K_z, K_x, K_p, K_i   
)
pygame.init()
pygame.mixer.init()
pygame.font.init()

clock = pygame.time.Clock()
RAD = pi / 180

Width = 800
Height = 600
GameDisplay = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("TANKS")

music = pygame.mixer.music.load("music.ogg")
pygame.mixer.music.play(-1)
bullet_sound = pygame.mixer.Sound("bullet.ogg")
bomb_sound = pygame.mixer.Sound("bomb.ogg")
class Bullet(object):
    def __init__(self,x,y,angle):
        self.x = x
        self.y = y
        self.side = 4
        self.angle = angle
        self.color = ((0,0,0))
        self.speed = 10
    
    def update(self):
        self.x +=self.speed*cos(self.angle*RAD)
        self.y +=self.speed*sin(self.angle*RAD)
        
    def draw(self):
        pygame.draw.circle(GameDisplay,self.color,(round(self.x),round(self.y)),self.side)
        

class Tank(object):
    color = ((173,6,35),(0,158,0))
    color_dulo = ((200,0,0),(0,200,0))
    def __init__(self, number):
        self.number = number
        self.x = random.randint(10,700)
        self.y = random.randint(10,500) 
        self.width = 60
        self.height = 40
        self.vel = 80
        self.color = Tank.color[self.number-1]
        self.color_dulo = Tank.color_dulo[self.number-1]
        self.angle = 0
        self.center = (self.x+self.width/2,self.y+self.height/2)
        self.stop = False
        self.life = 3
        self.direction = ""
        self.z = 0
    def update(self,seconds):
        self.speed = self.vel * seconds
        pressedkeys = pygame.key.get_pressed()
        if pressedkeys[K_z]:
            self.stop = 1
        elif pressedkeys[K_x]:
            self.stop = 0
        #Player1
        if self.number ==1 :
            if pressedkeys[K_UP]:
                if self.stop:
                    self.y -= self.speed
                self.direction = 'u'
            elif pressedkeys[K_DOWN]:
                if self.stop:
                    self.y += self.speed
                self.direction = 'd'
            elif pressedkeys[K_RIGHT]:
                if self.stop:
                    self.x += self.speed
                self.direction = 'r'
            elif pressedkeys[K_LEFT]:
                if self.stop:
                    self.x -= self.speed
                self.direction = 'l'
            if pressedkeys[K_p]:
                self.angle += 35*seconds
            elif pressedkeys[K_i]:
                self.angle -= 35*seconds
            if pressedkeys[K_RETURN] and (pygame.time.get_ticks() - self.z)/1000 >=0.2:
                self.z = pygame.time.get_ticks()
                bullet = Bullet(self.center[0]+0.7*self.width*cos(self.angle*RAD),self.center[1]+self.height*sin(self.angle*RAD),self.angle)
                bullets.append(bullet)
                bullet_sound.play()
        #Player2
        if self.number == 2:
            if pressedkeys[K_w]:
                if self.stop:
                    self.y -= self.speed
                self.direction = 'u'
            elif pressedkeys[K_s]:
                if self.stop:
                    self.y += self.speed
                self.direction = 'd'
            elif pressedkeys[K_d]:
                if self.stop:
                    self.x += self.speed
                self.direction = 'r'
            elif pressedkeys[K_a]:
                if self.stop:
                    self.x -= self.speed
                self.direction = 'l'
            if pressedkeys[K_e]:
                self.angle += 35*seconds
            elif pressedkeys[K_q]:
                self.angle -= 35*seconds
                5*seconds
            if pressedkeys[K_SPACE] and (pygame.time.get_ticks() - self.z)/1000 >=0.2:
                self.z = pygame.time.get_ticks()
                bullet = Bullet(self.center[0]+0.7*self.width*cos(self.angle*RAD),self.center[1]+self.height*sin(self.angle*RAD),self.angle)
                bullets.append(bullet)
                bullet_sound.play()
    
        self.center = (self.x+self.width/2,self.y+self.height/2)
        self.draw()
        self.rules()
    def draw(self):
        pygame.draw.rect(GameDisplay, self.color, (self.x,self.y,self.width,self.height))
        pygame.draw.line(GameDisplay, self.color_dulo, self.center,(self.center[0]+0.7*self.width*cos(self.angle*RAD),self.center[1]+self.height*sin(self.angle*RAD)),7)
        pygame.draw.circle(GameDisplay, self.color_dulo, (round(self.center[0]),round(self.center[1])), 13)
    def rules(self):
        if self.y + self.height <= 0:
            self.y = Height
        elif self.y >= Height:
            self.y = 0 - self.height
        elif self.x >= Width:
            self.x = 0 - self.width
        elif self.x + self.width <= 0:
            self.x = Width
        
        if not self.stop:
            if self.direction == "u":#up
                self.y -= self.speed
            elif self.direction == "r":
                self.x += self.speed
            elif self.direction == "d":
                self.y += self.speed
            elif self.direction == "l":
                self.x -= self.speed

tank1 = Tank(1)
tank2 = Tank(2)

tanks = []
tanks.append(tank1)
tanks.append(tank2)
bullets = []


font = pygame.font.SysFont('Pokemon GB.ttf', 30) 
font_win = pygame.font.SysFont('Pokemon GB.ttf', 90) 
font_score = pygame.font.SysFont('Pokemon GB.ttf', 30) 


running = True
gameover = False
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    GameDisplay.fill((214,214,214))
    text1 = font.render("1 Player" + " - " + str(tank1.life),0, (0,0,0))
    GameDisplay.blit(text1, (5,5))
    text2 = font.render("2 Player" + " - " + str(tank2.life),0, (0,0,0))
    GameDisplay.blit(text2, (680,5))
    time = clock.tick(60)
    seconds = time/1000

    for tank in tanks:
        tank.update(seconds)
 
    for bullet in bullets :
        bullet.draw()
        bullet.update()

    for tank in tanks:
        for bullet in bullets:
            if tank.x <= bullet.x <= tank.x + tank.width and tank.y <= bullet.y <= tank.y + tank.height:
                tank.life -= 1
                bullets.remove(bullet)
        if tank.life == 0:
            tank.color = (135, 60, 203)
            tanks.remove(tank)
            bomb_sound.play()
            gameover = True
    
    if gameover==True:
        GameDisplay.fill((0,0,0))
        text2 = font_score.render("Score: "+str(tank1.life)+" - "+str(tank2.life), 0, (255,255,255))
        text2_rect = text2.get_rect()
        text2_x = Width / 2 - text2_rect.width / 2
        GameDisplay.blit(text2,(text2_x,10))
        if tank1.life != 0:
            text = font_win.render("Player 1 WIN", 0, (255,0,0))
            text_rect = text.get_rect()
            text_x = Width / 2 - text_rect.width / 2
            text_y = Height / 2 - text_rect.height / 2
            GameDisplay.blit(text, (text_x,text_y))
        else:
            text = font_win.render("Player 2 WIN", 0, (0,255,0))
            text_rect = text.get_rect()
            text_x = Width / 2 - text_rect.width / 2
            text_y = Height / 2 - text_rect.height / 2
            GameDisplay.blit(text, (text_x,text_y))
        pygame.mixer.music.stop()

    pygame.display.update()
pygame.mixer.quit()