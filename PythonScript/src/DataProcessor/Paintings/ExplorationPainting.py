from PythonScript.src.DataProcessor.Paintings.Painting import Painting
from PythonScript.src.Navigator.Events.EventFactory import EventFactory

class ExplorationPainting(Painting):
    
    def __init__(self, location: tuple, treasureExists = False) -> None:
        super().__init__(1, 'EXPLORATION', 'exploration.png', location)
        
    def nextAction(self):
        self.event.stepForward()
        action = self._getAction()
        if action and action[0:5] == 'START':
            if action[6:12] == 'COMBAT':
                self.startCombatEvent()
            elif action[6:14] == 'TREASURE':
                self.startTreasureEvent()
            else:
                self.startEffectEvent()
        
        return self._getAction()
            
    
    def startCombatEvent(self):
        self.startEvent('COMBAT', True)
        
    def startTreasureEvent(self):
        self.startEvent('TREASURE')

    def startEffectEvent(self):
        self.startEvent('EFFECT')
        