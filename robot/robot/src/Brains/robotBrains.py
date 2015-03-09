'''
Created on 9/03/2015

@author: Jermin
'''

#A, B are the motor strength. So A=B>0 means forward, A>B>0 means turn left, A<B>0 turn right
def drive(A,B):
    print("drove "+ A+ " "+ B)

class position(object):
    def __init__(self,x,y,heading):
        self.x = x
        self.y = y
        self.heading = heading
        
class sensorReading(object):
    def __init__(self,degrees,distance):
        self.degrees = degrees
        self.distance = distance

class robotBrains(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    def setPosition(self, position):
        self.position = position
        
    def setSensorReading(self,sensorReading):
        self.sensorReading = sensorReading
        
        
    def update(self):
        #TODO
        drive(0,0) 
        
    