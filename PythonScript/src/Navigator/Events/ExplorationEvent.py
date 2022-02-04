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
        self.treasureTolerance = configurer.getTolerance('Treasure')
        self.doorFile = configurer.getFileFromPath('DoorFile')
        self.eventFile = configurer.getFileFromPath('EventFile')
        self.treasureFile = configurer.getFileFromPath('TreasureFile')
        self.battleFile = configurer.getFileFromPath('BattleFile')
        
    def _advance(self):
        if self.stateNumber == 1:
            self.getExplorationResults()
        elif self.stateNumber == 2:
            if self.isTreasure():
                self.setActionAndState('START_TREASURE_EVENT', self.STATES[2])
            else:
                self.setActionAndState('START_COMBAT_EVENT', self.STATES[3])
        else:
            self.setActionAndState(None, None)
            
    def getExplorationResults(self):
        self.waitForExploration()
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
        # print(result)
        return result > self.tolerance

    def isDoor(self):
        result = self._getMatchPercent(self.doorFile)
        # print(result)
        return result > self.tolerance
    
    def isBattle(self):
        result = self._getMatchPercent(self.battleFile)
        # print(result)
        return result > self.tolerance
    
    def isTreasure(self):
        result = self._getMatchPercent(self.treasureFile)
        # print(result)
        return result > self.treasureTolerance
    
    def endRun(self):
        self.stateNumber = 3
        
    def waitForExploration(self):
        while not (self.isBattle() or self.isDoor() or self.isEvent()):
            self.controller.getScreenshot()
            time.sleep(1)
            
    def waitForDoor(self):
        while not (self.isBattle() or self.isTreasure()):
            self.controller.getScreenshot()
            time.sleep(1)
    
    def takeAction(self):
        action = self.action
        if action == 'PROCEED':
            self.waitForButtonAndClick()
                     
        elif action == 'DETERMINE_STATE':
            pass
            
        elif action == 'DETERMINE_DOOR_TYPE':
            self.waitForButtonAndClick()
            self.waitForDoor()
            
        elif action == 'START_COMBAT_EVENT':
            pass
            
        elif action == 'START_EFFECT_EVENT':
            pass
            
        elif action == 'START_TREASURE_EVENT':
            pass
                        
        else:
            raise TypeError(action)  


if __name__ == '__main__':
    test = ExplorationEvent()
    test.stepForward()
    test.stepForward()
    test.stepForward()
    test.stepForward()
    test.stepForward()