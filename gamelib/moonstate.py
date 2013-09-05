
from gamelib.moonmodel import *

class MoonState(object):

    """
    Class Description
    """

    def __init__(self):
        """ Initialise """
        self.DayPhase = 2
        self.Time = 0
        self.Danger = 0
        self.Size = 0
        self.Model = MoonModel(128)
        self.Model.Generate()
        self.PlayerPos = [5,5]
        self.PlayerDirection = 2
        
    def CurrSector(self):
        return self.Model.Sectors[self.PlayerPos[0]][self.PlayerPos[1]]
    
    def GetSectorsAhead(self):
        x = self.PlayerPos[0]
        y = self.PlayerPos[1]
        ahead = [self.CurrSector()]
        if self.PlayerDirection == 1:
            ahead.append(self._getSector(x, y - 1))
            ahead.append(self._getSector(x, y - 2))
        elif self.PlayerDirection == 2:
            ahead.append(self._getSector(x + 1, y))
            ahead.append(self._getSector(x + 2, y))
        elif self.PlayerDirection == 3:
            ahead.append(self._getSector(x, y + 1))
            ahead.append(self._getSector(x, y + 2))
        elif self.PlayerDirection == 4:
            ahead.append(self._getSector(x - 1, y))
            ahead.append(self._getSector(x - 2, y))
        return ahead
        
    def MovePlayerForward(self):
        if self.PlayerDirection == 1:
            xm, ym = 0, -1
        elif self.PlayerDirection == 2:
            xm, ym = 1, 0
        elif self.PlayerDirection == 3:
            xm, ym = 0, 1
        elif self.PlayerDirection == 4:
            xm, ym = -1, 0
        self.PlayerPos[0] += xm
        self.PlayerPos[1] += ym

    def MovePlayerBack(self):
        if self.PlayerDirection == 1:
            xm, ym = 0, 1
        elif self.PlayerDirection == 2:
            xm, ym = -1, 0
        elif self.PlayerDirection == 3:
            xm, ym = 0, -1
        elif self.PlayerDirection == 4:
            xm, ym = 1, 0
        self.PlayerPos[0] += xm
        self.PlayerPos[1] += ym
        
    def TurnLeft(self):
        self.PlayerDirection -=1
        if self.PlayerDirection==0: self.PlayerDirection = 4
        
    def TurnRight(self):
        self.PlayerDirection +=1
        if self.PlayerDirection==5: self.PlayerDirection = 1
        
    def _getSector(self,x,y):
        try:
            return self.Model.Sectors[x][y]
        except:
            return None

if __name__=="__main__":

    # /* Exercise */
    o = MoonState()

    print(o.DayPhase)
    print(o.Time)
    print(o.Danger)
    print(o.Size)
    print(o)
