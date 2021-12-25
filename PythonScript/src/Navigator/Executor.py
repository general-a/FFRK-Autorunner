import time

from PythonScript.src.DataProcessor.PartyChooser import PartyChooser

class Executor:

    @staticmethod
    def doAction(painting, controller, identifier, partyChooser):
        
        def clickButton():
            controller.getScreenshot()
            loc = identifier.buttonIdentifier.getButtonLocation() 
            controller.clickScreen(loc)
        
        print('Sleeping')
        action = painting.event.action
        print(painting.event)
        if action == 'PROCEED':
            clickButton()
                     
        elif action == 'DETERMINE_STATE':
            controller.getScreenshot()
            
        elif action == 'PARTY_SELECTION':
            loc = partyChooser.getParty()
            controller.clickScreen(partyChooser.getParty())
            print(loc)
            time.sleep(3)
            clickButton()
            
        elif action == 'DETERMINE_DOOR_TYPE':
            clickButton()
            
        elif action == 'START_COMBAT_EVENT':
            painting.startCombatEvent()
            
        elif action == 'START_EFFECT_EVENT':
            painting.startEffectEvent()
            clickButton()
            
        elif action == 'START_TREASURE_EVENT':
            painting.startTreasureEvent()
            
        elif action == 'START_LABYRINTH_EVENT':
            painting.startLabyrinthEvent()
                  
        elif action == 'WAIT':
            battle = True
            while(battle):
                print('In Battle... Waiting')
                time.sleep(2)
                controller.getScreenshot()
                battle = identifier.inBattle()
                
        elif action == 'CLICK_SKIP_BUTTON':
            controller.getScreenshot()
            loc = identifier.buttonIdentifier.getSkipButton()
            controller.clickScreen(loc)
            
        elif action == 'CLICK_MIDDLE_CHEST':
            controller.getScreenshot()
            loc = identifier.buttonIdentifier.getMiddleChest()
            controller.clickScreen(loc)
            
        elif action == 'CLICK_OK':
            controller.getScreenshot()
            loc = identifier.buttonIdentifier.getOkButton()
            controller.clickScreen(loc)
        
        elif action == 'CLOSE':
            controller.getScreenshot()
            loc = identifier.buttonIdentifier.getCloseButton()
            controller.clickScreen(loc)
                        
        else:
            raise TypeError(action)
        
        Executor.stateWaiter(painting.event.getState())
        painting.nextAction()

    @staticmethod
    def stateWaiter(state):
        UNIVERSAL_WAIT_TIME = 5
        DOOR_WAIT = 5
        PARTY_TIME = 7
        BATTLE_INFO = 3
        print('Sleeping')
        if state == 'DOOR' or state == 'DETERMINE_STATE':
            time.sleep(DOOR_WAIT)
        elif state == 'BATTLE_INFO':
            time.sleep(BATTLE_INFO)
        elif state == 'PARTY_SELECT':
            time.sleep(PARTY_TIME)
        else:
            time.sleep(UNIVERSAL_WAIT_TIME)


     
if __name__ == '__main__':
    Executor.doAction.clickButton()