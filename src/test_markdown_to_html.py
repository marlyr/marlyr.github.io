import unittest

from htmlnode import ParentNode
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
> This is a quote
> in markdown
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        '<div><blockquote>This is a quote\nin markdown</blockquote></div>'
    )
        
    def test_headings(self):
        md = """
# This is a big heading
###### and a little one
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        '<div><h1>This is a big heading</h1><h6>and a little one</h6></div>'
    )
    
    def test_unordered_list(self):
        md = """
- This is an
- Unordered list
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        '<div><ul><li>This is an</li><li>Unordered list</li></ul></div>'
    )
        
    def test_ordered_list(self):
        md = """
1. This is an
2. Ordered list
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        '<div><ol><li>This is an</li><li>Ordered list</li></ol></div>'
    )
      
    def test_quote_and_lists(self):
        md = """
> This is a quote

- List item 1
- List item 2

> Another quote

1. Ordered list item
2. Another ordered item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><blockquote>This is a quote</blockquote><ul><li>List item 1</li><li>List item 2</li></ul><blockquote>Another quote</blockquote><ol><li>Ordered list item</li><li>Another ordered item</li></ol></div>'
        )


    def test_mixed_paragraph_and_code(self):
        md = """
This is a paragraph with some **bold** text.

And here is some inline `code` in the middle of the paragraph.

Another paragraph with _italic_ text and `more code`.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is a paragraph with some <b>bold</b> text.</p><p>And here is some inline <code>code</code> in the middle of the paragraph.</p><p>Another paragraph with <i>italic</i> text and <code>more code</code>.</p></div>'
        )

    def test_headings_with_lists_and_paragraphs(self):
        md = """
# Main Heading

This is a paragraph.

- List item 1
- List item 2

## Subheading

Another paragraph under the subheading.

1. Ordered list item
2. Another ordered item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Main Heading</h1><p>This is a paragraph.</p><ul><li>List item 1</li><li>List item 2</li></ul><h2>Subheading</h2><p>Another paragraph under the subheading.</p><ol><li>Ordered list item</li><li>Another ordered item</li></ol></div>'
        )

    def test_complex_mixed_elements(self):
        md = """
# Heading

Here is a paragraph with `inline` code.

> This is a blockquote with some **bold** and _italic_ text inside it.

1. First ordered list item
2. Second ordered list item

Here is a paragraph after the list.

![Alt text](image_url)

[Link Text](https://example.com)
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Heading</h1><p>Here is a paragraph with <code>inline</code> code.</p><blockquote>This is a blockquote with some <b>bold</b> and <i>italic</i> text inside it.</blockquote><ol><li>First ordered list item</li><li>Second ordered list item</li></ol><p>Here is a paragraph after the list.</p><p><img src="image_url" alt="Alt text"></img></p><p><a href="https://example.com">Link Text</a></p></div>'
        )
    def test_bold_and_italic_in_headings(self):
        md = """
## The Art of **World-Building**
### Some _Italic_ in Headings
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h2>The Art of <b>World-Building</b></h2><h3>Some <i>Italic</i> in Headings</h3></div>'
        )
