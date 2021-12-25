import unittest
from PythonScript.src.DataProcessor.ButtonIdentifier import ButtonIdentifier
from PythonScript.src.Helper.LocationHelper import LocationHelper

class TestButtonIdentifier(unittest.TestCase):

    def test_GetNextButton(self):
        image = 'etc/images/battlescreen.png'
        test = ButtonIdentifier(image)
        loc = test.getNextButton()
        self.assertEqual((308,928), loc)

    def test_GetSkipButton(self):
        image = 'etc/images/winscreen.png'
        test = ButtonIdentifier(image)
        loc = test.getSkipButton()
        self.assertEqual((491, 841), loc)
        
    def test_GetCloseButton(self):
        image = 'etc/images/testing/end.png'
        test = ButtonIdentifier(image)
        loc = test.getCloseButton()
        self.assertEqual((282, 865), loc)

    def test_GetOkButton(self):
        image = 'etc/images/testing/leavetreasure.png'
        test = ButtonIdentifier(image)
        loc = test.getOkButton()
        #LocationHelper.makeLocation(image, [loc])
        self.assertEqual((396, 642), loc)

if __name__ == '__main__':
    unittest.main()