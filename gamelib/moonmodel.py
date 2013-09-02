import random
import jsonpickle
from moonstate import MoonState
from util import *

class MoonModel(object):

    """
    Square map of moon model.
    """

    def __init__(self, Width):
        """ Initialise """
        self.Width = Width
        self.State = MoonState()
        self.Sectors = None
        
    def Generate(self):
        """ Generate a moon """
        
        w = self.Width
        self.Sectors = [[{"ground" : True } for i in range(w)] for j in range(w)]
        S = self.Sectors
                
        NewWater = []
        print("Adding water")
        waterlocations = self._addFeature( int(w/8), "water", True )
        print("Growing water")
        self._growFeature("water", waterlocations, 15 + RND(5), "ground")
        
        #Make one big water body
        print("Growing Loch")
        print(waterlocations[:-1])
        self._growFeature("water", waterlocations[:-1], 25, "ground")
        
        print("Adding trees")
        treelocations =  self._addFeature( int(w/8), "tree", True )
        print("Growing trees")
        self._growFeature("tree", treelocations, 10+RND(5))
        
    """
        Grow a feature optionally replacing another.
    """
    def _growFeature(self, feature, featurelocations, cycles, remove = None):
        NewFeatures = []
        S = self.Sectors
        for u in range(cycles):
            #print(u)
            featurelocations.extend(NewFeatures)
            NewFeatures = []
            for ws in featurelocations:
                tx = ws[0] + randomPlusMinus1()
                ty = ws[1] + randomPlusMinus1()
                try:
                    S[tx][ty] [feature] = True
                    #print("+")
                    if not remove == None:
                        #print("Remove" + remove)
                        if remove in S[tx][ty]:
                            del S[tx][ty][remove]
                    NewFeatures.append( (tx,ty) )
                except Exception as e:
                    print("Exception")
                    #print(e)
                    #print(dir(e))
    
    def _addFeature(self, count, label, value, maker = None):
        """ Add a number of items to the map """
        compcount = 0
        w = self.Width
        locations = []
        while compcount<count:
            x = random.randint(1, w)-1
            y = random.randint(1, w)-1
            r = self.Sectors[x][y]
            if not label in r:
                if maker == None: 
                    r[label] = value
                else:
                    r[label] = maker()
                compcount += 1
                locations.append( (x,y) )
        return locations
        
    def __str__(self):
        """ __str__ """
        w = self.Width
        s = "Moon Model" + "\r\n"
        s += "Width : " + str(w) + "\r\n"
        for x in range(w):
            l=""
            for y in range(w):
                l += str(self.Sectors[x][y])
            s += l + "\r\n"
        return s

    def Load(self):
        """ Load """
        pass

    def Save(self):
        """ Save """
        pickled = jsonpickle.encode(self)
        return pickled

if __name__=="__main__":
    # /* Exercise */
    o = MoonModel(8)

    print(o.Width)
    print(o.Generate())
    print(o)
    print(o.Load())
    print("------")
    print(o.Save())