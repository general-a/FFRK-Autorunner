from PythonScript.src.DataProcessor.Paintings.BossPainting import Painting

class PortalPainting(Painting):
    
    def __init__(self, location) -> None:
        super().__init__(10, 'EFFECT', 'portal.png', location)

    
        