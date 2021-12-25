from PythonScript.src.Navigator.Events.BossEvent import BossEvent
from PythonScript.src.Navigator.Events.ExplorationEvent import ExplorationEvent
from PythonScript.src.Navigator.Events.CombatEvent import CombatEvent
from PythonScript.src.Navigator.Events.LabyrinthEvent import LabyrinthEvent
from PythonScript.src.Navigator.Events.Proceed import Proceed
from PythonScript.src.Navigator.Events.TreasureEvent import TreasureEvent


class EventFactory:
    
    @staticmethod
    
    def getEvent(event, isExplorationBattle=None):
        if not event:
            return None
        
        if event == 'COMBAT':
            return CombatEvent() #if isExplorationBattle else CombatEvent()        
        elif event == 'EXPLORATION':
            return ExplorationEvent()
        elif event == 'BOSS':
            return BossEvent()
        elif event == 'EFFECT':
            return Proceed()
        elif event == 'TREASURE':
            return TreasureEvent()
        elif event == 'LABYRINTH':
            return LabyrinthEvent()
        else:
            raise TypeError(event)