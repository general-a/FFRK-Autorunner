from PythonScript.src.DataProcessor.Paintings.Painting import Painting
from PythonScript.src.Navigator.Events.EventFactory import EventFactory

class ExplorationPainting(Painting):
    
    def __init__(self, location: tuple, treasureExists = False) -> None:
        super().__init__(1, 'EXPLORATION', 'exploration.png', location)
    
    def startCombatEvent(self):
        self.event = EventFactory.getEvent('COMBAT', True)
        
    def startTreasureEvent(self):
        self.event = EventFactory.getEvent('TREASURE')

    def startEffectEvent(self):
        self.event = EventFactory.getEvent('EFFECT')
        