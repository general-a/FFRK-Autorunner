import PythonScript.src.DataProcessor.Paintings
from PythonScript.src.DataProcessor.Paintings.ExplorationPainting import ExplorationPainting
from PythonScript.src.DataProcessor.Paintings.GreenCombatPainting import GreenCombatPainting
from PythonScript.src.DataProcessor.Paintings.OrangeCombatPainting import OrangeCombatPainting
from PythonScript.src.DataProcessor.Paintings.RedCombatPainting import RedCombatPainting
from PythonScript.src.DataProcessor.Paintings.RestorationPainting import RestorationPainting
from PythonScript.src.DataProcessor.Paintings.OnslaughtPainting import OnslaughtPainting
from PythonScript.src.DataProcessor.Paintings.PortalPainting import PortalPainting
from PythonScript.src.DataProcessor.Paintings.BossPainting import BossPainting
from PythonScript.src.DataProcessor.Paintings.TreasurePainting import TreasurePainting

class PaintingFactory:

    @staticmethod
    def getPainting(paintingType: str, location: tuple):
        if not paintingType:
            return None

        if paintingType == 'exploration.png':
            return ExplorationPainting(location)
        elif paintingType == 'greencombat.png':
            return GreenCombatPainting(location)
        elif paintingType == 'orangecombat.png':
            return OrangeCombatPainting(location)
        elif paintingType == 'redcombat.png':
            return RedCombatPainting(location)
        elif paintingType == 'restoration.png':
            return RestorationPainting(location)
        elif paintingType == 'onslaught.png':
            return OnslaughtPainting(location)
        elif paintingType == 'portal.png':
            return PortalPainting(location)
        elif paintingType == 'boss.png':
            return BossPainting(location)
        elif paintingType == 'treasure.png':
            return TreasurePainting(location)
        else:
            raise ValueError(paintingType)

