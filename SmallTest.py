from SmallEngine.SmallEngine import SmallEngine
from SmallEngine.Object import Object
from pyglet.window import key
from types import MethodType
from SmallEngine.dataStructs import Point

#Modified KeyEvent for Shrek
def keyEvent(self, symbol):
    if(symbol == key.UP):
        self.position.y+=10
    if(symbol == key.DOWN):
        self.position.y-=10
    if(symbol == key.RIGHT):
        self.position.x+=10
    if(symbol == key.LEFT):
        self.position.x-=10
    
if __name__ == "__main__":
    #Creates an instance of the SmallEngine
    MyEngine = SmallEngine(800, 600, "Shrek")
    #Creates ShrekPic object and modifies the keyEvent with ours
    ShrekPic = Object("shrek.png")
    ShrekPic.keyEvent = MethodType(keyEvent, ShrekPic)
    #Adds the object and starts the Engine
    MyEngine.addObject(ShrekPic)
    MyEngine.start()