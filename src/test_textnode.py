import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
