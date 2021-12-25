import unittest
from PythonScript.src.ConfigureSettings import ConfigureSettings

class TestConfigSettings(unittest.TestCase):
    
    def test_ValidScreenDimensions(self):
        dimensions = ConfigureSettings().getScreenDimensions()
        self.assertIsInstance(dimensions, tuple)
        for i in dimensions:
            self.assertIsInstance(i, int)



    
if __name__ == '__main__':
    unittest.main()