
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
        self.PlayerPos = (5,5)
        
    def CurrSector(self):
        return self.Model.Sectors[self.PlayerPos[0]][self.PlayerPos[1]]

if __name__=="__main__":

    # /* Exercise */
    o = MoonState()

    print(o.DayPhase)
    print(o.Time)
    print(o.Danger)
    print(o.Size)
    print(o)
