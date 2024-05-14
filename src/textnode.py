# class TextNode(text, text_type, url=None):
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # def __eq__(self, text1, text_type1, url1):
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    def __repr__(self):
        return_str = "TextNode(" + self.text + ", " + self.text_type + ", " + self.url + ")"
        # print (return_str)
        return return_str
