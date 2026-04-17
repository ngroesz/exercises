#!/usr/bin/env python3

import sys

CARD_VALUES_BY_RANK = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}


def sorted_rank_values_are_consecutive(sorted_rank_values):
    return all(value + 1 == sorted_rank_values[index + 1] for index, value in enumerate(sorted_rank_values[:-1]))


def sort_ranks_by_value(ranks):
    return sorted(ranks, key=lambda rank: CARD_VALUES_BY_RANK[rank])


def count_by_rank_value(rank_values):
    result = {}
    for rank_value in rank_values:
        if rank_value in result:
            result[rank_value] += 1
        else:
            result[rank_value] = 1
    return result


def sorted_rank_values_from_ranks(ranks):
    return sorted(
                list(
                    map(lambda r: CARD_VALUES_BY_RANK[r], ranks)
                )
            )


def hand_rank_and_value(hand):
    try:
        assert len(hand) == 5
    except AssertionError:
        print('Expected 5 cards. Got {} instead.'.format(len(hand)))

    ranks = [card[0:1] for card in hand]
    suits = [card[1:2] for card in hand]

    sorted_rank_values = sorted_rank_values_from_ranks(ranks)
    all_suits_are_equal = all(suit == suits[0] for suit in suits)

    if all_suits_are_equal:
        if sorted_rank_values == [10, 11, 12, 13, 14]:
            # royal flush
            return 9, [14]
        if sorted_rank_values_are_consecutive(sorted_rank_values):
            # straight flush
            return 8, [sorted_rank_values[-1]]

    counts_by_rank_value = count_by_rank_value(sorted_rank_values)
    rank_value_counts = list(counts_by_rank_value.values())

    if 4 in rank_value_counts:
        # four of a kind
        return (7,
                [next(v for v in counts_by_rank_value.keys() if counts_by_rank_value[v] == 4)])

    if 3 in rank_value_counts and 2 in rank_value_counts:
        # full house
        return (6,
                [next(v for v in counts_by_rank_value.keys() if counts_by_rank_value[v] == 2),
                 next(v for v in counts_by_rank_value.keys() if counts_by_rank_value[v] == 3)])

    if all_suits_are_equal:
        # flush
        return (5,
                sorted_rank_values)

    if sorted_rank_values_are_consecutive(sorted_rank_values):
        # straight
        return (4,
                sorted_rank_values)

    if 3 in rank_value_counts:
        # three of a kind
        return (3,
                [next(v for v in counts_by_rank_value.keys() if counts_by_rank_value[v] == 3)])

    if rank_value_counts.count(2) == 2:
        # two pair
        return (2,
                list(v for v in counts_by_rank_value.keys() if counts_by_rank_value[v] == 2))

    if 2 in rank_value_counts:
        # pair
        return (1,
                [next(v for v in counts_by_rank_value.keys() if counts_by_rank_value[v] == 2)])

    return (0,
            sorted_rank_values)


def declare_winner(hand_1, hand_2):
    hand_1_rank_and_value = hand_rank_and_value(hand_1)
    hand_2_rank_and_value = hand_rank_and_value(hand_2)

    if hand_1_rank_and_value[0] > hand_2_rank_and_value[0]:
        return 1
    elif hand_1_rank_and_value[0] < hand_2_rank_and_value[0]:
        return 2
    else:
        hand_1_values = hand_1_rank_and_value[1]
        hand_2_values = hand_2_rank_and_value[1]
        for index in range(len(hand_1_values) - 1, -1, -1):
            if hand_1_values[index] > hand_2_values[index]:
                return 1
            elif hand_1_values[index] < hand_2_values[index]:
                return 2

    sorted_hand_1_rank_values = sorted_rank_values_from_ranks([card[0:1] for card in hand_1])
    sorted_hand_2_rank_values = sorted_rank_values_from_ranks([card[0:1] for card in hand_2])

    for index in range(len(sorted_hand_1_rank_values) - 1, -1, -1):
        if sorted_hand_1_rank_values[index] > sorted_hand_2_rank_values[index]:
            return 1
        elif sorted_hand_1_rank_values[index] < sorted_hand_2_rank_values[index]:
            return 2

    raise RuntimeError('Could not evaluate hands {} and {}'.format(hand_1, hand_2))


def score_hands_from_file(filename):
    player_1_win_count = 0
    with open(filename) as file_handle:
        for line in file_handle:
            line = line.rstrip('\r\n')
            cards = line.split(' ')
            try:
                assert len(cards) == 10
            except AssertionError:
                print('Unexpected number of cards parsed ({}) from line {}'.format(len(cards), line))

            if (declare_winner(cards[0:5], cards[5:10]) == 1):
                player_1_win_count += 1

    print(str(player_1_win_count))

    return player_1_win_count


if __name__ == '__main__':
    filename = sys.argv[1]
    score_hands_from_file(filename)
