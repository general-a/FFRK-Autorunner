from PythonScript.src.DataProcessor.Paintings.Painting import Painting
from PythonScript.src.Navigator.Events.EventFactory import EventFactory

class BossPainting(Painting):
    
    def __init__(self, location: tuple) -> None:
        super().__init__(10, 'BOSS', 'boss.png', location)
    
    def startLabyrinthEvent(self):
        self.event = EventFactory.getEvent('LABYRINTH')
        