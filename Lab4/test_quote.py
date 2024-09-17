import unittest
from unittest import TestCase

import quote

class QuoteTest(TestCase):

    def test_quote_for_small_lawn_same_day(self):
        actual_quote = quote.lawn_quote('small', True)
        expected_quote = 15
        self.assertEqual(expected_quote, actual_quote)  # compare actual value and test value

    def test_quote_for_large_lawn_not_same_day(self):
        actual_quote = quote.lawn_quote('large', False)
        expected_quote = 20
        self.assertEqual(expected_quote, actual_quote)

    def test_quote_for_unrecognized_size(self):
        actual_quote = quote.lawn_quote('tiny', False)
        self.assertIsNone(actual_quote)     # check if the actual quote is None


if __name__ == '__main__':
    unittest.main()

