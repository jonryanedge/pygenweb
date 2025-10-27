import unittest

from htmlnode import HTMLNode, LeafNode


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

if __name__ == "__main__":
    unittest.main()
