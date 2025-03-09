class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        return vars(self) == vars(other)
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return " ".join(map(lambda items: f'{items[0]}="{items[1]}"', self.props.items()))
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Value was not provided")
        if self.tag is None:
            return self.value
        if self.props:
            props_html = self.props_to_html()
            return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag was not provided")
        if self.children is None:
            raise ValueError("Children were not provided")
        
        child_nodes = []
        for child in self.children:
            child_nodes.append(child.to_html())
        return f"<{self.tag}>{''.join(child_nodes)}</{self.tag}>"
