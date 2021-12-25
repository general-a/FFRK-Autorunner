import unittest
from PythonScript.src.DataProcessor.ElementFinder import ElementFinder

class TestElementFinder(unittest.TestCase):
    
    def test_FindOneElement(self):
        elementLoc = ElementFinder.findOneElement('etc/images/labyEnter.png', 'etc/images/enterButton.png')
        self.assertIsInstance(elementLoc, tuple)
        self.assertEqual((277, 876), elementLoc)


    def test_FindMultipleElements(self):
        elementLoc = ElementFinder.findMultipleElements('etc/images/SamplePaintings.png', 'etc/images/CombatEz.png', threshold=.99)
        self.assertIsInstance(elementLoc, tuple)
        self.assertEqual(((106, 499), (279, 499), (452, 499)), elementLoc)
        
    def test_MatchPercentage(self):
        res = ElementFinder.matchPercentage('etc/images/leave.png', 'etc/images/elements/fatigue.png')
        self.assertAlmostEqual(0.87642443, res)
        res = ElementFinder.matchPercentage('etc/images/testfatigue.png', 'etc/images/elements/fatigue.png')
        self.assertAlmostEqual(0.8951634, res)
 



    
if __name__ == '__main__':
    unittest.main()