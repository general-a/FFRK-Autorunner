from PythonScript.src.Navigator.Events.Event import Event

class LabyrinthEvent(Event):
    
    STATES = ['ENTER_LABYRINTH', 'CONFIRM_PARTY', 'CONFIRM_STAMINA']
    END = 'PAINTING_SELECT'
    
    def __init__(self):
        super().__init__('PROCEED', self.STATES)
        
    
    def _advance(self):
        if self.stateNumber < 3:
            self.setActionAndState('PROCEED', self.STATES[self.stateNumber])
        else:
            self.setActionAndState(None, None)
    
    
if __name__ == '__main__':
    t = LabyrinthEvent()
    t.stepForward()
    t.stepForward()
    t.stepForward()
    t.stepForward()