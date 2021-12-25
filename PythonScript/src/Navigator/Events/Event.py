import abc
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
        
    @abc.abstractmethod
    def _advance(self):
        if not self.state or self.state != self.END:
            return None 
        
    def __str__(self) -> str:
        return f'State:{self.state}, Action:{self.action}, StateNum:{self.stateNumber}'

