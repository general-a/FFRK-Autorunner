from PythonScript.src.DataProcessor.Paintings.Painting import Painting
from PythonScript.src.Navigator.Events.EventFactory import EventFactory

class BossPainting(Painting):
    
    def __init__(self, location: tuple) -> None:
        super().__init__(10, 'BOSS', 'boss.png', location)
    
    def nextAction(self):
        self.event.stepForward()
        action = self._getAction()
        if action and action[0:5] == 'START':
            self.startLabyrinthEvent()
        
        return self._getAction()
    
    def startLabyrinthEvent(self):
        self.startEvent('LABYRINTH')
        