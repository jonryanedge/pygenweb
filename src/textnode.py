from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "text"
    BOLD_TEXT = "bold"
    ITALICS_TEXT = "italics"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"


class TextNode():
    def __init__(self, content, text_type, ref):
        self.text = content
        self.type = TextType[text_type]
        self.url = ref

    def __eq__(self, compare):
        if compare.text == self.text and compare.type == self.type and compare.url == self.url:
            return True
        else:
            return False


    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"

