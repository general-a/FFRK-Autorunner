from PythonScript.src.DataProcessor.Paintings import TreasurePainting
from PythonScript.src.DataProcessor.Paintings.BossPainting import BossPainting
from PythonScript.src.DataProcessor.Paintings.ExplorationPainting import ExplorationPainting
from PythonScript.src.DataProcessor.Paintings.GreenCombatPainting import GreenCombatPainting
from PythonScript.src.DataProcessor.Paintings.OnslaughtPainting import OnslaughtPainting
from PythonScript.src.DataProcessor.Paintings.OrangeCombatPainting import OrangeCombatPainting
from PythonScript.src.DataProcessor.Paintings.PaintingFactory import PaintingFactory
from PythonScript.src.DataProcessor.Paintings.PortalPainting import PortalPainting
from PythonScript.src.DataProcessor.Paintings.RedCombatPainting import RedCombatPainting
from PythonScript.src.DataProcessor.Paintings.RestorationPainting import RestorationPainting
from PythonScript.src.DataProcessor.Paintings.TreasurePainting import TreasurePainting
import unittest

class TestPaintingFactory(unittest.TestCase):
    
    def test_FactoryReturnsTreasure(self):
        test = PaintingFactory.getPainting('treasure.png', (100, 100))
        self.assertIsInstance(test, TreasurePainting)
        self.assertEqual(test.getLocation(), (100, 100))
        self.assertEqual(test.getPaintingType(), "TREASURE")

    def test_FactoryReturnsBoss(self):
        test = PaintingFactory.getPainting('boss.png', (100, 100))
        self.assertIsInstance(test, BossPainting)
        self.assertEqual(test.getLocation(), (100, 100))
        self.assertEqual(test.getPaintingType(), "BOSS")

    def test_FactoryReturnsExploration(self):
        test = PaintingFactory.getPainting('exploration.png', (100, 100))
        self.assertIsInstance(test, ExplorationPainting)
        self.assertEqual(test.getLocation(), (100, 100))
        self.assertEqual(test.getPaintingType(), "EXPLORATION")

    def test_FactoryReturnsGreenCombat(self):
        test = PaintingFactory.getPainting('greencombat.png', (100, 100))
        self.assertIsInstance(test, GreenCombatPainting)
        self.assertEqual(test.getLocation(), (100, 100))
        self.assertEqual(test.getPaintingType(), "COMBAT")

    def test_FactoryReturnsOrangeCombat(self):
        test = PaintingFactory.getPainting('orangecombat.png', (100, 100))
        self.assertIsInstance(test, OrangeCombatPainting)
        self.assertEqual(test.getLocation(), (100, 100))
        self.assertEqual(test.getPaintingType(), "COMBAT")
        
    def test_FactoryReturnsRedCombat(self):
        test = PaintingFactory.getPainting('redcombat.png', (100, 100))
        self.assertIsInstance(test, RedCombatPainting)
        self.assertEqual(test.getLocation(), (100, 100))
        self.assertEqual(test.getPaintingType(), "COMBAT")
        
    def test_FactoryReturnsRestoration(self):
        test = PaintingFactory.getPainting('restoration.png', (100, 100))
        self.assertIsInstance(test, RestorationPainting)
        self.assertEqual(test.getLocation(), (100, 100))
        self.assertEqual(test.getPaintingType(), "EFFECT")
        
    def test_FactoryReturnsOnslaught(self):
        test = PaintingFactory.getPainting('onslaught.png', (100, 100))
        self.assertIsInstance(test, OnslaughtPainting)
        self.assertEqual(test.getLocation(), (100, 100))
        self.assertEqual(test.getPaintingType(), "EFFECT")

    def test_FactoryReturnsPortal(self):
        test = PaintingFactory.getPainting('portal.png', (100, 100))
        self.assertIsInstance(test, PortalPainting)
        self.assertEqual(test.getLocation(), (100, 100))
        self.assertEqual(test.getPaintingType(), "EFFECT")
        

    
if __name__ == '__main__':
    unittest.main()