import pygame
import random
import numpy as np
import sys
import time

pygame.init()

screenW = 1366 
screenH = 768
icon = pygame.image.load("Sprites/DownB_2.png")
screen = pygame.display.set_mode((screenW,screenH),pygame.FULLSCREEN)
#screen = pygame.display.set_mode((screenW,screenH))
pygame.display.set_caption('Warning planet')
pygame.display.set_icon(icon)

Back = pygame.image.load("Wp_Background.png")
plankback = pygame.image.load("Wp_backplank.png")
vitoria = pygame.image.load("Wp_Vitoria.png")
derrota = pygame.image.load("Wp_Derrota.png")
Name = pygame.image.load("Wp_Nome.png")


spriteUp1 = [pygame.image.load("Sprites/UpA_1.png"),pygame.image.load("Sprites/UpA_2.png"),pygame.image.load("Sprites/UpA_3.png")]
spriteRight1 = [pygame.image.load("Sprites/RightA_1.png"),pygame.image.load("Sprites/RightA_2.png"),pygame.image.load("Sprites/RightA_3.png")]
spriteLeft1 = [pygame.image.load("Sprites/LeftA_1.png"),pygame.image.load("Sprites/LeftA_2.png"),pygame.image.load("Sprites/LeftA_3.png")]
spriteDown1 = [pygame.image.load("Sprites/DownA_1.png"),pygame.image.load("Sprites/DownA_2.png"),pygame.image.load("Sprites/DownA_3.png")]

spriteUp2 = [pygame.image.load("Sprites/UpB_1.png"),pygame.image.load("Sprites/UpB_2.png"),pygame.image.load("Sprites/UpB_3.png")]
spriteRight2 = [pygame.image.load("Sprites/RightB_1.png"),pygame.image.load("Sprites/RightB_2.png"),pygame.image.load("Sprites/RightB_3.png")]
spriteLeft2 = [pygame.image.load("Sprites/LeftB_1.png"),pygame.image.load("Sprites/LeftB_2.png"),pygame.image.load("Sprites/LeftB_3.png")]
spriteDown2 = [pygame.image.load("Sprites/DownB_1.png"),pygame.image.load("Sprites/DownB_2.png"),pygame.image.load("Sprites/DownB_3.png")]

Fire = [pygame.image.load("Sprites/Fire__1.png"),pygame.image.load("Sprites/Fire__2.png"),pygame.image.load("Sprites/Fire__3.png"),pygame.image.load("Sprites/Fire__4.png"),pygame.image.load("Sprites/Fire__5.png"),pygame.image.load("Sprites/Fire__6.png"),pygame.image.load("Sprites/Fire__7.png")]

somsirene = pygame.mixer.Sound("Audios/Sirene.wav")
somsirene.set_volume(.3)
somcaught = pygame.mixer.Sound("Audios/Caught.wav")
somcaught.set_volume(.15)
somvitoria = pygame.mixer.Sound("Audios/Victory.wav")
somvitoria.set_volume(.3)

pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("Audios/Good_Times.wav")
pygame.mixer.music.play(5)

