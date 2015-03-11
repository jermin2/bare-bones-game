'''
Created on 1/03/2015

@author: Jermin
'''
import pygame
from src.simulator.robot import robot


def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect
    
 
class block(object):

    def __init__(self, x,y,w,h):
        self.location = [x,y] 
        self.width = w
        self.length = h
        self.colour = (100,100,50)
        
    def getRect(self):
        return (self.location[0],self.location[1],self.width,self.length )
         
class Simulator(object):
    '''
    classdocs
    '''

    
    
    def __init__(self):
        '''
        Constructor
        '''
        pygame.init()
        size = self.width, self.height = 640,240
        
        self.screen = pygame.display.set_mode(size)
        
        self.player = robot()
        
        #robot image
        self.robotImg = pygame.image.load("robot.bmp")
        self.robotImg = pygame.transform.scale(self.robotImg, (40, 40))
        
        someWall = block(50,50,100,10)
        self.walls = [someWall]

    
    def event_handle(self):
        
    
        key = pygame.key.get_pressed()
        """Move in the direction of the key"""   
        self.player.move_amount= [0 ,0]
        if key[pygame.K_UP]:
            self.player.moveForward()
        if key[pygame.K_DOWN]:
            self.player.moveBackward()
        if key[pygame.K_RIGHT]:
            self.player.rotation -= 10
        if key[pygame.K_LEFT]:
            self.player.rotation += 10   

         
    def main(self):
        
        #Some Constants
        black = 0,0,0
        white = 255,255,255
        
        #Standard Game Stuff
        running = True
        clock = pygame.time.Clock()
 
        #starting position
        ballrect = self.robotImg.get_rect()
        ballrect = ballrect.move(self.width/4 - ballrect.width/2, self.height/2 - ballrect.height/2)
        self.player.location = [ballrect.x, ballrect.y]
         
        while True:
            clock.tick(30) #30 FPS
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False
                    pygame.quit()
                    break
            if not running:
                break


            self.event_handle()
                
            #Update location
            #Update Travel
            ballrect = ballrect.move(self.player.move_amount)
            #update Rotation
            robotImg_t, ballrect = rot_center(self.robotImg, ballrect, self.player.rotation)
            self.player.location = ballrect.center
            
            #Clear the screen
            self.screen.fill(white)
            
            #Draw the walls
            for b in self.walls:
                pygame.draw.rect(self.screen, b.colour, b.getRect(), 0)
            
            #Draw Robot
            self.screen.blit(robotImg_t, ballrect)
            #Draw range finding stuff
            pygame.draw.line(self.screen, black, (ballrect.center), self.player.getLeftLine(), 1)
            pygame.draw.line(self.screen, black, (ballrect.center), self.player.getRightLine(), 1)
            
            pygame.draw.line(self.screen, black, (self.width/2,0), (self.width/2, self.height),1)
            pygame.display.flip()
            
s = Simulator();
s.main()