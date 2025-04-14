import re

from htmlnode import ParentNode
from block_markdown import BlockType
from block_markdown import markdown_to_blocks, block_to_block_type
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        
        tag = block_type_to_tag(block_type, block)
        
        if block_type == BlockType.PARAGRAPH:
            block = block.replace("\n", " ")

        elif block_type == BlockType.QUOTE:
            block = "\n".join([line.lstrip(">").strip() for line in block.split("\n")])

        elif block_type == BlockType.HEADING:
            block_nodes.extend(heading_to_nodes(block))
            continue

        elif block_type in [BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST]:
            block_nodes.append(list_to_node(block, tag))
            continue

        elif block_type == BlockType.CODE:
            block_nodes.append(code_to_node(block))
            continue

        children = text_to_children(block)
        html_node = ParentNode(tag, children)
        block_nodes.append(html_node)
    
    return ParentNode("div", block_nodes)


def block_type_to_tag(block_type, block):
    match block_type:
        case BlockType.HEADING:
            stripped_string = block.rstrip(" ")
            count = len(stripped_string) - len(stripped_string.lstrip("#"))
            return f"h{count}"

        case BlockType.QUOTE:
            return "blockquote"
        
        case BlockType.UNORDERED_LIST:
            return "ul"
        
        case BlockType.ORDERED_LIST:
            return "ol"
        
        case BlockType.CODE:
            return "pre"
        
        case BlockType.PARAGRAPH:
            return "p"
        
        case _:
            raise Exception("Invalid block type")


def text_to_children(text):
    children = []
    nodes = text_to_textnodes(text)
    
    
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)

    return children



def heading_to_nodes(block):
    nodes = []

    for line in block.split("\n"):
        if not re.match(r"^#{1,6} ", line):
            continue
        heading_level = len(re.match(r"^#+", line).group(0))
        heading_text = re.sub(r"^#+\s*", "", line.strip())

        inline_nodes = text_to_children(heading_text)

        tag = f"h{heading_level}"

        nodes.append(ParentNode(tag, inline_nodes))

    return nodes


def code_to_node(block):
    code_content = block.strip("`").strip() + "\n"
    node = TextNode(code_content, TextType.CODE)
    html_node = text_node_to_html_node(node)
    return ParentNode("pre", [html_node])

def list_to_node(block, tag):
    children = []

    for line in block.split("\n"):
        if not line.strip():
            continue
        
        if tag == "ul":
            text = re.sub(r"^[-*+]\s+", "", line)
        elif tag == "ol":
            text = re.sub(r"^\d+\.\s+", "", line)
        
        
        inline_nodes = text_to_children(text)
        children.append(ParentNode("li", inline_nodes))

    return ParentNode(tag, children)


def unordered_list_to_node(block):
    return list_to_node(block, "ul")


def ordered_list_to_node(block):
    return list_to_node(block, "ol")


txt = """
## The Art of **World-Building**
"""

node = markdown_to_html_node(txt)
html = node.to_html()