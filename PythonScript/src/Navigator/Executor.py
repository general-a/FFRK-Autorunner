import time


class Executor:
    
    @staticmethod
    def doAction(painting, controller, identifier, partyChooser):
        
        def clickButton():
            controller.getScreenshot()
            loc = identifier.buttonIdentifier.getButtonLocation() 
            controller.clickScreen(loc)
        
        # print('Sleeping')
        eventStarted = False
        action = painting.event.action
        print(painting.event)
        if action == 'PROCEED':
            clickButton()
                     
        elif action == 'DETERMINE_STATE':
            controller.getScreenshot()
            
        elif action == 'PARTY_SELECTION':
            loc = partyChooser.getParty()
            print(loc)
            controller.clickScreen(loc)
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
            eventStarted = True
            
        elif action == 'START_LABYRINTH_EVENT':
            painting.startLabyrinthEvent()
            eventStarted = True
               
        elif action == 'WAIT':
            battle = True
            while(battle):
                print('In Battle... Waiting')
                time.sleep(2)
                controller.getScreenshot()
                battle = identifier.inBattle()
                
        elif action == 'NETWORK_WAIT':
            inPaintingRoom = False
            while(not inPaintingRoom):
                print('Waiting for paintings...')
                time.sleep(1)
                controller.getScreenshot()
                inPaintingRoom = identifier.inPaintingRoom()
        
                
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
                
        if not eventStarted:
            painting.nextAction()
            
        Executor.stateWaiter(painting.event.getState())





     
if __name__ == '__main__':
    Executor.doAction.clickButton()