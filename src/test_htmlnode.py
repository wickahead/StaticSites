import unittest

# from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

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
        with self.assertRaises(ValueError) as cm:
            leaf_node_3.to_html()
        self.assertEqual(str(cm.exception), "All leaf nodes require a value.")

    # def test_leaf_raise_error_if_children_present(self): #This errors out on creation. Ignoring this test for now.
    #     leaf_node_4 = LeafNode("a", "value", [LeafNode("b", "Bold text"),LeafNode(None, "Normal text")],{"href": "https://www.google.com"})
    #     with self.assertRaises(TypeError) as cm:
    #         leaf_node_4.to_html()
    #     self.assertEqual(str(cm.exception), "TypeError: LeafNode.__init__() takes from 1 to 4 positional arguments but 5 were given")

    def test_raw_text(self):
        leaf_node_raw = LeafNode(None,"Raw text here. Nothing extra to see.")
        self.assertEqual(leaf_node_raw.to_html(), "Raw text here. Nothing extra to see.")

class TestParentNode(unittest.TestCase):
    def test_leaf_nodes(self):
        parent_node_1 = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),]) 
        self.assertEqual(parent_node_1.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_leaf_and_parent_nodes(self):
        p_node = ParentNode("p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],)
    
        p_node2 = ParentNode("p",
        [
            LeafNode("b", "Bubba1"),
            LeafNode(None, "Bubba2"),
            p_node,
            LeafNode("i", "Bubba3"),
            LeafNode(None, "Bubba4"),
        ],)
        # self.assertEqual(p_node2.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
        self.assertEqual(p_node2.to_html(), '<p><b>Bubba1</b>Bubba2<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>Bubba3</i>Bubba4</p>')

    def test_raise_error_no_children(self):
        parent_node_2 = ParentNode("p", None)
        with self.assertRaises(ValueError) as cm:
            parent_node_2.to_html()
        self.assertEqual(str(cm.exception), "ParentNode objects must have children.")

    def test_raise_error_no_tag(self):
        parent_node_3 = ParentNode(None,[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),])
        with self.assertRaises(ValueError) as cm:
            parent_node_3.to_html()
        self.assertEqual(str(cm.exception), "Tag cannot be empty.")



if __name__ == "__main__":
    print("in 'dunder main'") #never see
    unittest.main()
