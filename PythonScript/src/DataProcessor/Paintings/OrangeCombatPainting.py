from PythonScript.src.DataProcessor.Paintings.Painting import Painting

class OrangeCombatPainting(Painting):
    
    def __init__(self, location) -> None:
        super().__init__(5, 'COMBAT', 'orangecombat.png', location)

    
    