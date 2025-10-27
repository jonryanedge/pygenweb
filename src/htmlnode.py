from enum import Enum

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(self, tag, value, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf nodes must have a value")

        if not self.tag:
            return f"{self.value}"

        return f"<{self.tag}>{self.value}{super().props_to_html()}</{self.tag}>"
