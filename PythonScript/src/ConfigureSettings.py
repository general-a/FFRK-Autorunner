from configparser import ConfigParser


class ConfigureSettings:
    
    def __init__(self):
        self.configurer = ConfigParser()
        self.configurer.read('etc\Config\config.ini')

    
    def getScreenDimensions(self):
        screenDims = []
        names = ['left', 'top', 'width', 'height']
        dimensions = dict(self.configurer.items('GameWindow'))
        for i in names:
            screenDims.append(int(dimensions.get(i)))
        return tuple(screenDims)

    def getTolerance(self, toleranceType='Global'):
        tolerance = self.configurer.get('Tolerances', toleranceType)
        return float(tolerance)
    
    def getFileFromPath(self, filename):
        return self.configurer.get('Paths', filename)
    
    def getScreenFile(self):
        path = self.configurer.get('Paths', 'ScreenPath')
        screen = self.configurer.get('Paths', 'ScreenFile')
        return f'{path}{screen}'
    
    
    def _getList(self, section, option):
        value = self.configurer.get(section, option)
        return list(filter(None, (x.strip() for x in value.splitlines())))

    
    def getPaintingList(self):
        return [str(x) for x in self._getList('Paths', 'PaintingFiles')]

    def getTreasureList(self):
        return [str(x) for x in self._getList('Paths', 'TreasureFiles')]

if __name__ == '__main__':
    test = ConfigureSettings()
    a = test.getFileFromPath('DoorFile')
    print(a)