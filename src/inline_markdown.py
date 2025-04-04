import re
from textnode import TextNode, TextType   

DELIMITERS = {
    TextType.BOLD: "**",
    TextType.ITALIC: "_",
    TextType.CODE: "```"

}

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        while delimiter in remaining_text:
            start_idx = remaining_text.find(delimiter)
            if start_idx > 0:
                new_nodes.append(TextNode(remaining_text[:start_idx], TextType.TEXT))
            content_start = start_idx + len(delimiter)
            end_idx = remaining_text.find(delimiter, content_start)
            if end_idx == -1:
                raise Exception("Invalid Markdown syntax. Missing closing delimiter.")
            
            new_nodes.append(TextNode(remaining_text[content_start:end_idx], text_type))
            remaining_text = remaining_text[end_idx + len(delimiter):]

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_url(node, type):
    new_nodes = []
    if node.text_type == TextType.TEXT:
        text = node.text
        parts = []

        if type == TextType.IMAGE:
            matches = extract_markdown_images(text)
        elif type == TextType.LINK:
            matches = extract_markdown_links(text)

        if not matches:
            new_nodes.append(node)
            return new_nodes
        
        for link_text, url in matches:
            if type == TextType.IMAGE:
                pattern = f'![{link_text}]({url})'
            elif type == TextType.LINK:
                pattern = f'[{link_text}]({url})'
            before, after = text.split(pattern, maxsplit=1)
            if before:
                parts.append(TextNode(before, TextType.TEXT))
            parts.append(TextNode(link_text, type, url=url))
            text = after
        
        if text:
            parts.append(TextNode(text, TextType.TEXT))
        
        new_nodes.extend(parts)
    else:
        new_nodes.append(node)
        
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_nodes_url(node, TextType.IMAGE))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_nodes_url(node, TextType.LINK))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes

