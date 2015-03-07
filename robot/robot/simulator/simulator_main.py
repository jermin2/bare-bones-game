'''
Created on 1/03/2015

@author: Jermin
'''
import sys,pygame, math
from simulator.robot import robot
from pygame.constants import K_RIGHT, K_LEFT, K_UP, K_DOWN


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
        
        self.ball = pygame.image.load("ball.bmp")
        
        self.player = robot()
        
        #robot image
        self.robotImg = pygame.image.load("robot.jpg")
        self.robotImg = pygame.transform.scale(self.robotImg, (40, 40))
        
        someWall = block(50,50,100,10)
        self.walls = [someWall]


    
    def move(self, key):
        """Move in the direction of the key"""
        move_distance = [0,0]
        
        if(key == K_UP):
            self.player.moveForward()
        if(key == K_DOWN):
            self.player.moveBackward()
        if(key == K_RIGHT):
            self.player.rotation -= 10
        if(key == K_LEFT):
            self.player.rotation += 10
                           
        return move_distance
    

         
    def main(self):
        
        black = 0,0,0
        white = 255,255,255
        
 
        #starting position
        ballrect = self.robotImg.get_rect()
        ballrect = ballrect.move(self.width/4 - ballrect.width/2, self.height/2 - ballrect.height/2)
        self.player.location = [ballrect.x, ballrect.y]
        
        print (ballrect)
        while 1:
            self.player.move_amount= [0 ,0]
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.move(event.key)
                
            #Draw the walls
            #
            #Update location
            #Update Travel
            ballrect = ballrect.move(self.player.move_amount)
            #update Rotation
            robotImg_t, ballrect = rot_center(self.robotImg, ballrect, self.player.rotation)
            self.player.location = ballrect.center
            
            
            self.screen.fill(white)
            for b in self.walls:
                pygame.draw.rect(self.screen, b.colour, b.getRect(), 0)
            
            #Draw Robot
            self.screen.blit(robotImg_t, ballrect)
            #print (ballrect)
            pygame.draw.line(self.screen, black, (ballrect.center), self.player.getLeftLine(), 1)
            pygame.draw.line(self.screen, black, (ballrect.center), self.player.getRightLine(), 1)
            
            pygame.draw.line(self.screen, black, (self.width/2,0), (self.width/2, self.height),1)
            pygame.display.flip()
            
s = Simulator();
s.main()