class Player1(object):
    def __init__(self,width,height):
        self.create(width,height)
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.hitbox = (self.x, self.y, 32, 32)
        self.center = []
        self.score = 0
    
    def create(self, width, height):
        self.x = random.randint(0,(screenW-width))
        self.y = random.randint(0,(screenH-height))
        if((self.x+width>0 and self.x+width<417) and (self.y+height>0 and self.y+height<153)):
            self.create(width,height)
        if((self.x+width>100 and self.x+width<288) and (self.y+height>464 and self.y+height<619)):
            self.create(width,height)
        if((self.x+width>895 and self.x+width<1029) and (self.y+height>256 and self.y+height<390)):
            self.create(width,height)
        if((self.x+width>1212 and self.x+width<1366) and (self.y+height>588 and self.y+height<768)):
            self.create(width,height)

    def takeCenter(self):
        self.center = (self.x + self.width // 2, self.y + self.height // 2 )
        
    def drawHitbox(self):
        self.hitbox = (self.x, self.y, 32, 32)
        pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    def draw(self, screen):

        if (self.walkCount+1 >= 9):
            self.walkCount = 0

        if self.left:
            screen.blit(spriteLeft2[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            self.takeCenter()

        elif self.right:
            screen.blit(spriteRight2[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
            self.takeCenter()

        elif self.up:
            screen.blit(spriteUp2[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
            self.takeCenter()

        elif self.down:
            screen.blit(spriteDown2[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
            self.takeCenter()

        else:
            screen.blit(spriteDown2[1], (self.x,self.y))
            self.takeCenter()

    def movement(self, screen):
        keys = pygame.key.get_pressed()
      
        if (keys[pygame.K_a]) and self.x - 2 > self.vel:
            if parede(self):
                self.x -= self.vel
                self.left = True
                self.right = False
                self.up=False
                self.down=False

        elif (keys[pygame.K_d]) and self.x + 2 < screenW - self.width - self.vel:
            if parede(self):
                self.x += self.vel
                self.left = False
                self.right = True
                self.up=False
                self.down=False

        elif (keys[pygame.K_w]) and self.y + 2 > self.vel:
            if parede(self):
                self.y -= self.vel
                self.up = True
                self.down = False
                self.left=False
                self.right=False

        elif (keys[pygame.K_s]) and self.y -2 < screenH - self.height - self.vel:
            if parede(self):
                self.y += self.vel
                self.up = False
                self.down = True
                self.left=False
                self.right=False
        else:
            self.left=False
            self.right=False
            self.up=False
            self.down=False
            self.walkCount=0

class Player2(object):
    def __init__(self,width,height):
        self.create(width,height)
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.hitbox = (self.x, self.y, 32, 32)
        self.center = []
        self.score = 0

    def create(self, width, height):
        self.x = random.randint(0,(screenW-width))
        self.y = random.randint(0,(screenH-height))

        if((self.x+width>0 and self.x+width<417) and (self.y+height>0 and self.y+height<153)):
            self.create(width,height)
        if((self.x+width>100 and self.x+width<288) and (self.y+height>464 and self.y+height<619)):
            self.create(width,height)
        if((self.x+width>895 and self.x+width<1029) and (self.y+height>256 and self.y+height<390)):
            self.create(width,height)
        if((self.x+width>1212 and self.x+width<1366) and (self.y+height>588 and self.y+height<768)):
            self.create(width,height)

    def takeCenter(self):
        self.center = (self.x + self.width // 2, self.y + self.height // 2 )
        
    def drawHitbox(self):
        self.hitbox = (self.x, self.y, 32, 32)
        pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    def draw(self, screen):

        if (self.walkCount+1 >= 9):
            self.walkCount = 0

        if self.left:
            screen.blit(spriteLeft1[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            self.takeCenter()

        elif self.right:
            screen.blit(spriteRight1[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
            self.takeCenter()

        elif self.up:
            screen.blit(spriteUp1[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
            self.takeCenter()

        elif self.down:
            screen.blit(spriteDown1[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
            self.takeCenter()

        else:
            screen.blit(spriteDown1[1], (self.x,self.y))
            self.takeCenter()

    def movement(self, screen):
        keys = pygame.key.get_pressed()
      
        if (keys[pygame.K_LEFT]) and self.x > self.vel:
            if parede(self):
                self.x -= self.vel
                self.left = True
                self.right = False
                self.up=False
                self.down=False

        elif (keys[pygame.K_RIGHT]) and self.x < screenW - self.width - self.vel:
            if parede(self):
                self.x += self.vel
                self.left = False
                self.right = True
                self.up=False
                self.down=False

        elif (keys[pygame.K_UP]) and self.y > self.vel:                
            if parede(self):
                self.y -= self.vel
                self.up = True
                self.down = False
                self.left=False
                self.right=False

        elif (keys[pygame.K_DOWN]) and self.y < screenH - self.height - self.vel:
            if parede(self):
                self.y += self.vel
                self.up = False
                self.down = True
                self.left=False
                self.right=False
        else:
            self.left=False
            self.right=False
            self.up=False
            self.down=False
            self.walkCount=0

class Target(object):

    def __init__(self, width, height):
        self.create(width,height)
        self.width = width
        self.height = height
        self.fireCount = 0
        self.caught = False
        self.hitbox = (self.x, self.y, 32, 32)
        self.area = self.listarea()
        self.draw(screen)
    
    def create(self, width, height):
        self.x = random.randint(0,(screenW-width))
        self.y = random.randint(0,(screenH-height))
        if((self.x+width>0 and self.x+width<417) and (self.y+height>0 and self.y+height<153)):
            self.create(width,height)
        if((self.x+width>100 and self.x+width<288) and (self.y+height>464 and self.y+height<619)):
            self.create(width,height)
        if((self.x+width>895 and self.x+width<1029) and (self.y+height>256 and self.y+height<390)):
            self.create(width,height)
        if((self.x+width>1212 and self.x+width<1366) and (self.y+height>588 and self.y+height<768)):
            self.create(width,height)
    
    def marcador(self,screen):
        pixel = []
        for pixel in self.area:
            pygame.draw.rect(screen, (0,0,255), (pixel[0],pixel[1],1,1))
            pygame.display.update()
     
    def drawHitbox(self):
        self.hitbox = (self.x, self.y, 32, 32)
        pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    def draw(self, screen):
        if (self.fireCount+1 >= 21):
            self.fireCount = 0

        screen.blit(Fire[self.fireCount//3], (self.x,self.y))
        self.fireCount += 1        

    def listarea(self):
        areatotal = []
        for col in range(self.width+1):
            for lin in range(self.height+1):
                areatotal.append((self.x+col, self.y+lin))
        return areatotal

def parede(player):
    if((player.x>0 and player.x<417)) and ((player.y>0 and player.y<153)):
        player.x += player.vel
        player.y -= player.vel

    elif((player.x>100 and player.x<288)) and ((player.y>464 and player.y<619)):
        player.x += player.vel
        player.y -= player.vel

    elif(player.x>895 and player.x<1029) and ((player.y>256 and player.y<390)):
        player.x += player.vel
        player.y -= player.vel
    elif((player.x>1212 and player.x<1366)) and ((player.y>588 and player.y<768)):
        player.x += player.vel
        player.y -= player.vel                        
    else:
        return True

def hit(player,fogonatela):
    if player.center in fogonatela.area:
        pygame.mixer.Sound.play(somcaught)
        fogonatela.caught = True
        player.score += 1

def pushTarget(fogonatela):
    global tempo
    if (tempo == 500):
        tempo = 0
        alvos.append(Target(32,32))
    elif(fogonatela.caught == True):
        tempo = 0
        alvos.append(Target(32,32))    

def popTarget(fogonatela):
    if (fogonatela.caught == True):
        alvos.pop(alvos.index(fogonatela))

def final(screen, player1, player2):
    global playing, game_intro
    if (player1.score == 15):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(somvitoria)
        for i in range(20):
            for j in range(3):
                char = pygame.transform.scale(spriteDown2[j], (320, 320))
                pygame.time.delay(50)
                screen.fill((0,0,0))
                screen.blit(vitoria, (0, 0))
                screen.blit(char, (545,282))
                pygame.display.update()
        game_intro = True
        pygame.mixer.Sound.stop(somvitoria)
        pygame.mixer.music.play()

    if (player2.score == 15):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(somvitoria)
        for i in range(20):
            for j in range(3):
                char = pygame.transform.scale(spriteDown1[j], (320, 320))
                pygame.time.delay(50)
                screen.fill((0,0,0))
                screen.blit(vitoria, (0, 0))
                screen.blit(char, (545,282))
                pygame.display.update()
        game_intro = True
        pygame.mixer.Sound.stop(somvitoria)
        pygame.mixer.music.play()

    if (len(alvos)==5):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(somsirene)
        for i in range(10):
            for j in range(6):
                char = pygame.transform.scale(Fire[j], (320, 320))
                pygame.time.delay(50)
                screen.fill((0,0,0))
                screen.blit(derrota, (0, 0))
                screen.blit(char, (545,282))
                pygame.display.update()
        game_intro = True
        pygame.mixer.Sound.stop(somsirene)
        pygame.mixer.music.play()
        

def redrawScreen(fire):
    screen.blit(plankback, (0,0))
    text1 = font.render('Score BOY: ' + str(man.score), 1,(0,0,0))
    screen.blit(text1, (45,27))
    text2 = font.render('Score GIRL: ' + str(woman.score), 1,(0,0,0))
    screen.blit(text2, (47,67))
    for fire in alvos:
        fire.draw(screen)
    man.draw(screen)
    woman.draw(screen)
    
    pygame.display.update()

def game_name(screen):
    screen.blit(Back, (0,0))
    screen.blit(Name, (0,0))
    pygame.display.update()
    pygame.time.delay(500)
    



def personagem(screen):

    players = pygame.image.load("intro_nome.png")
    Controllers = pygame.image.load("Wp_arrow_wasd.png")
    for i in range(20):
        for j in range(3):
            pygame.time.delay(50)
            screen.fill((0,0,0))
            screen.blit(players, (0,0))
            screen.blit(Controllers, (185+j,620+j))
            char1 = pygame.transform.scale(spriteDown1[j], (320, 320))
            char2 = pygame.transform.scale(spriteDown2[j], (320, 320))
            fire = pygame.transform.scale(Fire[j], (320, 320))

            screen.blit(char1, (118,282))
            screen.blit(char2, (545,282))
            screen.blit(fire, (994,264))
            
            pygame.display.update()
    

def historia(screen):
    cont = 0
    while cont!=1850:
        cont += 1 
        for j in range(3):
            
            screen.fill((10,10,10))
            pygame.draw.rect(screen,(50,50,50), (0,600,1366,168))
            
            p2 = pygame.transform.scale(spriteLeft2[j], (320, 320))

            if (cont<200):
                p1 = pygame.transform.scale(spriteRight1[j], (320, 320))
                screen.blit(p1, (cont,282+50))
            else:
                p1 = pygame.transform.scale(spriteRight1[1], (320, 320))
                screen.blit(p1, (200,282+50))
                
            if (cont<500):
                p2 = pygame.transform.scale(spriteLeft2[j], (320, 320))
                screen.blit(p2, (1366-cont,264+50))
            else:
                p2 = pygame.transform.scale(spriteLeft2[1], (320, 320))
                screen.blit(p2, (866,264+50))

            if (cont>500 and cont<800):
                fala11 = font.render('Ei, você viu como a ', 1,(255,255,255))
                fala12 = font.render('floresta ta pegando fogo?', 1,(255,255,255))
                screen.blit(fala11, (400,200))
                screen.blit(fala12, (400,230))
            if (cont>1099 and cont<1400):
                fala11 = font.render('Aposto que eu consigo apagar ', 1,(255,255,255))
                fala12 = font.render('mais focos de incêndio que você.', 1,(255,255,255))
                screen.blit(fala11, (400,200))
                screen.blit(fala12, (400,230))
            if (cont>800 and cont<1100):
                fala11 = font.render('Sim, alguém tem que ', 1,(255,255,255))
                fala12 = font.render('fazer alguma coisa...', 1,(255,255,255))
                screen.blit(fala11, (766,200))
                screen.blit(fala12, (766,230))
            if (cont>1399 and cont<1700):
                fala12 = font.render('Duvido, apostado!!', 1,(255,255,255))
                screen.blit(fala12, (766,230))

            pygame.display.update()

def regrastxt(screen):
    #pygame.font.init()    
    text = pygame.font.SysFont('Arial Bold', 25)
    i = 1
    texto = []
    with open("Regras.txt") as file:
        for info in file:
            texto.append(info)
            
    for info in texto:
        regra = text.render(info, 1, (0,0,0))
        screen.blit(regra, (1050, i*25))
        i+=1

    pygame.display.update()

pygame.font.init()
font = pygame.font.SysFont('Bauhaus 93', 30)
tempo = 0

playing = True
game_intro = True

while playing:

    while game_intro:

        regrastxt(screen)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.display.quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        screen.blit(Back, (0,0))
        screen.blit(Name, (0,0))
        
        if 433+150 > mouse[0] > 433 and 550+50 > mouse[1] > 550:  #Botao de play
            pygame.draw.rect(screen,(0,220,0), (433,550,150,50))
            if click[0] == 1:
                game_intro = False
                personagem(screen)
                man = Player1(32, 32)
                woman = Player2(32,32)
                alvos = [Target(32,32)]
        else: 
            pygame.draw.rect(screen,(0,200,0), (433,550,150,50))

        if 633+150 > mouse[0] > 633 and 550+50 > mouse[1] > 550:  #Botao de Intro
            pygame.draw.rect(screen,(50+10,102+10,152+10), (633,550,150,50))
            if click[0] == 1:
                historia(screen)
                game_name(screen)
        else: 
            pygame.draw.rect(screen,(50-10,102-10,152-10), (633,550,150,50))
        
        if 833+150 > mouse[0] > 833 and 550+50 > mouse[1] > 550:   #Botao de sair
            pygame.draw.rect(screen,(220,0,0), (833,550,150,50))
            if click[0] == 1:                
                game_intro = False
                playing = False
                
        else: 
            pygame.draw.rect(screen,(200,0,0), (833,550,150,50))
        
        PLAY = font.render('PLAY!', 1,(255,255,255),1)
        screen.blit(PLAY, (470,555))

        INTRO = font.render('INTRO', 1,(255,255,255),1)
        screen.blit(INTRO, (668,555))

        EXIT = font.render('EXIT', 1,(255,255,255),1)
        screen.blit(EXIT, (878,555))

        pygame.display.update()

    if playing:
        pygame.time.delay(10)
        tempo += 5
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                playing = False
                pygame.display.quit()

        man.movement(screen)
        woman.movement(screen)

        for fire in alvos:
            hit(man,fire)
            hit(woman,fire)
            popTarget(fire)
            pushTarget(fire)
        
        final(screen, man, woman)
        
        redrawScreen(fire)

pygame.display.quit()