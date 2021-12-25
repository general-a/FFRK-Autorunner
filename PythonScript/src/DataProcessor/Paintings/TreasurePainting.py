from PythonScript.src.DataProcessor.Paintings.Painting import Painting

class TreasurePainting(Painting):
    
    def __init__(self, location) -> None:
        super().__init__(0, 'TREASURE', 'treasure.png', location)
        
    
