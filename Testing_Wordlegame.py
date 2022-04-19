import unittest
import Hw10_Wordle

class wordle_test(unittest.TestCase):

    def test_get_init(self):
            result = Hw10_Wordle.get_init()
            self.assertEqual(result,expected_result)

    def test_get_word(self):
            result = Hw10_Wordle.get_word()
            self.assertEqual(result,expected_result)

    def test_access_word(self):
            result = Hw10_Wordle.access_word()
            self.assertEqual(result,expected_result)

    def test_parsed_rule_code(self):
        result = Hw10_Wordle.parsed_rule_code()
        self.assertEqual(result,expected_result)

    def test_apply_Rule(self):
        result = Hw10_Wordle.apply_rule()
        self.assertEqual(result,expected_result)

    def test_get_user_input(self):
            result = Hw10_Wordle.get_user_input()
            self.assertEqual(result,expected_result)

    def test_check_if_entered_word_is_valid(self):
            result = Hw10_Wordle.check_if_entered_word_is_valid()
            self.assertEqual(result,expected_result)

    def test_user_guessed_the_right_word(self):
            result = Hw10_Wordle.user_guessed_the_right_word()
            self.assertEqual(result,expected_result)

    def test_check_valid_word(self):
            result = Hw10_Wordle.check_valid_word()
            self.assertEqual(result,expected_result)

    def test_get_spot_name(self):
            result = Hw10_Wordle.get_spot_name()
            self.assertEqual(result,expected_result)

    def test_check_word_in_dictionary(self):
            result = Hw10_Wordlee.check_word_in_dictionary()
            self.assertEqual(result,expected_result)

    def test_get_final(self):
            result = Hw10_Wordle.get_final()
            self.assertEqual(result,expected_result)

    def test_find_words(self):
            result = Hw10_Wordle.get_find_words()
            self.assertEqual(result,expected_result)

    def test_match_word_alphabets(self):
            result = Hw10_Wordle.get_matched_word_alphabets()
            self.assertEqual(result,expected_result)

    def test_solve(self):
            result = Hw10_Wordle.get_solve()
            self.assertEqual(result,expected_result)

    def __init__(self):
        result = Hw10_Wordle.__init__()
        self.assertEqual(result,expected_result)

    def test_get_words(self):
        result = Hw10_Wordle.get_words()
        self.assertEqual(result,expected_result)

    def test_set_words(self):
        result = Hw10_Wordle.set_words()
        self.assertEqual(result,expected_result)

    def test_get_test_words(self):
        result = Hw10_Wordle.get_test_words()
        self.assertEqual(result,expected_result)

    def test_get_Rule_Input(self):
        result = Hw10_Wordle.get_Rule_Input()
        self.assertEqual(result,expected_result)

    def test_Interact(self):
        result = Hw10_Wordle.Interact()
        self.assertEqual(result,expected_result)

    def __str__(self):
        result = Hw10_Wordle.__str__()
        self.assertEqual(result,expected_result)


if __name__ == '__main__':
            unittest.main()
