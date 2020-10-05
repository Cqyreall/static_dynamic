import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        card1 = Card('hearts', 8)
        card2 = Card('spade', 1)
        card3 = Card('diamonds', 9)
        self.cards = [card1, card2, card3]
   
    def test_card_has_ace(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.cards[0]))
        self.assertEqual(True, CardGame.check_for_ace(self, self.cards[1]))
    
    def test_card1_has_highest_value(self):
        self.assertEqual(self.cards[0], CardGame.highest_card(self, self.cards[0], self.cards[1]))
    
    def test_card2_has_highest_value(self):
        self.assertEqual(self.cards[2], CardGame.highest_card(self, self.cards[0], self.cards[2]))

    def test_total(self):
        self.assertEqual('You have a total of 18', CardGame.cards_total(self, self.cards))
