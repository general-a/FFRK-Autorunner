from PythonScript.src.Navigator.Events.CombatEvent import CombatEvent
from PythonScript.src.ConfigureSettings import ConfigureSettings
import time

class BossEvent(CombatEvent):
    
    def __init__(self):
        super().__init__()
        self.combatEvent = CombatEvent()
        self.closeFile = ConfigureSettings().getFileFromPath('ClosePath')

    
    def setController(self, controller):
        self.combatEvent.setController(controller)
        self.controller = controller

    def setIdentifier(self, identifier):
        self.combatEvent.setIdentifier(identifier)
        self.identifier = identifier
    
    
    def setPartyChooser(self, partyChooser):
        self.combatEvent.setPartyChooser(partyChooser)
        self.partyChooser = partyChooser
        
        
    def _advance(self):
        if self.stateNumber < 5:
            self.combatEvent.stepForward()
            self.action = self.combatEvent.getAction()
            self.state = self.combatEvent.getState()
            
        else:
            if self.stateNumber == 5:
                self.setActionAndState('CLOSE', 'COMPLETION_SCREEN')
            elif self.stateNumber == 6:
                self.setActionAndState('START_LABYRINTH_EVENT', 'LABYRINTH_SELECT_SCREEN')
            else:
                self.setActionAndState(None, None)


    def takeAction(self):
        if self.stateNumber < 5:
            self.combatEvent.takeAction()
            
        else:
            if self.stateNumber == 5:
                self.elementWaiter(self.closeFile)
                while self.closeExists():
                    self.clickClose()
                    time.sleep(2)
                    self.controller.getScreenshot()

            elif self.stateNumber == 6:
                pass
            else:
                self.setActionAndState(None, None)
                
    def closeExists(self):
        return self.identifier.elementExists(self.closeFile, .9)
        
    
    def clickClose(self):
        loc = self.identifier.buttonIdentifier.getCloseButton()
        self.controller.clickScreen(loc)
    
    

if __name__ == '__main__':
    test = BossEvent()
    test.stepForward()
    test.stepForward()
    test.stepForward()
    test.stepForward()
    test.stepForward()
    test.stepForward()
    test.stepForward()
    test.stepForward()