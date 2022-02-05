from PythonScript.src.Navigator.Events.Event import Event
import unittest
from unittest.mock import patch

class TestEventFactory(unittest.TestCase):
    
    @patch.object(Event, '_getScreenshot')
    def test_isDoor(self, mockedFile):
        mockedFile.return_value = 'etc/images/testing/door.png'
        test = Event('t', 't')
        res = test._getMatchPercent('etc/images/elements/door.png')
        self.assertAlmostEqual(res, 1, 5)


    @patch.object(Event, '_getScreenshot')
    def test_notDoor(self, mockedFile):
        mockedFile.return_value = 'etc/images/testing/s1.png'
        test = Event('t', 't')
        res = test._getMatchPercent('etc/images/elements/door.png')
        self.assertLess(res, .5)
             
             
    @patch.object(Event, '_getScreenshot')
    def test_isEvent(self, mockedFile):
        mockedFile.return_value = 'etc/images/testing/event.png'
        test = Event('t', 't')
        res = test._getMatchPercent('etc/images/elements/moveon.png')
        self.assertAlmostEqual(res, 1, 5)


    @patch.object(Event, '_getScreenshot')
    def test_notEvent(self, mockedFile):
        mockedFile.return_value = 'etc/images/testing/s2.png'
        test = Event('t', 't')
        res = test._getMatchPercent('etc/images/elements/moveon.png')
        self.assertLess(res, .7)


    @patch.object(Event, '_getScreenshot')
    def test_isEvent(self, mockedFile):
        mockedFile.return_value = 'etc/images/testing/fatigued.png'
        test = Event('t', 't')
        res = test._getMatchPercent('etc/images/elements/fatigue.png')
        self.assertAlmostEqual(res, 1, 5)


    @patch.object(Event, '_getScreenshot')
    def test_notEvent(self, mockedFile):
        mockedFile.return_value = 'etc/images/testing/s1.png'
        test = Event('t', 't')
        res = test._getMatchPercent('etc/images/elements/fatigue.png')
        self.assertLess(res, .7)
        
        
    @patch.object(Event, '_getScreenshot')
    def test_enterButton(self, mockedFile):             
        mockedFile.return_value = 'etc/images/testing/partysel.png'
        test = Event('t', 't')
        res = test._getMatchPercent('etc/images/Buttons/enter.png')
        print(res)
        




if __name__ == '__main__':
    unittest.main()
