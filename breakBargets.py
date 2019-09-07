#note do not copy past the b emoji into Python Idle it will crash
#maybe other ides can use b emoji but not idle
import pygame

pygame.init()
size = (1600,900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("break the bargets")
clock = pygame.time.Clock()
#big note when doing references to files make sure they are in the same folder as this py folder or oyu have to like type more
class Character:
    def __init__(self, playerNick, speed,x,y,sprite ):
        self.name = playerNick
        self.speed = speed
        self.x = x
        self.y = y
        self.sprite = sprite
        self.spriteIndex = 0
    
            
    def drawCharacter(self):
        screen.blit(self.sprite[self.spriteIndex], (self.x,self.y))

    def moveCharacter(self,x,y):
        self.x += x
        self.y += y

    def CSTICKDOWN(self):
        self.spriteIndex = 1
    def standing(self):
        self.spriteIndex = 0
def menu():
    gameRun = True
    x = 50
    isRight = False
    isLeft = False
    shiekSprite = pygame.image.load("shiek.png")
    shiekSpriteCSTICKDOWN = pygame.image.load("shiekATTACK.jpg")
    shiekspriteList = [shiekSprite, shiekSpriteCSTICKDOWN]

    shiek = Character("CYGN", 1, 50,50,shiekspriteList)

    while gameRun:
        
        for event in pygame.event.get():#this is similiar to making a window in cpp events are like mouse clicks or keyboard presses they all get queued here
            if event.type == pygame.QUIT:#pygame.quit means the user hit the x button on the top right
                gameRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    isLeft = True
                if event.key == pygame.K_RIGHT:#keyup means the user lifted their finger off the key
                    isRight = True
                if(event.key == pygame.K_a):
                    shiek.CSTICKDOWN()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    isLeft = False
                if event.key == pygame.K_RIGHT:
                    isRight = False
                if(event.key == pygame.K_a):
                    shiek.standing()

        if(isLeft):
            x = x -1
            shiek.moveCharacter(-1,0)
        if(isRight):
            x = x + 1
            shiek.moveCharacter(1,0)
        screen.fill((255,0,0))                   #these four numbers are left top width height
        shiek.drawCharacter()

        pygame.display.flip()# this flip is refering to how opengl(the low level language for your motherboard and shit) renders graphics it basically "flips" the image just know you need this to have the screen update
        clock.tick(60)#this is framerate
    pygame.quit()

menu()
