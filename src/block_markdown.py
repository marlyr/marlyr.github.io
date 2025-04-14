from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    return [block.strip() for block in markdown.split("\n\n") if block.strip()]


def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    elif all(line.startswith("> ") for line in block.split("\n")):
        return BlockType.QUOTE
    
    elif all(line.startswith("- ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST
    
    elif block.startswith("1."):
        for i, line in enumerate(block.split("\n")):
            if not line.startswith(f"{i+1}. "):
                return BlockType.PARAGRAPH 
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
