from PythonScript.src.Navigator.Events.CombatEvent import CombatEvent

class BossEvent(CombatEvent):
    
    def __init__(self):
        super().__init__()
        self.combatEvent = CombatEvent()

    
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