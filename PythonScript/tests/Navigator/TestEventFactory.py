from PythonScript.src.Navigator.Events.EventFactory import EventFactory
from PythonScript.src.Navigator.Events.BossEvent import BossEvent
from PythonScript.src.Navigator.Events.ExplorationEvent import ExplorationEvent
from PythonScript.src.Navigator.Events.CombatEvent import CombatEvent
from PythonScript.src.Navigator.Events.LabyrinthEvent import LabyrinthEvent
from PythonScript.src.Navigator.Events.Proceed import Proceed
from PythonScript.src.Navigator.Events.TreasureEvent import TreasureEvent
import unittest
from unittest.mock import patch


class TestEventFactory(unittest.TestCase):
    
    def setUp(self):
        self.MODULE_PATH = 'PythonScript.src.Navigator.Events.'
    
    def test_FactoryBossEvent(self):
        test = EventFactory.getEvent('BOSS')
        self.assertIsInstance(test, BossEvent)
        for i in range(6):
            test.stepForward()
        self.assertEqual('START_LABYRINTH_EVENT', test.getAction())
        test.stepForward()
        self.assertEqual(None, test.getAction())
        
    @patch.object(CombatEvent, 'isFatigued')
    def test_FactoryCombatEventNoFatigue(self, mockFatigue):
        mockFatigue.return_value = False
        test = EventFactory.getEvent('COMBAT')
        self.assertIsInstance(test, CombatEvent)
        self.assertEqual('PROCEED', test.getAction())
        test.stepForward()
        self.assertEqual('PARTY_SELECTION', test.getAction())
        test.stepForward()
        self.assertEqual('WAIT', test.getAction())
        test.stepForward()
        self.assertEqual('CLICK_SKIP_BUTTON', test.getAction())
        test.stepForward()
        self.assertEqual('PROCEED', test.getAction())
        test.stepForward()
        self.assertEqual('NETWORK_WAIT', test.getAction())
        test.stepForward()
        self.assertEqual(None, test.getAction())

    @patch.object(CombatEvent, 'isFatigued')
    def test_FactoryCombatEventFatigue(self, mockFatigue):
        mockFatigue.return_value = True
        test = EventFactory.getEvent('COMBAT')
        self.assertIsInstance(test, CombatEvent)
        self.assertEqual('PROCEED', test.getAction())
        test.stepForward()
        self.assertEqual('PARTY_SELECTION', test.getAction())
        test.stepForward()
        self.assertEqual('CLICK_OK', test.getAction())
        test.stepForward()
        self.assertEqual('WAIT', test.getAction())
        test.stepForward()
        self.assertEqual('CLICK_SKIP_BUTTON', test.getAction())
        test.stepForward()
        self.assertEqual('PROCEED', test.getAction())
        test.stepForward()
        self.assertEqual('NETWORK_WAIT', test.getAction())
        test.stepForward()
        self.assertEqual(None, test.getAction())

    # def test_FactoryExplorationCombatEvent(self):
    #     test = EventFactory.getEvent('COMBAT', True)
    #     self.assertIsInstance(test, CombatEvent)
    #     self.assertEqual('PROCEED', test.getAction())
    #     test.stepForward()
    #     self.assertEqual('WAIT', test.getAction())
    #     test.stepForward()
    #     self.assertEqual('CLICK_SKIP_BUTTON', test.getAction())
    #     test.stepForward()
    #     self.assertEqual('PROCEED', test.getAction())
    #     test.stepForward()
    #     self.assertEqual(None, test.getAction())
    
    @patch.object(ExplorationEvent, 'isEvent')
    def test_FactoryExplorationEffect(self, mockedEvent):
        mockedEvent.return_value = True
        test = EventFactory.getEvent('EXPLORATION')
        self.assertIsInstance(test, ExplorationEvent)
        self.assertEqual('DETERMINE_STATE', test.getAction())
        test.stepForward()
        self.assertEqual('PROCEED', test.getAction())
        test.stepForward()
        self.assertEqual(None, test.getAction())

    @patch.object(ExplorationEvent, 'isEvent')
    @patch.object(ExplorationEvent, 'isTreasure')    
    @patch.object(ExplorationEvent, 'isDoor')
    def test_FactoryExplorationTreasure(self, mockedDoor, mockedTreasure, mockedEvent):
        mockedEvent.return_value = False
        mockedDoor.return_value = True
        mockedTreasure.return_value = True
        test = EventFactory.getEvent('EXPLORATION')
        self.assertIsInstance(test, ExplorationEvent)
        self.assertEqual('DETERMINE_STATE', test.getAction())
        test.stepForward()
        self.assertEqual('DETERMINE_DOOR_TYPE', test.getAction())
        test.stepForward()
        self.assertEqual('START_TREASURE_EVENT', test.getAction())
        test.stepForward()
        self.assertEqual(None, test.getAction())

    @patch.object(ExplorationEvent, 'isEvent')
    @patch.object(ExplorationEvent, 'isTreasure')    
    @patch.object(ExplorationEvent, 'isDoor')
    def test_FactoryExplorationDoor(self, mockedDoor, mockedTreasure, mockedEvent):
        mockedEvent.return_value = False
        mockedDoor.return_value = True
        mockedTreasure.return_value = False
        test = EventFactory.getEvent('EXPLORATION')
        self.assertIsInstance(test, ExplorationEvent)
        self.assertEqual('DETERMINE_STATE', test.getAction())
        test.stepForward()
        self.assertEqual('DETERMINE_DOOR_TYPE', test.getAction())
        test.stepForward()
        self.assertEqual('START_COMBAT_EVENT', test.getAction())
        test.stepForward()
        self.assertEqual(None, test.getAction())
    

    @patch.object(ExplorationEvent, 'isEvent')    
    @patch.object(ExplorationEvent, 'isDoor')
    @patch.object(ExplorationEvent, 'isBattle')
    def test_FactoryExplorationCombat(self, mockedCombat, mockedDoor, mockedEvent):
        mockedDoor.return_value = False
        mockedEvent.return_value = False
        mockedCombat.return_value = True
        test = EventFactory.getEvent('EXPLORATION')
        self.assertIsInstance(test, ExplorationEvent)
        self.assertEqual('DETERMINE_STATE', test.getAction())
        test.stepForward()
        self.assertEqual('START_COMBAT_EVENT', test.getAction())
        test.stepForward()
        self.assertEqual(None, test.getAction())
        
        
    def test_proceed(self):
        test = EventFactory.getEvent('EFFECT')
        self.assertIsInstance(test, Proceed)
        self.assertEqual('PROCEED', test.getAction())
        test.stepForward()
        self.assertEqual(None, test.getAction())
        
    def test_treasureEvent(self):
        test = EventFactory.getEvent('TREASURE')
        self.assertIsInstance(test, TreasureEvent)
        self.assertEqual('CLICK_MIDDLE_CHEST', test.getAction())
        test.stepForward()
        self.assertEqual('PROCEED', test.getAction())
        test.stepForward()
        self.assertEqual('PROCEED', test.getAction())
        test.stepForward()
        self.assertEqual('CLICK_OK', test.getAction())
        test.stepForward()
        self.assertEqual(None, test.getAction())
    
    def test_labyrinthEvent(self):
        test = EventFactory.getEvent('LABYRINTH')
        self.assertIsInstance(test, LabyrinthEvent)
        self.assertEqual('PROCEED', test.getAction())
        test.stepForward()
        self.assertEqual('PROCEED', test.getAction())
        test.stepForward()
        self.assertEqual('PROCEED', test.getAction())
        test.stepForward()
        self.assertEqual(None, test.getAction())
 
if __name__ == '__main__':
    unittest.main()
