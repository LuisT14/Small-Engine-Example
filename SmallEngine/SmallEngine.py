import pyglet
from SmallEngine import Object
from dataclasses import dataclass

# Following Documentation https://pyglet.readthedocs.io/en/latest/modules/window.html

class SmallEngine(pyglet.window.Window):
    # Default Constructor ?
    def __init__(self, width: int, height: int, nameWindow: str):
        super().__init__(width, height, nameWindow)
        # Keep Track of the list
        self.objects = []
        # For more advance things in the future
        pyglet.clock.schedule_interval(self.update, 1/30)
    
    # add Object to the Stage
    def addObject(self, obj):
        self.objects.append(obj)

    # removes Object from stage
    def removeObject(self, obj):
        self.objects.remove(obj)

    # Draws objects, called by pyglet's Event Loop
    def on_draw(self):
        super().clear()
        for item in self.objects:
            item.getImageObj().blit(item.getPositon().x, item.getPositon().y)
    
    # Future Implementation
    def update(self, deltatime):
        pass

    # Gets key presses and passes them to objects
    def on_key_press(self, symbol, modifiers):
        for item in self.objects:
            item.keyEvent(symbol)

    # Closes Window 
    def closeWindow(self):
        super().close()
    
    # Starts Small Engine
    def start(self):
        pyglet.app.run()