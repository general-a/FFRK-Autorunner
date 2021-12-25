from PythonScript.src.DataProcessor.ElementFinder import ElementFinder
from PythonScript.src.Helper.LocationHelper import LocationHelper

class ButtonIdentifier:
    BUTTON_PATH = 'etc/images/Buttons/'
    
    def __init__(self, screenFile: str):
        self.screenFile = screenFile
        
    def getButtonLocation(self, button='moveon.png'):
        path = f'{self.BUTTON_PATH}{button}'
        result = ElementFinder.findOneElement(self.screenFile, path)
        return result
    
    def getNextButton(self):
        return self.getButtonLocation('moveon.png')
    
    def getSkipButton(self):
        return self.getButtonLocation('skip.png')
    
    def getCloseButton(self):
        return self.getButtonLocation('close.png')
    
    def getOkButton(self):
        return self.getButtonLocation('ok.png')
    
    def getMiddleChest(self):
        return self.getButtonLocation('middlechest.png')



if __name__ == '__main__':
    image = 'etc/images/winscreen.png'
    test = ButtonIdentifier(image)
    loc = test.getSkipButton()
    LocationHelper.makeLocation(image, [loc])