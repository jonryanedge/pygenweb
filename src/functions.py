import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            start = node.text
            parts = start.split(delimiter)
            for i in range(len(parts)):
                if i % 2 == 0:
                    new_node = TextNode(parts[i], TextType.TEXT)
                else:
                    new_node = TextNode(parts[i], text_type)
                new_nodes.append(new_node)

    return new_nodes

def extract_markdown_images(text):
    alt_matches = re.findall(r"!\[(.*?)\]", text)
    src_matches = re.findall(r"\((http.*?)\)", text)
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)

    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)

    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            splits = extract_markdown_images(node.text)
            num_parts = len(splits)
            for i in range(num_parts):
                part = node.text.split(f"![{splits[i][0]}]({splits[i][1])")
            parts = node.text.split("!")


def split_nodes_link(old_nodes):
