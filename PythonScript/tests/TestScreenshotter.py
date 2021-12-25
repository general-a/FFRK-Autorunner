import unittest
from PythonScript.src.Controller import Controller

class TestScreenshotter(unittest.TestCase):
    
    def test_ValidateScreenshotIsWorking(self):
        self.assertTrue(Controller().getScreenshot())
        

    
if __name__ == '__main__':
    unittest.main()