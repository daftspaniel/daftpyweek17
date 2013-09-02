#DayPhase,Time,Danger,Size
class MoonState(object):

    """
    Class Description
    """

    def __init__(self):
        """ Initialise """
        self.DayPhase = 0
        self.Time = 0
        self.Danger = 0
        self.Size = 0

    def __str___(self):
        """ __str___ """
        pass
        
if __name__=="__main__":

    # /* Exercise */
    o = MoonState()

    print(o.DayPhase)
    print(o.Time)
    print(o.Danger)
    print(o.Size)
    print(o)
