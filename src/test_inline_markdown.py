import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_single_delim(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])
    def test_two_delims(self):
        node = TextNode("This is **text** with **two** bold words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes, [
            TextNode("This is ",TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with ", TextType.TEXT),
            TextNode("two", TextType.BOLD),
            TextNode(" bold words", TextType.TEXT),
        ])
    
    def test_invalid_markdown(self):
        node = TextNode("This is **text with **invalid** syntax", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.TEXT)
    
    def test_other_text_type(self):
        node = TextNode("This is a link", TextType.LINK, "www.link.com")
        self.assertEqual([node], split_nodes_delimiter([node], "", TextType.LINK))

class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another image](https://i.imgur.com/alxpMKU.jpeg)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("another image", 'https://i.imgur.com/alxpMKU.jpeg')], matches)
    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images(
            "This is text with an no images but a [link](https://www.link.com)"
        )
        self.assertListEqual([], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.link.com) and [another link](https://www.anotherlink.com)"
        )
        self.assertListEqual([("link", "https://www.link.com"), ("another link", "https://www.anotherlink.com")], matches)
    def test_extract_markdown_links_none(self):
        matches = extract_markdown_images(
            "This is text with an no link but a [image](https://www.image.com)"
        )
        self.assertListEqual([], matches)

class TestSplitNodesImage(unittest.TestCase):
    def test_one_image(self):
        node = TextNode(
                    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
                    TextType.TEXT,
                )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )

    def test_multiple_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_only_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_invalid_image(self):
        node = TextNode(
            "[image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("[image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_other_text_type(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.IMAGE,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.IMAGE),
            ],
            new_nodes,
        )
    

class TestSplitNodesLink(unittest.TestCase):
    def test_one_link(self):
        node = TextNode(
                    "This is text with a [link](https://www.link.com)",
                    TextType.TEXT,
                )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.link.com")
            ],
            new_nodes,
        )

    def test_multiple_link(self):
        node = TextNode(
            "This is text with a [link](https://www.link.com) and [another link](https://www.anotherlink.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.link.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "another link", TextType.LINK, "https://www.anotherlink.com"
                ),
            ],
            new_nodes,
        )

    def test_only_link(self):
        node = TextNode(
            "[link](https://www.link.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://www.link.com"),
            ],
            new_nodes,
        )

    def test_invalid_link(self):
        node = TextNode(
            "![link](https://www.link.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("![link](https://www.link.com)", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_other_text_type(self):
        node = TextNode(
            "[link](https://www.link.com)",
            TextType.LINK,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("[link](https://www.link.com)", TextType.LINK),
            ],
            new_nodes,
        ) 

class TestTextToTextNodes(unittest.TestCase):
    def test_all(self):
        nodes =  text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")

        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ]

        # Check if the nodes returned by the function match the expected ones
        self.assertListEqual(nodes, expected_nodes)
    
    def test_none(self):
        nodes =  text_to_textnodes("This is plain text")

        expected_nodes = [
            TextNode("This is plain text", TextType.TEXT),
        ]

        # Check if the nodes returned by the function match the expected ones
        self.assertListEqual(nodes, expected_nodes)
    