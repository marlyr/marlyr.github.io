import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a code node", TextType.CODE)
        self.assertNotEqual(node, node2)
    def test_url(self):
        node = TextNode("This a link node", TextType.LINK, "www.webkinz.com")
        self.assertEqual(node.url, "www.webkinz.com")
    def test_urlnone(self):
        node = TextNode("This not a link node", TextType.BOLD)
        self.assertIsNone(node.url)