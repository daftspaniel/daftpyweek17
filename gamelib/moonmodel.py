import random
import jsonpickle

from gamelib.util import *

class MoonModel(object):

    """
    Square map of moon model.
    """

    def __init__(self, Width):
        """ Initialise """
        self.Width = Width
        self.Sectors = None
        
    def Generate(self):
        """ Generate a moon """
        
        w = self.Width
        self.Sectors = [[{"ground" : True } for i in range(w)] for j in range(w)]
        S = self.Sectors
                
        NewWater = []
        print("Adding water")
        waterlocations = self._addFeature( int(w/8), "water", returnTrue )
        print("Growing water")
        self._growFeature("water", waterlocations, int(w/16), returnTrue, "ground")
        
        #Make one big water body
        print("Growing Loch")
        print([waterlocations[0]])
        self._growFeature("water", [waterlocations[0]], int(w/2), returnTrue, "ground")
        
        print("Adding trees to seed woods")
        treelocations =  self._addFeature( int(w/12), "tree", self.rndGroundpos )
        
        print("Growing trees")
        self._growFeature("tree", treelocations, int(w/8), self.rndGroundpos)
        
        print("Adding lone trees")
        self._addFeature( w*3, "tree", self.rndGroundpos )
        
        print("Adding mushrooms")
        self._addFeature( w*3, "mushroom", self.rndGroundpos )
        
        print("Adding flowers")
        self._addFeature( w*3, "flowers", self.rndGroundpos )
        
        print("Adding Snow")
        S[int(w/2)][0] = {"snow" : True}
        S[int(w/2)][1] = {"snow" : True}
        S[int(w/2)][w-2] = {"snow" : True}
        S[int(w/2)][w-1] = {"snow" : True}
        self._growFeature("snow", [(int(w/2),2), (int(w/2),w-2), (int(w/2),w-2), (int(w/2),w-3)], 25, returnTrue)
        
        print("Adding Shore")
        for x in range(1,w-1):
            for y in range(1,w-1):
                r = S[x][y]
                if (not "water" in r):
                    if ("water" in S[x][y+1]):
                        r["shore"] = self.get2rndGroundpos()
                    if ("water" in S[x][y-1]):
                        r["shore"] = self.get2rndGroundpos()
                    if ("water" in S[x+1][y]):
                        r["shore"] = self.get2rndGroundpos()
                    if ("water" in S[x-1][y]):
                        r["shore"] = self.get2rndGroundpos()
                    #if ("water" in r): del r["water"]
        
        print("Moon created.")

    """
        Grow a feature optionally replacing another.
    """
    def _growFeature(self, feature, featurelocations, cycles, valueMaker, remove = None):
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
                    if not feature in S[tx][ty]: 
                        S[tx][ty] [feature] = valueMaker()
                        #print("+")
                        if not remove == None:
                            #print("Remove" + remove)
                            if remove in S[tx][ty]:
                                del S[tx][ty][remove]
                        NewFeatures.append( (tx,ty) )
                except Exception as e:
                    pass
                    #print("Exception")
                    #print(e)
                    #print(dir(e))
    
    def _addFeature(self, count, label, valueMaker):
        """ Add a number of items to the map """
        compcount = 0
        w = self.Width
        locations = []
        while compcount<count:
            x = random.randint(1, w)-1
            y = random.randint(1, w)-1
            r = self.Sectors[x][y]
            if not label in r:
                r[label] = valueMaker()
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
        
    def rndGroundpos(self):
        return (RND(100),RND(100))
        
    def get2rndGroundpos(self):
        return [(RND(50),RND(100)), (60 + RND(30),RND(100))]
        
if __name__=="__main__":
    # /* Exercise */
    o = MoonModel(8)

    print(o.Width)
    print(o.Generate())
    print(o)
    print(o.Load())
    print("------")
    print(o.Save())
