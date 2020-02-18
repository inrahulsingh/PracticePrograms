import math

class Line:
    def __init__(self,coor1,coor2):
        self.x1=coor1[0]
        self.y1=coor1[1]

        self.x2=coor2[0]
        self.y2=coor2[1]
    
    def distance(self):
        self.d=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        return self.d
    
    def slope(self):
        self.s=((self.y2-self.y1)/(self.x2-self.x1))
        return self.s

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
