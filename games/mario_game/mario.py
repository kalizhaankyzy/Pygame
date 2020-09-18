import pygame, random

pygame.init()

width = 400
height = 400
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
pygame.mixer.music.load("mario_bros.mp3")
pygame.mixer.music.play(-1)
class Player(object):
    def __init__(self):
        self.x = 200
        self.y = 300
        self.dx = 3
        self.score = 0
    def update(self):
        self.surf = pygame.image.load("mario.png")
        screen.blit(self.surf, (self.x,self.y))
        
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.x += self.dx
        elif key[pygame.K_LEFT]:
            self.x -= self.dx
        
class Ball(object):
    def __init__(self):
        self.x = random.randint(20,380)
        self.y = 5
        self.dy = 5
    def draw(self):
        self.surf = pygame.image.load("coin.png")
        screen.blit(self.surf, (self.x,self.y))

player = Player()
ball = Ball()
balls = []
balls.append(ball)
font = pygame.font.SysFont('Pokemon GB.ttf', 30) 
font2 = pygame.font.SysFont('Pokemon GB.ttf', 20)
game = True
gameover = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                        
            game = False
    
    # screen.fill((0,255,255))
    img = pygame.image.load("img.jpg")
    screen.blit(img,(0,0))
    text1 = font.render(("SCORE: "+str(player.score)),1,(255,255,255))
    text1_rect = text1.get_rect()
    text1_x = width / 2 - text1_rect.width / 2
    screen.blit(text1,(text1_x,10))
    player.update()
    
    for ball in balls:
        ball.draw()
        ball.y += ball.dy

    for ball in balls:
        if player.y <=ball.y<=player.y +player.surf.get_height() and player.x <= ball.x <= player.x+player.surf.get_width(): 
            ball.color = ((255,255,255))
            balls.remove(ball)
            new_ball = Ball()
            balls.append(new_ball)
            player.score += 1
        elif ball.y>=height:
            gameover = True
    if gameover == True:
        img = pygame.image.load("img.jpg")
        screen.blit(img,(0,0))
        text = font.render("GAMEOVER",1,(255,255,255))
        text_rect = text.get_rect()
        text_x = width / 2 - text_rect.width / 2
        text_y = height / 2 - text_rect.height / 2
        screen.blit(text, (text_x,text_y))
        text2 = font2.render(("SCORE: "+str(player.score)),1,(255,255,255))
        text2_rect = text2.get_rect()
        text2_x = width / 2 - text2_rect.width / 2
        screen.blit(text2,(text2_x,text_y+20))
        pygame.mixer.music.stop()
    
    pygame.display.update()
    clock.tick(60)
pygame.mixer.quit()