"""
Items have prices but can also have a special price (n items for X).

Calculate prices of all the items in the cart

From a vaguely-remembered Codility problem.
"""



prices = {
    'A': {'price': 50, 'special': {'count': 3, 'price': 120}},
    'B': {'price': 70},
    'C': {'price': 100, 'special': {'count': 4, 'price': 300}},
}

cart = [
    {'item': 'A', 'count': 4}, # 120 + 50 == 170
    {'item': 'B', 'count': 2}, # 2 * 70 == 140
    {'item': 'C', 'count': 2}, # 2 * 100 == 200
]                              # 170 + 140 + 200 = 510


def checkout(cart):
    total = 0

    for items in cart:
        total += price_of_n_items(items['item'], items['count'])

    return total


def price_of_n_items(item, count):
    price = 0
    items_remaining_to_be_checked_out = count

    if 'special' in prices[item] and count >= prices[item]['special']['count']:
        special_count = int(count / prices[item]['special']['count'])
        price += special_count * prices[item]['special']['price']
        items_remaining_to_be_checked_out = count % prices[item]['special']['count']

    price += items_remaining_to_be_checked_out * prices[item]['price']

    return price


if __name__ == '__main__':
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(checkout(cart), 510)

