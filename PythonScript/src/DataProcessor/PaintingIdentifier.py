from PythonScript.src.DataProcessor.Paintings.PaintingFactory import PaintingFactory
from PythonScript.src.DataProcessor.Paintings.ExplorationPainting import ExplorationPainting
from PythonScript.src.DataProcessor.ElementFinder import ElementFinder
from PythonScript.src.ConfigureSettings import ConfigureSettings
from PythonScript.src.DataProcessor.ButtonIdentifier import ButtonIdentifier
from PythonScript.src.Controller import Controller

class PaintingIdentifier:
    

    def __init__(self):
        self.paintings = []
        configurer = ConfigureSettings()
        self.PAINTING_PATH = configurer.getFileFromPath('PaintingsPath')
        self.PAINTING_FILES = configurer.getPaintingList()
        self.SCREEN_FILE = configurer.getScreenFile()
        self.buttonIdentifier = ButtonIdentifier(self.SCREEN_FILE)
        self.BATTLE_END = configurer.getFileFromPath('BattleEndFile')
        self.PAINTING_ROOM = configurer.getFileFromPath('PaintingRoomFile')
        self.TOLERANCE = configurer.getTolerance('InBattle')
        self.BUTTON = configurer.getFileFromPath('EventFile')
        self.ELEMENT_PATH = configurer.getFileFromPath('ElementsPath')
        self.TREASURE_FILES = configurer.getTreasureList()
        self.tolerance = configurer.getTolerance()
    
    def identifyPainting(self, paintingType: str):
        try:
            paintings = []
            elementFile = f'{self.PAINTING_PATH}{paintingType}'
            results = ElementFinder.findMultipleElements(self.SCREEN_FILE, elementFile)
            if results:
                for i in results:
                    painting = PaintingFactory.getPainting(paintingType, i)
                    self.paintings.append(painting)
        except IndexError:
            print('Not Valid Paintings Photo')

    def populatePaintings(self):
        i = 0
        while len(self.paintings) < 3 and i < 9:
            png = self.PAINTING_FILES[i]
            self.identifyPainting(png)
            i += 1
        return self.paintings
         
            
    def getPaintings(self):
        Controller().getScreenshot()
        self.populatePaintings()
        self.paintings.sort()
        if self.paintings and isinstance(self.paintings[0], ExplorationPainting) and self.treasureExists():
            self.setNewPriorities()
        return self.paintings
    
    def setNewPriorities(self):
        for i in self.paintings:
            if isinstance(i, ExplorationPainting):
                i.setPriority(9)
        self.paintings.sort()

    
    def inBattle(self):
        result = ElementFinder.matchPercentage(self.SCREEN_FILE, self.BATTLE_END)
        # print(result)
        return self.TOLERANCE > result
    
    def inPaintingRoom(self):
        return self.elementExists(self.PAINTING_ROOM)


    def elementExists(self, element, tolerance=None):
        if not tolerance:
            tolerance = self.TOLERANCE
        result = ElementFinder.matchPercentage(self.SCREEN_FILE, element)
        print(result)
        return tolerance < result
    
    def buttonExists(self):
        return self.elementExists(self.BUTTON, tolerance=.75)
         
    
    def getScreenFile(self):
        return self.SCREEN_FILE
    
    def clearPaintings(self):
        self.paintings = []
        
    def treasureExists(self):
        screenFile = self.getScreenFile()
        secondRowTreasure = f'{self.ELEMENT_PATH}{self.TREASURE_FILES[0]}'
        thirdRowTreasure = f'{self.ELEMENT_PATH}{self.TREASURE_FILES[1]}'
        propForSecondRow = ElementFinder.matchPercentage(screenFile, secondRowTreasure)
        probForThirdRow = ElementFinder.matchPercentage(screenFile, thirdRowTreasure)
        print(f'Prob of teasure in second row: {propForSecondRow} \n Prob for third row:{probForThirdRow}')
        return (propForSecondRow > self.tolerance or
                probForThirdRow > self.tolerance)
        
        
    
if __name__ == '__main__':
    test = PaintingIdentifier()
    test.populatePaintings()
    print(test.paintings)