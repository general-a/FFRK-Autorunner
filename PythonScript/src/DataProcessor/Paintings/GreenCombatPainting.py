from PythonScript.src.DataProcessor.Paintings.Painting import Painting

class GreenCombatPainting(Painting):
    
    def __init__(self, location: tuple) -> None:
        super().__init__(6, 'COMBAT', 'greencombat.png', location)

    
        