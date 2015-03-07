'''
Created on 1/03/2015

@author: Jermin
'''
import math
class robot(object):
    '''
    classdocs
    '''
    


    def __init__(self):
        '''
        Constructor
        '''
        self.speed = [2,2]
        self.location = [0,0]
        self.move_amount = [0,0]
        self.rotation = float(180)
        self.rangeDistance = 300
       
    def moveForward(self):
        rotation_rad = self.rotation/180*math.pi
        self.move_amount = [self.move_amount[0] + math.sin(rotation_rad)*self.speed[1], self.move_amount[1] + math.cos(rotation_rad)*self.speed[1]]
        self.location = [self.location[0]+self.move_amount[0], self.location[1]+self.move_amount[1]]
        
    def moveBackward(self):
        rotation_rad = self.rotation/180*math.pi 
        self.move_amount = [self.move_amount[0] - math.sin(rotation_rad)*self.speed[1], self.move_amount[1] - math.cos(rotation_rad)*self.speed[1]]
        self.location = [self.location[0]+self.move_amount[0], self.location[1]+self.move_amount[1]]   
            
    def getLeftLine(self): 
        rotation_rad = (self.rotation+45)/180*math.pi
        return  (self.location[0] + math.sin(rotation_rad)*self.rangeDistance, self.location[1] + math.cos(rotation_rad)*self.rangeDistance) 
    
    def getRightLine(self): 
        rotation_rad = (self.rotation-45)/180*math.pi
        return  (self.location[0] + math.sin(rotation_rad)*self.rangeDistance, self.location[1] + math.cos(rotation_rad)*self.rangeDistance)          
             