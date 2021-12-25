import unittest
from unittest.mock import patch
from PythonScript.src.Navigator import Navigator

class TestPaintingIdentifier(unittest.TestCase):
    modulePrefix = 'PythonScript.src.Navigator.Navigator.PaintingIdentifier'
    

    def test_thirdRowTreasure(self):
        with patch(f'{self.modulePrefix}.getScreenFile') as mockFile:
            filePath = 'etc/images/treasurethirdrow.png'
            mockFile.return_value = filePath
            test = Navigator()
            self.assertTrue(test.treasureExists())
            
            
    def test_secondRowTreasure(self):
        with patch(f'{self.modulePrefix}.getScreenFile') as mockFile:
            filePath = 'etc/images/treasuresecondrow.png'
            mockFile.return_value = filePath
            test = Navigator()
            self.assertTrue(test.treasureExists())
                       
                       
    def test_noTreasure(self):
        with patch(f'{self.modulePrefix}.getScreenFile') as mockFile:
            filePath = 'etc/images/SamplePaintings.png'
            mockFile.return_value = filePath
            test = Navigator()
            self.assertFalse(test.treasureExists())
            
    
    
if __name__ == '__main__':
    unittest.main()


        