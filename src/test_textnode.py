import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("Hello Mark", "bubba")
        node2 = TextNode("Hello Mark", "bubba")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("Word", "bold", "https://cnn.com")
        node2 = TextNode("Word", "bold", "https://cnn.com")
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode("Word", "bold")
        node2 = TextNode("Word", "bold", None)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different_text node", "bold")
        self.assertNotEqual(node, node2)

    def test_neq2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    print("in 'dunder main'") #never see
    unittest.main()
