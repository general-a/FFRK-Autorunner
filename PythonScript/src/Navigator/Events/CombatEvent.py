from PythonScript.src.Navigator.Events.Event import Event
from PythonScript.src.Navigator.Events.Proceed import Proceed
from PythonScript.src.ConfigureSettings import ConfigureSettings
import time


class CombatEvent(Event):
    configurer = ConfigureSettings()
    END = 'PAINTING_SELECT'
    STATES = ['BATTLE_INFO', 'PARTY_SELECT', 'FATIGUED',
              'IN_BATTLE', 'RESULTS', 'FINAL_RESULTS', 'WAITING_FOR_PAINTINGS']
    FATIGUE_FILE = configurer.getFileFromPath('FatigueFile')
    TOLERANCE = configurer.getTolerance('Combat')
    
    def __init__(self, isExploration=False):
        if isExploration:
            super().__init__('PROCEED', self.STATES)
            self.stateNumber += 1
        else:
            super().__init__('PROCEED', self.STATES)
        self.proceed = Proceed()
        self.tolerance = self.TOLERANCE
        self.fatigueFile = self.FATIGUE_FILE
     
        
    def _advance(self):
        proceed = self.proceed
        stateNum = self.stateNumber
        if stateNum == 1:
            self.setActionAndState('PARTY_SELECTION', self.STATES[stateNum])
        elif stateNum == 2:
            if self.isFatigued():
                self.setActionAndState('CLICK_OK', self.STATES[stateNum])
            else:
                self.stateNumber += 1
                self.setActionAndState('WAIT', self.STATES[self.stateNumber])      
        elif stateNum == 3:
            self.setActionAndState('WAIT', self.STATES[stateNum])
        elif stateNum == 4:
            self.setActionAndState('CLICK_SKIP_BUTTON', self.STATES[stateNum])
        elif stateNum == 5:
            self.setActionAndState(proceed.getAction(), self.STATES[stateNum])
        elif stateNum == 6:
            self.setActionAndState('NETWORK_WAIT', self.STATES[stateNum])
        else:
            self.setActionAndState(None, None)
            
            
    def isFatigued(self):
        time.sleep(1)
        result = self._getMatchPercent(self.fatigueFile)
        print(result)
        return result > self.tolerance
        

# if __name__ == '__main__':
#     test = CombatEvent()
#     test.stepForward()
#     test.stepForward()
#     test.stepForward()
#     test.stepForward()
#     test.stepForward()
#     test.stepForward()