import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card('hearts', 8)
        self.card2 = Card('spade', 1)
        self.card3 = Card('diamonds', 9)
   
    def test_card_has_ace(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.card1))
        self.assertEqual(True, CardGame.check_for_ace(self, self.card2))
    
    def test_card1_has_highest_value(self):
        self.assertEqual(self.card1, CardGame.highest_card(self, self.card1, self.card2))
    
    def test_card2_has_highest_value(self):
        self.assertEqual(self.card3, CardGame.highest_card(self, self.card1, self.card3))
