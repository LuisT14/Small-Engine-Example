from SmallEngine.dataStructs import Point
from pyglet import image

#Object these have Postion and texture and are passed to the game engine for displaying
#Documentation https://pyglet.readthedocs.io/en/latest/modules/image/index.html for image 
#Documentaiion https://pyglet.readthedocs.io/en/latest/modules/window_key.html for key

class Object():
    def __init__(self, texture: str, positon=Point(0,0)):
        self.texture = texture
        self.position = positon
        self.imageObj = image.load(self.texture)
    
    # Returns Position
    def getPositon(self):
        return self.position
    
    # Sets Position
    def setPostition(self, vector):
        self.position = vector
    
    # Gets Texture Location
    def getTexture(self):
        return self.texture
    
    # Sets texture location
    def setTexture(self, texture):
        self.texture = texture
        self.imageObj = image.load(self.texture)

    # gets image obj
    def getImageObj(self):
        return self.imageObj
    
    # Gets called when a key is pressed
    def keyEvent(self, symbol):
        pass
