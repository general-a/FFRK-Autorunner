from PythonScript.src.Navigator.Events.Event import Event
from PythonScript.src.Navigator.Events.Proceed import Proceed

class TreasureEvent(Event):
    
    END = 'PAINTING_SELECT'
    STATES = ['TREASURE_ROOM','CONFIRM_CHOICE', 'OPENED_TREASURE', 'CONFIRM_EXIT']
    
    def __init__(self):
        super().__init__('CLICK_MIDDLE_CHEST', self.STATES)
        self.proceed = Proceed()
        
    def _advance(self):
        proceed = self.proceed
        stateNumber = self.stateNumber
        if self.stateNumber == 1:
            self.setActionAndState(proceed.getAction(), self.STATES[stateNumber])
        elif self.stateNumber == 2:
            self.setActionAndState('PROCEED', self.STATES[stateNumber])
        elif self.stateNumber == 3:
            self.setActionAndState('CLICK_OK', self.STATES[stateNumber])
        else:
            self.setActionAndState(None, None)
    
        
        
if __name__ == '__main__':
    t = TreasureEvent()
    print(t.stepForward())
    print(t.stepForward())
    print(t.stepForward())
    print(t.stepForward())
    print(t.stepForward())
