# Unit Test cases for Assignment.py

import unittest
from Assignment import FrequencyAnalyser


class TestFrequencyAnalyser(unittest.TestCase):
    """Tests for Assignment.py"""

    def test_calculate_highest_frequency(self):
        """Tests cases for method calculate_highest_frequency"""

        self.assertEqual(FrequencyAnalyser().calculate_highest_frequency(
            'This is the the first input string'), 2)

        self.assertEqual(FrequencyAnalyser().calculate_highest_frequency(
            'Here we are testing the occurance of a word'), 1)

        self.assertEqual(FrequencyAnalyser().calculate_highest_frequency(
            'May be this will give a different result'), 1)

        # An exception is generated when a numerical string is used as input
        with self.assertRaises(Exception):
            FrequencyAnalyser().calculate_highest_frequency(
                '9999999999999')

    def test_calculate_frequency_for_word(self):
        """Test cases for method calculate_frequency_for_word"""

        self.assertEqual(FrequencyAnalyser().calculate_frequency_for_word(
            'This is the the first input string', 'the'), 2)

        self.assertEqual(FrequencyAnalyser().calculate_frequency_for_word(
             'Here we are testing the occurance of a word', 'the'), 1)

        self.assertEqual(FrequencyAnalyser().calculate_frequency_for_word(
             'May be this will give a different result', 'be'), 1)

        # An exception is generated when a word which is not present in the input text is searched
        with self.assertRaises(Exception):
            FrequencyAnalyser().calculate_frequency_for_word(
                'May be this will give a different result', 'abc')

    def test_calculate_most_frequent_nwords(self):
        """Test cases for method calculate_most_frequent_nwords"""

        self.assertEqual(FrequencyAnalyser().calculate_most_frequent_nwords(
             'This is the the first input string', str(3)), [('the', 2), ('first', 1), ('input', 1)])

        self.assertEqual(FrequencyAnalyser().calculate_most_frequent_nwords(
             'Here we are testing the occurrence of a word', str(2)), [('a', 1), ('are', 1)])

        self.assertEqual(FrequencyAnalyser().calculate_most_frequent_nwords(
             'May be this will give a different result', str(2)), [('a', 1), ('be', 1)])

        # An exception is generated when a non-numerical character is provided as input for N words
        with self.assertRaises(Exception):
            FrequencyAnalyser().calculate_most_frequent_nwords(
                'May be this will give a different result', 'abc')


if __name__ == '__main__':
    unittest.main()


