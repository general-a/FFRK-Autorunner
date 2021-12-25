from PythonScript.src.DataProcessor.ElementFinder import ElementFinder
from PythonScript.src.ConfigureSettings import ConfigureSettings
from PythonScript.src.Helper.LocationHelper import LocationHelper


class PartyChooser:
    
    def __init__(self) -> None:
        configuerer = ConfigureSettings()
        self.screenFile = configuerer.getFileFromPath('PartyFile')
        self.partyImage = configuerer.getFileFromPath('PartyLabelFile')
        self.tolerance = configuerer.getTolerance('Party')
        self.partyLocations = self.locateParties()
        self.currentPartyPosition = 0
        
    def getParty(self):
        currentParty = self.partyLocations[self.currentPartyPosition]
        self._nextParty()
        return currentParty
    

    def _nextParty(self):
        self.currentPartyPosition = (self.currentPartyPosition + 1) % 3
             
    def locateParties(self):
        locs = ElementFinder.findMultipleElements(self.screenFile, self.partyImage, self.tolerance)
        trueLocations = []
        for i in locs:
            trueLocations.append((i[0], i[1] + 50))
        LocationHelper.makeLocation(self.screenFile, trueLocations)
        return trueLocations    


if __name__ == '__main__':
    test = PartyChooser()
    test.getParty()
    test.getParty()
    test.getParty()
    test.getParty()
    
    