from PythonScript.src.DataProcessor.Paintings.PaintingFactory import PaintingFactory
from PythonScript.src.DataProcessor.ElementFinder import ElementFinder
from PythonScript.src.ConfigureSettings import ConfigureSettings
from PythonScript.src.DataProcessor.ButtonIdentifier import ButtonIdentifier

class PaintingIdentifier:
    

    def __init__(self):
        self.paintings = []
        configurer = ConfigureSettings()
        self.PAINTING_PATH = configurer.getFileFromPath('PaintingsPath')
        self.PAINTING_FILES = configurer.getPaintingList()
        self.SCREEN_FILE = configurer.getScreenFile()
        self.buttonIdentifier = ButtonIdentifier(self.SCREEN_FILE)
        self.BATTLE_END = configurer.getFileFromPath('BattleEndFile')
        self.TOLERANCE = configurer.getTolerance('InBattle')
    
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
        self.paintings.sort()
         
            
    def getPaintings(self):
        self.populatePaintings()
        return self.paintings.sort()
    
    def inBattle(self):
        result = ElementFinder.matchPercentage(self.SCREEN_FILE, self.BATTLE_END)
        print(result)
        return self.TOLERANCE > result
    
    def getScreenFile(self):
        return self.SCREEN_FILE
    
    def clearPaintings(self):
        self.paintings = []
        
        
    
if __name__ == '__main__':
    test = PaintingIdentifier()
    test.populatePaintings()
    print(test.paintings)