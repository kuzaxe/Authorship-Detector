import unittest
import author_functions as af

class TestAverageWordLength(unittest.TestCase):

    failure_message = '''
When we called {}, we expected this:
{}
but your code returned this:
{}'''

    def approx(self, v1, v2):
        """ (float, float) -> bool

        Return True iff v1 and v2 are approximately equal.
        """
        #error_margin = 0.0001
        error_margin = 0.0

        return v1 - error_margin <= v2 <= v1 + error_margin

    def prototype_test(self, text, expected):
        call = 'author_functions.avg_word_length({})'.format(text)
        returned = af.avg_word_length(text)
        msg = TestAverageWordLength.failure_message.format(call, expected,
                                                           returned)
        #self.assertEqual(returned, expected, msg)
        #Use next line if we want to allow some error margin
        self.assertTrue(self.approx(returned, expected), msg)

    def test_01_single_line_one_word(self):
        text = ["simple\n"]
        expected = 6.0
        self.prototype_test(text, expected)

    def test_02_two_lines_two_words(self):
        text = ["two\n","lines\n"]
        expected = 4.0
        self.prototype_test(text, expected)

    def test_03_multiple_words_single_line(self):
        text = ["multiple words single line\n"]
        expected = 5.75
        self.prototype_test(text, expected)

    def test_04_single_line_one_word_with_punctuation(self):
        text = [",,,simple:\n"]
        expected = 6.0
        self.prototype_test(text, expected)

    def test_05_two_lines_two_words_with_punctuation(self):
        text = ["two,\n", "lines!\n"]
        expected = 4.0
        self.prototype_test(text, expected)

    def test_06_multiple_words_single_line_with_punctuation(self):
        text = ["multiple \"words\" single line?\n"]
        expected = 5.75
        self.prototype_test(text, expected)

    def test_07_single_line_multiple_words_internal_punctuation(self):
        text = ["multi-word lines, gotta check'em!\n"]
        expected = 7.0
        self.prototype_test(text, expected)

    def test_08_single_line_all_punctuation_words(self):
        text = ["Not even a word !!?!\n"]
        expected = 3.0
        self.prototype_test(text, expected)

if __name__ == '__main__':
    unittest.main()

