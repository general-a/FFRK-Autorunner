from PythonScript.src.Navigator.Events.Event import Event
from PythonScript.src.ConfigureSettings import ConfigureSettings
import time

class LabyrinthEvent(Event):
    
    STATES = ['ENTER_LABYRINTH', 'CONFIRM_PARTY', 'CONFIRM_STAMINA']
    END = 'PAINTING_SELECT'
    
    def __init__(self):
        super().__init__('CLICK_ENTER', self.STATES)
        self.enterFile = ConfigureSettings().getFileFromPath('EnterPath')
        self.okFile = ConfigureSettings().getFileFromPath('OkFile')
        
    
    def _advance(self):
        if self.stateNumber < 2:
            self.setActionAndState('CLICK_ENTER', self.STATES[self.stateNumber])
        elif self.stateNumber == 2:
            self.setActionAndState('CLICK_OK', self.STATES[self.stateNumber])
        else:
            self.setActionAndState(None, None)
            
    def takeAction(self):
        action = self.action
        if action == 'CLICK_ENTER':
            self.elementWaiter(self.enterFile, .9)
            loc = self.identifier.buttonIdentifier.getEnterButton()
            self.controller.clickScreen(loc)
            time.sleep(1)
        elif action == 'CLICK_OK':
            self.elementWaiter(self.okFile)
            loc = self.identifier.buttonIdentifier.getOkButton()
            self.controller.clickScreen(loc)
    
    
if __name__ == '__main__':
    t = LabyrinthEvent()