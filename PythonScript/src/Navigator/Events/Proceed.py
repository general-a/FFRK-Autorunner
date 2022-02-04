from PythonScript.src.Navigator.Events.Event import Event

class Proceed(Event):
    
    STATES = ['PROCEED_FROM_SCREEN']
    END = 'NEXT_STATE'
    
    def __init__(self):
        super().__init__('PROCEED', self.STATES)
        
    
    def _advance(self):
        self.setActionAndState(None, None)
    
    def takeAction(self):
        self.waitForButtonAndClick()