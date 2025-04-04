import unittest

from block_markdown import BlockType
from block_markdown import markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_one_block(self):
        md = """
This is **bolded** paragraph
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
            ],
        )

    def test_one_enter(self):
        md = """
This is **bolded** paragraph
This is still on the same line
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph\nThis is still on the same line",
            ],
        )

    def test_empty_blocks(self):
        md = """
This is **bolded** paragraph



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_1(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
    
    def test_heading_6(self):
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
    
    def test_incorrect_heading(self):
        self.assertEqual(block_to_block_type("########## Too many hashes"), BlockType.PARAGRAPH)
        
    def test_no_space_heading(self):
        self.assertEqual(block_to_block_type("#This is wrong!"), BlockType.PARAGRAPH)

    def test_code(self):
        self.assertEqual(block_to_block_type("``` This is code ```"), BlockType.CODE)

    def test_incomplete_code(self):
        self.assertEqual(block_to_block_type("```` This is not code ``"), BlockType.PARAGRAPH)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)

    def test_quote_lines(self):
        self.assertEqual(block_to_block_type("> This is a quote\n> with a second line"), BlockType.QUOTE)

    def test_incorrect_quote(self):
        self.assertEqual(block_to_block_type(">This is not a quote"), BlockType.PARAGRAPH)
    
    def test_missing_quote(self):
        self.assertEqual(block_to_block_type("> This could be a quote\nbut this line ruins it"), BlockType.PARAGRAPH)
    
    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- an unordered list"), BlockType.UNORDERED_LIST)

    def test_incorrect_unordered_list(self):
        self.assertEqual(block_to_block_type("-not an unordered list"), BlockType.PARAGRAPH)

    def test_incorrect_unordered_list_line(self):
        self.assertEqual(block_to_block_type("- this could be an unordered list\nbut this line ruins it"), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. This\n2. is\n3. an\n4. ordered\n5. list"), BlockType.ORDERED_LIST)
    
    def test_incorrect_ordered_list(self):
        self.assertEqual(block_to_block_type("1.This isn't an ordered list"), BlockType.PARAGRAPH)

    def test_incorrect_ordered_list_line(self):
        self.assertEqual(block_to_block_type("1. This could be an ordered list\nbut this line ruins it"), BlockType.PARAGRAPH)

    def test_incorrect_ordered_0_start(self):
        self.assertEqual(block_to_block_type("0. This isn't an ordered list"), BlockType.PARAGRAPH)
    
    def test_incorrect_increment_ordered_list(self):
        self.assertEqual(block_to_block_type("1. This isn't an ordered list\n3. Because the number is wrong"), BlockType.PARAGRAPH)
    
    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is just a plain paragraph"), BlockType.PARAGRAPH)