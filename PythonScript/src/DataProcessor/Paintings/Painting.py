import abc
from PythonScript.src.Navigator.Events.CombatEvent import CombatEvent
from PythonScript.src.Navigator.Events.EventFactory import EventFactory

class Painting(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, priority: int, paintingType: str, fileName: str, location: tuple):
        self.priority = priority
        self.paintingType = paintingType
        self.fileName = fileName
        self.location = location
        
    def setPriority(self, priority):
        self.priority = priority
        
    def setController(self, controller):
        self.controller = controller
        
        
    def setIdentifier(self, identifier):
        self.identifier = identifier
        
    def setPartyChooser(self, partyChooser):
        self.partyChooser = partyChooser
    
    def getPriority(self):
        return self.priority
    
    def getPaintingType(self):
        return self.paintingType

    def getFileName(self):
        return self.fileName

    def getLocation(self):
        return self.location
    
    def startEvent(self, event=None, explorationCombat=False):
        if not explorationCombat:
            if event == None:
                event = self.paintingType
            self.event = EventFactory.getEvent(event)
            if isinstance(self.event, CombatEvent):
                self.event.setPartyChooser(self.partyChooser)

        else:
            self.event = EventFactory.getEvent(event, True)
            self.event.setPartyChooser(self.partyChooser)
            
        self.event.setController(self.controller)
        self.event.setIdentifier(self.identifier)
        return self._getAction()
        
    def nextAction(self):
        self.event.stepForward()
        return self._getAction()
    
    def _getAction(self):
        if self.event:
            return self.event.getAction()
        else:
            return 'Error'
    
    # High "priority" means worse choice..
    def __lt__(self, other):
        if self.priority == other.priority:
            return self.location[0] < other.location[0]
        else:
            return self.priority < other.priority
    
    def __gt__(self, other):
        if self.priority == other.priority:
            return self.location[0] > other.location[0]
        else:
            return self.priority > other.priority
    
    def __eq__(self, other):
        return self.priority == other.priority
    
    def __str__(self) -> str:
        return str(self.__class__)
    
