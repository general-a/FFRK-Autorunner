from PythonScript.src.Navigator.Events.Event import Event
from PythonScript.src.Navigator.Events.Proceed import Proceed
from PythonScript.src.ConfigureSettings import ConfigureSettings
import time
class ExplorationEvent(Event):
    
    END = 'PAINTING_SELECT'
    STATES = ['DETERMINE_STATE', 'DOOR',
              'TREASURE_ROOM', 'COMBAT', 'EVENT']
    
    def __init__(self):
        super().__init__('DETERMINE_STATE', self.STATES)
        configurer = ConfigureSettings()
        self.proceed = Proceed()
        self.tolerance = configurer.getTolerance('Exploration')
        self.doorFile = configurer.getFileFromPath('DoorFile')
        self.eventFile = configurer.getFileFromPath('EventFile')
        self.treasureFile = configurer.getFileFromPath('TreasureFile')
        
    def _advance(self):
        if self.stateNumber == 1:
            self.getExplorationResults()
        elif self.stateNumber == 2:
            time.sleep(3)
            if self.isTreasure():
                self.setActionAndState('START_TREASURE_EVENT', self.STATES[2])
            else:
                self.setActionAndState('START_COMBAT_EVENT', self.STATES[3])
        else:
            self.setActionAndState(None, None)
            
    def getExplorationResults(self):
        time.sleep(3)
        if self.isEvent():
            self.setActionAndState(self.proceed.getAction(), self.STATES[4])
            self.endRun()
        elif self.isDoor():
            self.setActionAndState('DETERMINE_DOOR_TYPE', self.STATES[1])
        else:
            self.setActionAndState('START_COMBAT_EVENT', self.STATES[3])
            self.endRun()
        
    def isEvent(self):
        result = self._getMatchPercent(self.eventFile)
        print(result)
        return result > self.tolerance

    def isDoor(self):
        result = self._getMatchPercent(self.doorFile)
        print(result)
        return result > self.tolerance
    
    def isTreasure(self):
        time.sleep(3)
        result = self._getMatchPercent(self.treasureFile)
        return result > self.tolerance
    
    def endRun(self):
        self.stateNumber = 3


if __name__ == '__main__':
    test = ExplorationEvent()
    test.stepForward()
    test.stepForward()
    test.stepForward()
    test.stepForward()
    test.stepForward()