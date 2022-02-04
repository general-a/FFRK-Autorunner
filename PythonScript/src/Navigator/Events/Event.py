import abc
import time
from PythonScript.src.Controller import Controller
from PythonScript.src.DataProcessor.ElementFinder import ElementFinder
from PythonScript.src.ConfigureSettings import ConfigureSettings


class Event(object):
    
    __metaclass__ = abc.ABCMeta
    tolerance = ConfigureSettings().getTolerance('Event')
    
    def __init__(self, action:str, states: list):
        self.action = action
        self.stateNumber = 0
        self.state = states[self.stateNumber]

        
    def setController(self, controller):
        self.controller = controller
    
    def setIdentifier(self, identifier):
        self.identifier = identifier        
        
    def getState(self):
        return self.state
    
    
    def stepForward(self):
        if self.state != self.END:
            self.stateNumber += 1
            self._advance()
            print(self.state, ' now:', self.action)
            return True
        else: 
            return False
        
        
    def getAction(self):
        return self.action
    
    
    def setActionAndState(self, action, state):
        self.action = action
        self.state = state
    
        
    def _getScreenshot(self):
        screenshotter = Controller()
        return screenshotter.getScreenshot()
         
    def _getMatchPercent(self, elementFile):
        screenFile = self._getScreenshot()
        result = ElementFinder.matchPercentage(screenFile, elementFile)
        return result
    
    def _clicker(self, loc):
        self.controller.clickScreen(loc)
    
    def elementWaiter(self, element, tolerance=.9):
        elementExists  = self.identifier.elementExists(element, tolerance)
        print('Waiting for element...')
        while(not elementExists):
            time.sleep(.5)
            self.controller.getScreenshot()
            elementExists = self.identifier.elementExists(element, tolerance)
    
    def buttonWaiter(self):
        self.controller.getScreenshot()
        buttonExists  = self.identifier.buttonExists()
        print('Waiting for button...')
        while(not buttonExists):
            time.sleep(.5)
            self.controller.getScreenshot()
            buttonExists = self.identifier.buttonExists()
            
    def clickButton(self):
        loc = self.identifier.buttonIdentifier.getButtonLocation() 
        self.controller.clickScreen(loc)
        time.sleep(1)
        
    def waitForButtonAndClick(self):
        self.buttonWaiter()
        self.clickButton()
            
    
    @abc.abstractmethod
    def _advance(self):
        if not self.state or self.state != self.END:
            return None
        
        
    @abc.abstractmethod
    def takeAction(self):
        pass
        
    def __str__(self) -> str:
        return f'State:{self.state}, Action:{self.action}, StateNum:{self.stateNumber}'
