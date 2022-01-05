from PythonScript.src.Navigator.Events.Event import Event
import time

class LabyrinthEvent(Event):
    
    STATES = ['ENTER_LABYRINTH', 'CONFIRM_PARTY', 'CONFIRM_STAMINA']
    END = 'PAINTING_SELECT'
    
    def __init__(self):
        super().__init__('PROCEED', self.STATES)
        
    
    def _advance(self):
        time.sleep(5)
        if self.stateNumber < 3:
            self.setActionAndState('PROCEED', self.STATES[self.stateNumber])
        else:
            self.setActionAndState(None, None)
            
    def takeAction(self):
        action = self.action
        if action == 'PROCEED':
            self.waitForButtonAndClick()
    
    
if __name__ == '__main__':
    t = LabyrinthEvent()
    t.stepForward()
    t.stepForward()
    t.stepForward()
    t.stepForward()