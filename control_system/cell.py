import math
import numpy
from motor import Motor
from common import *

class Cell:
    """Cell class that represents a cell in table \n
    Attributes:
      None
    """

    def __init__(self, cell):
        """Initialize variables used by Cell class \n
        Args: \n
            cell: dict represents a cell data:
                cell.id: int 
                cell.location: list
                cell.coordinates: list
                cell.code: int
                cell.motors: list of objects
        """

        self.id = cell['id']
        self.location = cell['location']
        self.coordinates=cell['coordinates']
        self.code = cell['code']
        self.motors = []
        self.angle = self.magnitude = self.w = -1
        for i in range(len(cell['motors'])):
            self.motors.append(
                Motor({'id': self.id * 10 + i, **cell['motors'][i],  'code': self.code}))

    def __eq__(self, other): 
        return self.id/10  == other.id/10
    
    def __str__(self):
        return self.location
    
    def __repr__(self):
        return f"{self.location}"

    def getStatus(self):
        return (self.angle, self.magnitude, self.w)

    def updateStatus(self, status):
        angle, magnitude, w = status
        self.angle = angle
        self.magnitude = magnitude
        self.w = w

    def move(self, angle, magnitude, w, commonCells):
        theta = angle * 1000 / 57296
        vx = magnitude * math.cos(theta)
        vy = magnitude * math.sin(theta)
        w_= [] 
        w_ccw= [] 
        w_speed= []
        w_.append(-vx + w)
        w_.append(0.5 * vx + (math.sqrt(3) / 2.0) * vy + w)
        w_.append(0.5 * vx - (math.sqrt(3) / 2.0) * vy + w)

        for i in range(3):
            w_[i] = constrain(w_[i], -150, 150)
        for i in range(3):
            w_ccw.append(w_[i] < 0 and True or False)
        for i in range(3):
            w_speed.append(mapping(abs(w_[i]), 0, 150, 0, 255))
        for i in range(3):
            self.motors[i].run(w_ccw[i], w_speed[i], True)
        self.updateStatus((angle, magnitude, w))

        for i in range(len(commonCells)):
            commonCells[i].updateStatus((angle, magnitude, w))
            for j in range(3):
                commonCells[i].motors[j].run(w_ccw[j], w_speed[j], False)

    def stop(self, commonCells):
        for i in range(3):
            self.motors[i].stop(True)
        self.updateStatus((-1, -1, -1))
        for i in range(len(commonCells)):
            commonCells[i].updateStatus((-1, -1, -1))
            for j in range(3):
                commonCells[i].motors[j].stop(False)
        
