import unittest

# from textnode import TextNode
from htmlnode import HTMLNode, LeafNode

#(self, tag=None, value=None, children=None, props=None):

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        hnode2 = HTMLNode("a", None , None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(hnode2.props_to_html(), ' href="https://www.google.com" target="_blank"')

class TestLeafNode(unittest.TestCase):
    def test_p_tag(self):
        leaf_node_1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf_node_1.to_html(), '<p>This is a paragraph of text.</p>')

    def test_a_tag(self):
        leaf_node_2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node_2.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_raise_error_if_no_value(self):
        leaf_node_3 = LeafNode("a", None, {"href": "https://www.google.com"})
        #works (but not checking error msg)
        # with self.assertRaises(ValueError):
        #     leaf_node_3.to_html()
        with self.assertRaises(ValueError) as cm:
            leaf_node_3.to_html()
        self.assertEqual(str(cm.exception), "All leaf nodes require a value.")

    def test_raw_text(self):
        leaf_node_raw = LeafNode(None,"Raw text here. Nothing extra to see.")
        self.assertEqual(leaf_node_raw.to_html(), "Raw text here. Nothing extra to see.")

# class ParentNode

if __name__ == "__main__":
    print("in 'dunder main'") #never see
    unittest.main()
