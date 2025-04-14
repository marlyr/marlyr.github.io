import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, url="www.link.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "www.link.com"})
    
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, url="www.image.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.image.com", "alt": "This is an image node"})