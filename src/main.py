from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    # thing1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # thing2 = TextNode("This is a another text node", "italic", "https://www.wickahead.dev")
    # thing3 = TextNode("This is a yet another text node", "code", "https://www.boot.dev")
    # print (f"thing1 is {thing1}")
    # print (f"thing2 is {thing2}")
    # print (f"thing3 is {thing3}")

    # #(self, tag=None, value=None, children=None, props=None):
    # hnode1 = HTMLNode("p", "Hello world")
    # hnode2 = HTMLNode("a", None , None, {"href": "https://www.google.com", "target": "_blank"})
    # print(f"hnode1 is {hnode1}")
    # print(f"hnode2 is {hnode2}")
    # hnode2.props_to_html()

    # leaf1 = LeafNode("p", "This is a paragraph of text.")
    # leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    # print(f"leaf1 is {leaf1}")
    # print(f"leaf1.to_html() is {leaf1.to_html()}")
    
    # print(f"leaf2 is {leaf2}")
    # print(f"leaf2.to_html() is {leaf2.to_html()}")

    p_node = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
    ],)
    print(f"p_node is {p_node}")
    print(f"p_node.to_html() is {p_node.to_html()}")
    

    
    pass

main()
# print("hello world")