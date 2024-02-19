import unittest
from speakit import clean_word, count_frequency, get_matching_words

class TestWordFrequency(unittest.TestCase):
    def setUp(self):
        # Define some sample data for testing
        self.lines = [
            "This is a test file for checking the functionality of the code.",
            "It contains some words like cielo, camicia, civile, perciò, etc.",
            "We will use this file to test if the code correctly retrieves words containing a given substring."
        ]

    def test_clean_word(self):
        # Test the clean_word function
        self.assertEqual(clean_word("cielo"), "cielo")
        self.assertEqual(clean_word("Camicia!"), "camicia")
        self.assertEqual(clean_word("perciò"), "perciò")
        self.assertIsNone(clean_word("123"))
        self.assertIsNone(clean_word("l'ufficio"))

    def test_count_frequency(self):
        # Test the count_frequency function
        freq = count_frequency(self.lines)
        self.assertEqual(freq["cielo"], 1)
        self.assertEqual(freq["camicia"], 1)
        self.assertEqual(freq["perciò"], 1)
        self.assertEqual(freq["code"], 1)  # Testing a non-existing word
        self.assertEqual(freq["this"], 1)  # Testing case-insensitivity

    def test_get_matching_words(self):
        # Test the get_matching_words function
        freq = {"cielo": 1, "camicia": 1, "perciò": 1}
        self.assertEqual(get_matching_words(freq, "ci"), ["cielo", "camicia", "civile", "perciò", "rancio", "cucina", "cielo"])

if __name__ == '__main__':
    unittest.main()
