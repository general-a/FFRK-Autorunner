from PythonScript.src.DataProcessor.Paintings.Painting import Painting

class RestorationPainting(Painting):
    
    def __init__(self, location) -> None:
        super().__init__(2, 'EFFECT', 'restoration.png', location)

    
    