import unittest

from markdown_utils import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_header(self):
        md = "# Header"
        self.assertEqual(extract_title(md), "Header")

    def test_multiple_headers(self):
        md = "## Hello\n# First Header\n# Second Header"
        self.assertEqual(extract_title(md), "First Header")

    def test_no_header(self):
        md = "## No H1 header here"
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "No H1 header found in the markdown")

if __name__ == "__main__":
    unittest.main()