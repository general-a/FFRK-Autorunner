from PythonScript.src.DataProcessor.Paintings.Painting import Painting

class OnslaughtPainting(Painting):
    
    def __init__(self, location) -> None:
        super().__init__(4, 'EFFECT', 'onslaught.png', location)

    
    