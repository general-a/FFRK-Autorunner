import unittest
from unittest.mock import patch
from PythonScript.src.DataProcessor.PaintingIdentifier import PaintingIdentifier

class TestPaintingIdentifier(unittest.TestCase):
    modulePrefix = 'PythonScript.src.DataProcessor.PaintingIdentifier.ConfigureSettings'
    
    def setUp(self) -> None:
        self.posOne = (107, 498)
        self.posTwo = (280, 496)
        self.posThree = (453, 498)
    

    def test_getPaintingsAllTheSame(self):
        with patch(f'{self.modulePrefix}.getScreenFile') as mockFile:
            filePath = 'etc/images/testing/treasure.png'
            mockFile.return_value = filePath
            test = PaintingIdentifier()
            test.getPaintings()
            self.assertEqual(filePath, test.getScreenFile())
        painting = test.paintings[0]
        self.assertTrue(self.closePoints(self.posThree, painting.location))
        self.assertEqual(painting.paintingType, 'TREASURE')
        painting = test.paintings[1]
        self.assertTrue(self.closePoints(self.posOne, painting.location))
        self.assertEqual(painting.paintingType, 'COMBAT')
        painting = test.paintings[2]
        self.assertTrue(self.closePoints(self.posTwo, painting.location))
        self.assertEqual(painting.paintingType, 'COMBAT')


    # def test_getPaintingsBoss(self):
    #     with patch(f'{self.modulePrefix}.getScreenFile') as mockFile:
    #         filePath = 'etc/images/treasure.png'
    #         mockFile.return_value = filePath
    #         test = PaintingIdentifier()
    #         test.getPaintings()
    #     self.assertEqual(filePath, test.getScreenFile())
    #     painting = test.paintings[0]
    #     self.assertTrue(self.closePoints(self.posThree, painting.location))
    #     self.assertEqual(painting.paintingType, 'TREASURE')
    #     painting = test.paintings[1]
    #     self.assertTrue(self.closePoints(self.posTwo, painting.location))
    #     self.assertEqual(painting.paintingType, 'EXPLORATION')
    #     painting = test.paintings[2]
    #     self.assertTrue(self.closePoints(self.posOne, painting.location))
    #     self.assertEqual(painting.paintingType, 'BOSS')
        
    def test_getPaintingsPortal(self):
        with patch(f'{self.modulePrefix}.getScreenFile') as mockFile:
            filePath = 'etc/images/testing/s3.png'
            mockFile.return_value = filePath
            test = PaintingIdentifier()
            test.getPaintings()
            self.assertEqual(filePath, test.getScreenFile())
        painting = test.paintings[0]
        self.assertTrue(self.closePoints(self.posTwo, painting.location))
        self.assertEqual(painting.paintingType, 'EXPLORATION')
        painting = test.paintings[1]
        self.assertTrue(self.closePoints(self.posOne, painting.location))
        self.assertEqual(painting.paintingType, 'COMBAT')
        painting = test.paintings[2]
        self.assertTrue(self.closePoints(self.posThree, painting.location))
        self.assertEqual(painting.paintingType, 'EFFECT')    
    
    def test_getPaintingsOnslaught(self):
        with patch(f'{self.modulePrefix}.getScreenFile') as mockFile:
            filePath = 'etc/images/testing/s1.png'
            mockFile.return_value = filePath
            test = PaintingIdentifier()
            test.getPaintings()
            self.assertEqual(filePath, test.getScreenFile())
        painting = test.paintings[0]
        self.assertTrue(self.closePoints(self.posOne, painting.location))
        self.assertEqual(painting.paintingType, 'EFFECT')
        painting = test.paintings[1]
        self.assertTrue(self.closePoints(self.posTwo, painting.location))
        self.assertEqual(painting.paintingType, 'COMBAT')
        painting = test.paintings[2]
        self.assertTrue(self.closePoints(self.posThree, painting.location))
        self.assertEqual(painting.paintingType, 'COMBAT')    
    
    
    def test_getPaintingsOrange(self):
        with patch(f'{self.modulePrefix}.getScreenFile') as mockFile:
            filePath = 'etc/images/testing/s2.png'
            mockFile.return_value = filePath
            test = PaintingIdentifier()
            test.getPaintings()
            self.assertEqual(filePath, test.getScreenFile())
        painting = test.paintings[0]
        self.assertTrue(self.closePoints(self.posTwo, painting.location))
        self.assertEqual(painting.paintingType, 'EXPLORATION')
        painting = test.paintings[1]
        self.assertTrue(self.closePoints(self.posThree, painting.location))
        self.assertEqual(painting.paintingType, 'COMBAT')
        painting = test.paintings[2]
        self.assertTrue(self.closePoints(self.posOne, painting.location))
        self.assertEqual(painting.paintingType, 'COMBAT')  
          
    def test_nonPainting(self):
        with patch(f'{self.modulePrefix}.getScreenFile') as mockFile:
            filePath = 'etc/images/testing/battleend.png'
            mockFile.return_value = filePath
            test = PaintingIdentifier()
            test.getPaintings()
            self.assertEqual(filePath, test.getScreenFile())
        self.assertEqual(test.paintings, [])
 
    def test_inBattle(self):
        with patch(f'{self.modulePrefix}.getScreenFile') as mockFile:
            filePath = 'etc/images/testing/battleend.png'
            mockFile.return_value = filePath
            test = PaintingIdentifier()
            self.assertEqual(filePath, test.getScreenFile())
            self.assertFalse(test.inBattle())

    def test_inBattleBar(self):
        with patch(f'{self.modulePrefix}.getScreenFile') as mockFile:
            filePath = 'etc/images/testing/s1.png'
            mockFile.return_value = filePath
            test = PaintingIdentifier()
            self.assertEqual(filePath, test.getScreenFile())
            self.assertTrue(test.inBattle())
            
    def closePoints(self, a, b):
        return 10 > (a[0] - b[0] + a[1] - b[1])



    
if __name__ == '__main__':
    unittest.main()

