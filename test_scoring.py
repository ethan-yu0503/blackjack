import unittest
from blackjack import *


class TestBlackJack(unittest.TestCase):
    def setUp(self):
        self.dealer_hand = []
        self.player_hand = []
        self.player_hands = []

    def test_blackjack_with_one_ace(self):
        self.player_hand.append(("Spades", "Ace"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", "Jack"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", "Queen"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.assertEqual(blackjack(self.player_hand), True)

    def test_blackjack_with_no_aces(self):
        self.player_hand.append(("Spades", 2))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", 9))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", 4))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", 6))
        self.assertEqual(blackjack(self.player_hand), True)

    def test_one_ace_worth_eleven_points(self):
        self.player_hand.append(("Spades", "Ace"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", "Jack"))
        self.assertEqual(blackjack(self.player_hand), True)

    def test_two_aces_no_blackjack_safe(self):
        self.player_hand.append(("Spades", "Ace"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Diamonds", "Ace"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", "Jack"))
        self.assertEqual(calc_score(self.player_hand), 12)
        self.assertEqual(player_is_bust(self.player_hand), False)

    def test_three_aces_no_blackjack_safe(self):
        self.player_hand.append(("Spades", "Ace"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Diamonds", "Ace"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Clubs", "Ace"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", "Jack"))
        self.assertEqual(calc_score(self.player_hand), 13)
        self.assertEqual(player_is_bust(self.player_hand), False)

    def test_four_aces_no_blackjack_safe(self):
        self.player_hand.append(("Spades", "Ace"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Diamonds", "Ace"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Clubs", "Ace"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Hearts", "Ace"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", "Jack"))
        self.assertEqual(calc_score(self.player_hand), 14)
        self.assertEqual(player_is_bust(self.player_hand), False)

    def test_bust_with_thirty_points(self):
        self.player_hand.append(("Spades", "Jack"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", "Queen"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", "King"))
        self.assertEqual(calc_score(self.player_hand), 30)
        self.assertEqual(player_is_bust(self.player_hand), True)

    def test_bust_with_four_cards(self):
        self.player_hand.append(("Spades", 2))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", 5))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", 8))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Diamonds", 10))
        self.assertEqual(player_is_bust(self.player_hand), True)

    def test_two_cards_safe(self):
        self.player_hand.append(("Spades", 10))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", "Jack"))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.assertEqual(calc_score(self.player_hand), 20)

    def test_three_cards_safe(self):
        self.player_hand.append(("Spades", 5))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", 6))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", 9))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.assertEqual(calc_score(self.player_hand), 20)

    def test_four_cards_safe(self):
        self.player_hand.append(("Spades", 3))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", 4))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", 5))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.player_hand.append(("Spades", 8))
        self.assertEqual(player_is_bust(self.player_hand), False)
        self.assertEqual(calc_score(self.player_hand), 20)



if __name__ == "__main__":
    unittest.main()


