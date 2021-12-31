from PythonScript.src.DataProcessor.PaintingIdentifier import PaintingIdentifier
from PythonScript.src.DataProcessor.ElementFinder import ElementFinder
from PythonScript.src.ConfigureSettings import ConfigureSettings
from PythonScript.src.Controller import Controller
from PythonScript.src.DataProcessor.Paintings.ExplorationPainting import ExplorationPainting
from PythonScript.src.DataProcessor.PartyChooser import PartyChooser
from PythonScript.src.Navigator.Executor import Executor

import time

class Navigator:
    
    configurer = ConfigureSettings()
    ELEMENT_PATH = configurer.getFileFromPath('ElementsPath')
    TREASURE_FILES = configurer.getTreasureList()
    TOLERANCE = configurer.getTolerance()
    
    
    def __init__(self, tolerance=TOLERANCE) -> None:
        self.identifier = PaintingIdentifier()
        self.tolerance = tolerance
        
        
    def walker(self):
        
        def enterPainting():
            for i in range(2):
                controller.clickScreen(loc)
                time.sleep(1)


        identifier = self.identifier
        controller = Controller()
        partyChooser = PartyChooser()
        for i in range(1000):
            controller.getScreenshot()
            painting = self.choosePainting()
            print('Selected: ', painting)
            loc = painting.getLocation()
            enterPainting()
            action = painting.startEvent()
            time.sleep(4)
            while action:
                Executor.doAction(painting, controller, identifier, partyChooser)
                action = painting.event.getAction()
            self.identifier.clearPaintings()
            self.tester()
            

            
    
    def tester(self):
        print('sleeping for 3')
        time.sleep(3)
    
    #Todo: make sure painting selected is not a portal painting when there's treasure
    def choosePainting(self):
        print('Selecting painting...')
        self.identifier.getPaintings()
        paintings = self.identifier.paintings
        if isinstance(paintings[0], ExplorationPainting) and self.treasureExists():
            if isinstance(paintings[1], ExplorationPainting):
                return paintings[2]
            else:
                return paintings[1]
        else: 
            return paintings[0]
         
    
    def treasureExists(self):
        screenFile = self.identifier.getScreenFile()
        secondRowTreasure = f'{self.ELEMENT_PATH}{self.TREASURE_FILES[0]}'
        thirdRowTreasure = f'{self.ELEMENT_PATH}{self.TREASURE_FILES[1]}'
        propForSecondRow = ElementFinder.matchPercentage(screenFile, secondRowTreasure)
        probForThirdRow = ElementFinder.matchPercentage(screenFile, thirdRowTreasure)
        print(f'Prob of teasure in second row: {propForSecondRow} \n Prob for third row:{probForThirdRow}')
        return (propForSecondRow > self.tolerance or
                probForThirdRow > self.tolerance)
    
    #todo: grab screenshot of error screens and implement an error event..
    def isError():
        return False
    


if __name__ == '__main__':
    t = Navigator()
    t.walker()
    