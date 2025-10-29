import unittest

from textnode import TextNode, TextType
from functions import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestTextNodeSplit(unittest.TestCase):
    def test_split_1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_2(self):
        node = TextNode("This is text with a _couple italic_ words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("couple italic", TextType.ITALIC),
            TextNode(" words", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_3(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

class TestMarkdownExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_images(self):
        matches = extract_markdown_images(
            "Pineapple ![picture of pineapple](https://google.com/pineapple) goes on Pizza ![picture of pizza](https://google.com/pizza)"
        )
        self.assertListEqual([("picture of pineapple", "https://google.com/pineapple"), ("picture of pizza", "https://google.com/pizza")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Searching for things is easy with [Google.com](https://google.com). Try it now!"
        )
        self.assertListEqual([("Google.com", "https://google.com")], matches)

if __name__ == "__main__":
    unittest.main()

