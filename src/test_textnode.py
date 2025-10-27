import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a italic text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_moreuneq(self):
        node = TextNode("This is not a bold text node", TextType.TEXT)
        node2 = TextNode("This is not a italic text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_urls(self):
        node = TextNode("This is a link text node", TextType.LINK, "https://google.com")
        node2 = TextNode("This is a link text node", TextType.LINK, "https://google.com")
        self.assertEqual(node, node2)

    def test_links(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "https://edgeworth.net/assets/king.png")
        node2 = TextNode("This is a link text node", TextType.IMAGE, "assets/king.png")
        self.assertNotEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
