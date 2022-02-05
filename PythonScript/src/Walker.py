from PythonScript.src.DataProcessor.PaintingIdentifier import PaintingIdentifier
from PythonScript.src.DataProcessor.ElementFinder import ElementFinder
from PythonScript.src.ConfigureSettings import ConfigureSettings
from PythonScript.src.Controller import Controller
from PythonScript.src.DataProcessor.Paintings.ExplorationPainting import ExplorationPainting
from PythonScript.src.Navigator.Events.CombatEvent import CombatEvent
from PythonScript.src.DataProcessor.PartyChooser import PartyChooser
from PythonScript.src.Navigator.Executor import Executor
from datetime import datetime
import time

class Walker:
    
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
        for i in range(10000):
            controller.getScreenshot()
            painting = self.choosePainting()
            painting.setController(controller)
            painting.setIdentifier(identifier)
            painting.setPartyChooser(partyChooser)
            print(datetime.now())
            print('Selected: ', painting)
            loc = painting.getLocation()
            enterPainting()
            action = painting.startEvent()
            
            while action:
                painting.event.takeAction()
                action = painting.nextAction()
                
            self.identifier.clearPaintings()
            # self.tester()
            

            
    
    def tester(self):
        print('sleeping for 3')
        time.sleep(3)
    
    #Todo: make sure painting selected is not a portal painting when there's treasure
    def choosePainting(self):
        try:
            print('Selecting painting...')
            self.identifier.getPaintings()
            paintings = self.identifier.paintings
            return paintings[0]
        except IndexError:
            print('Retrying...')
            time.sleep(2)
            paintings = self.retry()
            return paintings[0]

         
    
    def retry(self):
        paintings = []
        i = 0
        while not paintings and i < 10:
            time.sleep(1)
            self.identifier.clearPaintings()
            self.identifier.getPaintings()
            paintings = self.identifier.paintings
            i += 1
        
        if i > 9:
            raise IndexError('Cannot get painting list after 10 trys...')
        
        return paintings

    #todo: grab screenshot of error screens and implement an error event..
    def isError():
        return False
    


if __name__ == '__main__':
    t = Navigator()
    t.walker()
    