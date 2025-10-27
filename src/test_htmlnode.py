import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "p", 
            "This is a paragraph", 
            None, 
            {"class":"intro", "id":"intro"},
        )
        self.assertEqual(node.props_to_html(), ' class="intro" id="intro"')

    def test_values(self):
        node = HTMLNode("a", "Click here", None, {"href":"https://google.com", "target":"_blank"})
        self.assertEqual(
            node.tag, 
            "a",
        )
        self.assertEqual(
            node.value, 
            "Click here",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://google.com" target="_blank"',
        )

    def test_repr(self):
        node = HTMLNode("div", "This is the way", None, {"class": "content"})
        self.assertEqual(
            node.__repr__(), 
            "HTMLNode(div, This is the way, children: None, {'class': 'content'})",
        )

    def test_leaf_to_html(self):
        leaf = LeafNode("p", "This is a leaf paragraph")
        self.assertEqual(leaf.to_html(), "<p>This is a leaf paragraph</p>")

    def test_leaf_to_html_a(self):
        leaf = LeafNode("a", "Click me", {"href": "https://google.com"})
        self.assertEqual(
            leaf.to_html(),
            '<a href="https://google.com">Click me</a>',
        )

    def test_parent_to_html(self):
        parent = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "normal text"),
            ],
        )
        self.assertEqual(parent.to_html(),
                         "<p><b>Bold text</b>Normal text<i>italic text</i>normal text</p>")
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )



if __name__ == "__main__":
    unittest.main()
