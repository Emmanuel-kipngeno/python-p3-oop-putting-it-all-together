import unittest
from unittest.mock import patch
from book import Book
import io

class TestBook(unittest.TestCase):
    '''Book in book.py'''

    def test_has_title_and_page_count(self):
        '''has the title and page_count passed into __init__, and values can be set to a new instance.'''
        book = Book("And Then There Were None", 272, 19.99)
        self.assertEqual(book.page_count, 272)
        self.assertEqual(book.title, "And Then There Were None")
        self.assertEqual(book.price, 19.99)

    def test_requires_int_page_count(self):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        book = Book("And Then There Were None", 272, 19.99)

        # Use io.StringIO directly for both stdout and stderr
        captured_out = io.StringIO()
        captured_err = io.StringIO()

        with patch('sys.stdout', new_callable=lambda: captured_out), \
             patch('sys.stderr', new_callable=lambda: captured_err):

            book.page_count = "not an integer"

        # Reset sys.stdout and sys.stderr to their original values
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        self.assertEqual(captured_out.getvalue(), '')
        self.assertEqual(captured_err.getvalue(), "page_count must be an integer\n")

    def test_can_turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
        book = Book("The World According to Garp", 69, 19.99)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            book.turn_page()
            self.assertEqual(mock_stdout.getvalue(), "Flipping the page...wow, you read fast!\n")

if __name__ == '__main__':
    unittest.main()
