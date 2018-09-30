import unittest
from blackjack import *


class TestEndResults(unittest.TestCase):
    def setUp(self):
        self.dealer_hand = []
        self.player_hand = []
        self.player_hands = []

    def test_players_tie_with_dealer(self):
        self.dealer_hand = [("Hearts", 10), ("Clubs", 10)]
        player_one_hand = [("Diamonds", 10), ("Spades", 10)]
        player_two_hand = [("Spades", "Ace"), ("Hearts", 9)]
        self.player_hands.append(player_one_hand)
        self.player_hands.append(player_two_hand)
        test_player_chips = [500, 500]
        test_player_bids = [100, 100]
        reveal_results(self.dealer_hand, self.player_hands, test_player_chips, test_player_bids)
        self.assertEqual(test_player_chips[0], 500)
        self.assertEqual(test_player_chips[1], 500)

    def test_players_bust(self):
        self.dealer_hand = [("Hearts", 10), ("Clubs", 10)]
        player_one_hand = [("Diamonds", 10), ("Spades", 10), ("Clubs", 5)]
        player_two_hand = [("Spades", 5), ("Hearts", 9), ("Hearts", 10)]
        self.player_hands.append(player_one_hand)
        self.player_hands.append(player_two_hand)
        test_player_chips = [500, 500]
        test_player_bids = [100, 100]
        reveal_results(self.dealer_hand, self.player_hands, test_player_chips, test_player_bids)
        self.assertEqual(test_player_chips[0], 400)
        self.assertEqual(test_player_chips[1], 400)

    def test_players_and_dealer_blackjack(self):
        self.dealer_hand = [("Hearts", 10), ("Clubs", 10), ("Spades", "Ace")]
        player_one_hand = [("Diamonds", 10), ("Spades", 10), ("Clubs", "Ace")]
        player_two_hand = [("Spades", 5), ("Hearts", 6), ("Hearts", 10)]
        self.player_hands.append(player_one_hand)
        self.player_hands.append(player_two_hand)
        test_player_chips = [500, 500]
        test_player_bids = [100, 100]
        reveal_results(self.dealer_hand, self.player_hands, test_player_chips, test_player_bids)
        self.assertEqual(test_player_chips[0], 500)
        self.assertEqual(test_player_chips[1], 500)

    def test_dealer_is_bust(self):
        self.dealer_hand = [("Hearts", 10), ("Clubs", 10), ("Spades", 10)]
        player_one_hand = [("Diamonds", 8), ("Spades", 10), ("Clubs", "Ace")]
        player_two_hand = [("Spades", 5), ("Hearts", 6), ("Hearts", 9)]
        self.player_hands.append(player_one_hand)
        self.player_hands.append(player_two_hand)
        test_player_chips = [500, 500]
        test_player_bids = [100, 100]
        reveal_results(self.dealer_hand, self.player_hands, test_player_chips, test_player_bids)
        self.assertEqual(test_player_chips[0], 600)
        self.assertEqual(test_player_chips[1], 600)

    def test_player_only_blackjacks_wins_double(self):
        self.dealer_hand = [("Hearts", 10), ("Clubs", 10), ("Spades", 10)]
        player_one_hand = [("Diamonds", 10), ("Spades", 10), ("Clubs", "Ace")]
        player_two_hand = [("Spades", 5), ("Hearts", 6), ("Hearts", 10)]
        self.player_hands.append(player_one_hand)
        self.player_hands.append(player_two_hand)
        test_player_chips = [500, 500]
        test_player_bids = [100, 100]
        reveal_results(self.dealer_hand, self.player_hands, test_player_chips, test_player_bids)
        self.assertEqual(test_player_chips[0], 700)
        self.assertEqual(test_player_chips[1], 700)

    def test_player_wins_dealer_no_blackjack(self):
        self.dealer_hand = [("Hearts", 7), ("Clubs", 10)]
        player_one_hand = [("Diamonds", 10), ("Spades", 10), ]
        player_two_hand = [("Spades", 5), ("Hearts", 6), ("Hearts", 8)]
        self.player_hands.append(player_one_hand)
        self.player_hands.append(player_two_hand)
        test_player_chips = [500, 500]
        test_player_bids = [100, 100]
        reveal_results(self.dealer_hand, self.player_hands, test_player_chips, test_player_bids)
        self.assertEqual(test_player_chips[0], 600)
        self.assertEqual(test_player_chips[1], 600)

    def test_dealer_wins_no_blackjack(self):
        self.dealer_hand = [("Hearts", 9), ("Clubs", 10)]
        player_one_hand = [("Diamonds", 5), ("Spades", 10), ]
        player_two_hand = [("Spades", 7), ("Hearts", "Jack")]
        self.player_hands.append(player_one_hand)
        self.player_hands.append(player_two_hand)
        test_player_chips = [500, 500]
        test_player_bids = [100, 100]
        reveal_results(self.dealer_hand, self.player_hands, test_player_chips, test_player_bids)
        self.assertEqual(test_player_chips[0], 400)
        self.assertEqual(test_player_chips[1], 400)

    def test_player_one_wins_but_player_two_loses(self):
        self.dealer_hand = [("Hearts", 9), ("Clubs", 10)]
        player_one_hand = [("Diamonds", 10), ("Spades", 10), ]
        player_two_hand = [("Spades", 7), ("Hearts", "Jack")]
        self.player_hands.append(player_one_hand)
        self.player_hands.append(player_two_hand)
        test_player_chips = [500, 500]
        test_player_bids = [100, 100]
        reveal_results(self.dealer_hand, self.player_hands, test_player_chips, test_player_bids)
        self.assertEqual(test_player_chips[0], 600)
        self.assertEqual(test_player_chips[1], 400)

    def test_player_two_wins_but_player_one_loses(self):
        self.dealer_hand = [("Hearts", 7), ("Clubs", 10)]
        player_one_hand = [("Diamonds", 5), ("Spades", 10), ]
        player_two_hand = [("Spades", 8), ("Hearts", "Jack")]
        self.player_hands.append(player_one_hand)
        self.player_hands.append(player_two_hand)
        test_player_chips = [500, 500]
        test_player_bids = [100, 100]
        reveal_results(self.dealer_hand, self.player_hands, test_player_chips, test_player_bids)
        self.assertEqual(test_player_chips[0], 400)
        self.assertEqual(test_player_chips[1], 600)

    def test_three_players_one_wins_one_draws_one_loses(self):
        self.dealer_hand = [("Hearts", 7), ("Clubs", 10)]
        player_one_hand = [("Diamonds", 10), ("Spades", 10)]
        player_two_hand = [("Spades", 7), ("Hearts", "Jack")]
        player_three_hand = [("Spades", 5), ("Spades", "Jack"), ("Diamonds", "Jack")]
        self.player_hands.append(player_one_hand)
        self.player_hands.append(player_two_hand)
        self.player_hands.append(player_three_hand)
        test_player_chips = [500, 500, 500]
        test_player_bids = [100, 100, 100]
        reveal_results(self.dealer_hand, self.player_hands, test_player_chips, test_player_bids)
        self.assertEqual(test_player_chips[0], 600)
        self.assertEqual(test_player_chips[1], 500)
        self.assertEqual(test_player_chips[2], 400)

    def test_everybody_busts_everyone_loses(self):
        self.dealer_hand = [("Hearts", 7), ("Clubs", 10), ("Hearts", 10)]
        player_one_hand = [("Diamonds", 5), ("Diamonds", 10), ("Spades", 10)]
        player_two_hand = [("Spades", 7), ("Hearts", "Jack"), ("Hearts", "Queen")]
        player_three_hand = [("Spades", 5), ("Spades", "Jack"), ("Diamonds", "Jack")]
        self.player_hands.append(player_one_hand)
        self.player_hands.append(player_two_hand)
        self.player_hands.append(player_three_hand)
        test_player_chips = [500, 500, 500]
        test_player_bids = [100, 100, 100]
        reveal_results(self.dealer_hand, self.player_hands, test_player_chips, test_player_bids)
        self.assertEqual(test_player_chips[0], 400)
        self.assertEqual(test_player_chips[1], 400)
        self.assertEqual(test_player_chips[2], 400)

if __name__ == "__main__":
    unittest.main()


