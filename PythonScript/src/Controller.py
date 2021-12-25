import pyautogui as pyag
from PythonScript.src.ConfigureSettings import ConfigureSettings
from PIL import Image

class Controller:

    def __init__(self):
        configurer = ConfigureSettings()
        self.__region = configurer.getScreenDimensions()
        self.__screenPath = configurer.getFileFromPath('ScreenPath')
        self.__screenFile = configurer.getFileFromPath('ScreenFile')
        self.filePath = self._getFilePath()
        self.topLeft = (self.__region[0], self.__region[1])
    
    def getScreenshot(self):
        gameState = pyag.screenshot(region = self.__region)
        gameState.save(self.filePath)
        gameState.save('etc/images/testing/test.png')
        # self.imageHelper()
        return self.filePath
    
    def _getFilePath(self):
        return f'{self.__screenPath}{self.__screenFile}'


    def clickScreen(self, location):
        trueLocation = [sum(x) for x in zip(location, self.topLeft)]
        pyag.click(trueLocation)
        return True
    
    def imageHelper(self):
        # open method used to open different extension image file
        im = Image.open('etc\images\screenshots\gamestate.png') 
        # This method will show image in any image viewer 
        im.show() 
        
if __name__ == '__main__':
    test = Controller()
    test.clickScreen((107, 500))
