import os
import tempfile
import unittest

from poker_hands import (
    count_by_rank_value,
    declare_winner,
    hand_rank_and_value,
    score_hands_from_file,
    sorted_rank_values_are_consecutive,
    sort_ranks_by_value)


class TestPokerHands(unittest.TestCase):
    def test_score_hands_from_file(self):
        self.score_file = tempfile.NamedTemporaryFile(mode='w', delete=False)

        with self.score_file as f:
            f.write("9S 2C 9H 4C 8D AS 7D 3D 6D 5S\n")
            f.write("6S 4C 7H 8C 3H 5H JC AH 9D 9C")

        self.assertEqual(
            score_hands_from_file(self.score_file.name),
            1
        )

        os.unlink(self.score_file.name)

    def test_sort_ranks_by_value(self):
        self.assertEqual(
            sort_ranks_by_value(['7', '5', 'K', '5', 'Q', 'J', '6', 'A']),
            ['5', '5', '6', '7', 'J', 'Q', 'K', 'A']
        )

    def test_sorted_rank_values_are_consecutive(self):
        self.assertTrue(
            sorted_rank_values_are_consecutive([9, 10, 11, 12, 13])
        )
        self.assertFalse(
            sorted_rank_values_are_consecutive([9, 10, 11, 11, 12])
        )

    def test_count_by_rank_value(self):
        self.assertEqual(
            count_by_rank_value([10, 11, 10, 12, 10]),
            {
                10: 3,
                11: 1,
                12: 1
            }
        )

    def test_hand_rank_and_value(self):
        self.assertEqual(
            hand_rank_and_value(['JH', 'TH', 'QH', 'AH', 'KH']),
            (9, [14])
        )

        self.assertEqual(
            hand_rank_and_value(['JH', 'TH', 'QH', 'KH', '9H']),
            (8, [13])
        )

        self.assertEqual(
            hand_rank_and_value(['3D', '3H', '3S', '3C', '2H']),
            (7, [3])
        )

        self.assertEqual(
            hand_rank_and_value(['6H', '6D', '2C', '6S', '2D']),
            (6, [2, 6])
        )

        self.assertEqual(
            hand_rank_and_value(['5S', '6S', 'AS', 'KS', '4S']),
            (5, [4, 5, 6, 13, 14])
        )

        self.assertEqual(
            hand_rank_and_value(['2H', '5H', '4S', '3D', '6D']),
            (4, [2, 3, 4, 5, 6])
        )

        self.assertEqual(
            hand_rank_and_value(['2H', '5H', '2S', '3D', '2C']),
            (3, [2])
        )

        self.assertEqual(
            hand_rank_and_value(['AS', 'KH', 'QH', 'AD', 'QD']),
            (2, [12, 14])
        )

        self.assertEqual(
            hand_rank_and_value(['2C', '3S', '8S', '8D', 'TD']),
            (1, [8])
        )

        self.assertEqual(
            hand_rank_and_value(['5D', '8C', '9S', 'JS', 'AC']),
            (0, [5, 8, 9, 11, 14])
        )

    def test_declare_winner(self):
        self.assertEqual(
            declare_winner(
                ['5H', '5C', '6S', '7S', 'KD'],
                ['2C', '3S', '8S', '8D', 'TD']
            ),
            2
        )

        self.assertEqual(
            declare_winner(
                ['5D', '8C', '9S', 'JS', 'AC'],
                ['2C', '5C', '7D', '8S', 'QH']
            ),
            1
        )

        self.assertEqual(
            declare_winner(
                ['2D', '9C', 'AS', 'AH', 'AC'],
                ['3D', '6D', '7D', 'TD', 'QD']
            ),
            2
        )

        self.assertEqual(
            declare_winner(
                ['4D', '6S', '9H', 'QH', 'QC'],
                ['3D', '6D', '7H', 'QD', 'QS']
            ),
            1
        )

        self.assertEqual(
            declare_winner(
                ['2H', '2D', '4C', '4D', '4S'],
                ['3C', '3D', '3S', '9S', '9D']
            ),
            1
        )


if __name__ == '__main__':
    unittest.main()
